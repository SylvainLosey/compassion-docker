# This file is to be executed with https://www.pyinvoke.org/
import json
import shutil
from io import StringIO
from pathlib import Path
from textwrap import dedent

from invoke import task

ESSENTIALS = ("git", "python3", "curl")


def _load_copier_settings(c):
    """Load copier.yml from outside of poetry venv."""
    with StringIO() as fd:
        c.run(
            dedent(
                """
                poetry run python -c '
                import json, yaml
                with open("copier.yml") as copier_fd:
                    print(json.dumps(yaml.safe_load(copier_fd.read())))
                '
                """
            ),
            out_stream=fd,
        )
        return json.loads(fd.getvalue())


@task
def check_dependencies(c):
    """Check essential development dependencies are present."""
    failures = []
    for dependency in ESSENTIALS:
        try:
            c.run(f"{dependency} --version", hide=True)
        except Exception:
            failures.append(dependency)
    if failures:
        print(f"Missing essential dependencies: {failures}")


@task(check_dependencies)
def develop(c, force=False):
    """Set up a development environment."""
    if not force and (Path(c.cwd) / ".venv").is_dir():
        print(".venv directory already exists, skipping. Use --force otherwise.")
        return
    c.run("git submodule update --init --checkout --recursive")
    # Ensure poetry is installed
    try:
        c.run("poetry --version")
    except Exception:
        # Official installation method of poetry
        c.run(
            "curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3"
        )
    # Use poetry to set up development environment in a local venv
    c.run("python3 -m venv .venv")
    c.run("poetry env use .venv/bin/python")
    c.run("poetry install")
    c.run("poetry run pre-commit install")


@task(develop)
def lint(c, verbose=False):
    """Lint & format source code."""
    flags = ["--show-diff-on-failure", "--all-files", "--color=always"]
    if verbose:
        flags.append("--verbose")
    flags = " ".join(flags)
    c.run(f"poetry run pre-commit run {flags}")


@task(develop)
def test(c, verbose=False):
    """Test project."""
    flags = ["-nauto", "--color=yes"]
    if verbose:
        flags.append("-vv")
    flags = " ".join(flags)
    c.run(f"poetry run pytest {flags} tests")


@task(develop)
def update_test_scaffoldings(c):
    """Update default scaffolding renderings."""
    # Make sure git repo is clean
    try:
        c.run("git diff --quiet --exit-code")
    except Exception:
        print("git repo is dirty; clean it and repeat")
        raise
    copier_settings = _load_copier_settings(c)
    default_settings_path = Path("tests") / "default_settings"
    shutil.rmtree(default_settings_path)
    default_settings_path.mkdir()
    try:
        c.run("git tag --force test")
        for odoo_version in copier_settings["odoo_version"]["choices"]:
            v = f"{odoo_version:.1f}"
            c.run(
                f"poetry run copier -fr HEAD -d odoo_version={v} "
                f"copy . {default_settings_path / f'v{v}'}"
            )
    finally:
        c.run("git tag --delete test")

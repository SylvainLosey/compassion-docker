import pytest
from copier.main import copy
from plumbum import local
from plumbum.cmd import diff, git

from .helpers import COPIER_SETTINGS


@pytest.mark.parametrize("odoo_version", COPIER_SETTINGS["odoo_version"]["choices"])
def test_default_settings(tmpdir, odoo_version):
    src, dst = tmpdir / "src", tmpdir / "dst"
    patch = git("diff")
    git("clone", ".", src)
    with local.cwd(src):
        (git["apply", "--reject"] << patch)()
        git("add", ".")
        git(
            "commit",
            "--author=Test<test@test>",
            "--message=test",
            "--allow-empty",
            "--no-verify",
        )
        git("tag", "--force", "test")
        copy(
            ".",
            str(dst),
            vcs_ref="test",
            force=True,
            data={"odoo_version": odoo_version},
        )
    diff(
        "--context=3",
        "--recursive",
        local.cwd / "tests" / "default_settings" / f"v{odoo_version:.1f}",
        dst,
    )

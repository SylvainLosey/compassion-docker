[![Doodba deployment](https://img.shields.io/badge/deplyment-doodba-informational)](https://github.com/Tecnativa/doodba)
[![Boost Software License 1.0](https://img.shields.io/badge/license-bsl--1.0-important)](https://choosealicense.com/licenses/bsl-1.0/)

# Doodba scaffolding

This project lets you spin up up [Odoo][] projects based on [Doodba][] using [Copier][].

[Read the docs.](https://github.com/Tecnativa/doodba#scaffolding)

<!-- toc -->

- [How to contribute](#how-to-contribute)
  - [Using Github](#using-github)
  - [Set up a development environment](#set-up-a-development-environment)
  - [Development toolkit](#development-toolkit)
- [Credits](#credits)

<!-- tocstop -->

# How to contribute

Here you will learn how to contribute to this project.

## Using Github

You should know how to use Github to contribute to this project. To learn, please follow
these tutorials:

- [Introduction to GitHub](https://lab.github.com/githubtraining/introduction-to-github)

Now that you know how to use Github, we just follow the standard process like everybody
else here: issues and pull requests.

## Set up a development environment

To hack in this project, you need to set up a development environment. To do that, first
make sure you have installed the essential dependencies:

- [curl](https://curl.haxx.se/)
- [git](https://git-scm.com/)
- [python](https://www.python.org/) 3.6+
- [invoke](https://www.pyinvoke.org/) (`python3 -m pip install --user invoke`)

Then, execute:

```bash
invoke develop
```

🎉 Your development environment is ready! Start hacking.

## Development toolkit

Once you did the steps above, it will be good for you to know that our basic building
blocks here are:

- [copier](https://github.com/pykong/copier)
- [poetry](https://python-poetry.org/)
- [pre-commit](https://pre-commit.com/)
- [pytest](https://docs.pytest.org/)

# Credits

This project is maintained by:

[![Tecnativa](https://www.tecnativa.com/r/H3p)](https://www.tecnativa.com/r/rIN)

Also, special thanks to
[our dear community contributors](https://github.com/Tecnativa/doodba-scaffolding/graphs/contributors).

[copier]: https://github.com/pykong/copier
[doodba]: https://github.com/Tecnativa/doodba
[odoo]: https://www.odoo.com/

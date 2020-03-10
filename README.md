# Compassion Odoo Docker
Based on [doodba](https://github.com/Tecnativa/doodba).

## Installation
```
git clone https://github.com/SylvainLosey/compassion-docker.git
cd compassion-docker
ln -s devel.yaml docker-compose.override.yml
chmod -R ug+rwX odoo/auto
export UID GID="$(id -g $USER)" UMASK="$(umask)"
```

Replace the remotes in `odoo/custom/src/repos.yaml` by your own forks.

```
docker-compose build --pull
docker-compose -f setup-devel.yaml run --rm odoo
docker-compose up
```

To browse Odoo go to `http://localhost:${ODOO_MAJOR}069` (i.e. for Odoo 11.0 this would be `http://localhost:11069`).


## Local development
All Compassion and OCA modules are cloned in `odoo/custom/src`

### Pycharm
1. Under File > New project choose `{compassion-docker}/odoo/custom/src/`
2. Install and configure the docker plugin (Unix socket for Linux)

### Gitcraken
Open the desired repo in `odoo/custom/src`



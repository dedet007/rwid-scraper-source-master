# rwid scraper source
Thank's for using rwid scraper source

# Table of contents
1. Get started on local
2. Get started on local (docker)
3. Deploy to heroku.

<hr>

## GET STARTED WINDOWS 10:
#### Download PostgreSQL Terbaru (Versi 13, pada Desember 2020)
Ikuti petunjuk instalasi di
https://www.postgresql.org/download/windows/

Download PgAdmin 4 di https://www.pgadmin.org/download/pgadmin-4-windows/

#### Buat VirtualEnvironment 
Ikuti video

#### Instalasi semua package yang dibutuhkan dengan `pip`
#### Jalankan server
`scripts\run.bat`

## GET STARTED LINUX:
#### create database and user on your local: 
```
CREATE DATABASE rwid_scraper_source;
CREATE DATABASE rwid_scraper_source_test;

CREATE USER amazinguser WITH password 'amazingPassword';
GRANT ALL PRIVILEGES ON database rwid_scraper_source to amazinguser;
ALTER USER amazinguser SUPERUSER;
```


#### Setup:
```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### upgrade db for init data:
```
$ source ./scripts/env_dev.sh
$ flask db upgrade
```


#### Running:
```
$ ./scripts/run.sh
```
**open localhost:5000/admin*
<hr><hr>


## GET STARTED (With Docker):
**Running:**
```sh
sudo ./scripts/docker_run_dev.sh
```
**open localhost:5000/admin*


<hr><hr>

## Deploy (Docker):
```
$ sudo ./scripts/docker_run_prod.sh
```

<hr><hr>

## Deploy (Heroku):

```sh
$ heroku login
$ heroku create app_name
$ git remote add heroku heroku_git_url
$ heroku addons:create heroku-postgresql:hobby-dev --app app_name
```

See database url with command:
```sh
$ heroku config --app app_name
```
Then Paste database URL to scripts/heroku_config.sh. Next commit your code changes and then:

```shell script
$ git push heroku master
$ ./scripts heroku_config.sh
$ heroku run flask db upgrade
```
**Open app_name.herokuapp.com/admin on your browser*






<hr><hr>

## NOTES
**How migration**:
```
$ flask db migrate
$ flask db upgrade
```

**Exec DB (docker)**
```sh
sudo ./scripts/engine-db.sh
psql -U postgres
```

**Migrate DB (docker)**
```sh
sudo ./scripts/engine.sh
flask db migrate
flask db upgrade
```

**Remote Server:**
```sh
$ sudo ./scripts/connect_server.sh
```


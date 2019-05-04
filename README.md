# Flask Robot Backend

> use flask to implement a simple API Server

## API Docs

[PostMan](https://documenter.getpostman.com/view/4303292/RzthSXR3#609b2c55-47d0-4623-bc88-411c5f35fd57)

## Dependencies

See [Pipfile](./Pipfile)

## Features

1. Auth
2. register mail, verify email address
3. forget password mail(not support modified password)
3. Data CURD
4. Params validation
5. Custom Http Exception
6. Pagination
7. [uwsgi + nginx](./docs/)

More features will coming.....

## Development

### Install the `pipenv` before run `setup.sh`

I'd like to use `pipenv`, but on `vps` or other has only limited system resource case (like your tencent cloud server, aliyun cloud server and etc.), `pipenv lock` is very slow, so you can use `pip install -r requirement` command, but make sure that you are **not** install package in `/usr/local/lib` path, it's global python library path!

**Again, Don't install dependencies in global python library path.**

```bash
chmod +x setup.sh
./setup.sh
```
### Maybe your should change to `postgres` user to create db user:
```bash
sudo -s -u postgres
psql -c "create user testusr with password 'password';"
psql -c "ALTER USER testusr WITH SUPERUSER;" 
```
**Don't use the default password**

### Set Env

#### Run server in debug mode

```bash
export FLASK_DEBUG=True
```

#### want to send your email?

```bash
export qqmailaddress="your_mail_address@foxmail.com"
export qqmailpass="your_mail_auth_code" # not the qq password.
```
### Run Server

```bash
python manage.py recreate_db
python manage.py runserver
```
### Verify server status

```bash
curl http://0.0.0.0:5000
```

## Any Questions?

welcome to [create a issue.](https://github.com/Raoul1996/flask-boilerplate/issues/new)

## Other Detail? Please See the Old README

[OLD_README](./docs/OLD_README.md)

Thanks for [tko22](https://github.com/tko22)

# 部署

> 英文水平有限，这部分是中文，部署文档目前只面向 Linux，使用 apt 进行安装

## 背景

flask 提供了 development server，但是强烈建议在生产环境中不要使用。推荐使用 uwsgi + nginx 进行部署。

## 准备

### 安装 pipenv，生成 venv 环境

```bash
sudo apt install -y python3.7 python3-dev 
sudo pip3 install pipenv  
pipenv install

```

生成的 venv 环境一般会在 `~/.local/virtualenv/` 下

## 配置

```ini
[uwsgi]

; project path
project-dir=/path_to_project
venv-dir=/path_to_python_vnev
pythonpath = /path_to_venv/lib/python3.7/site-packages/
pythonpath=/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/

master=true

chdir=%(project-dir)

venv=%(venv-dir)

; uwsgi bootstrap file
file=wsgi.py

; uwsgi will call it
callable=application

processes=4
threads=2
buffer-size=32768

no-site=true
vacuum=true

socket=%(project-dir)/uwsgi/uwsgi.sock
stats=%(project-dir)/uwsgi/uwsgi.status
pidfile=%(project-dir)/uwsgi/uwsgi.pid
daemonize=%(project-dir)/uwsgi/uwsgi.log

```

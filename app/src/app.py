#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

from v1.status.status import Status, ns_status


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app,
    title='Flask-RESTPlus API Sample',
    version='1.0',
    description='Flask-RESTPlus API Sample'
)

api.add_namespace(ns_status)


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()

#!/usr/bin/env python

from app.controller import app_server

app = app_server('config')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])

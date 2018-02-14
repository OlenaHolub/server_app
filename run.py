#!/usr/bin/env python
from app.zip_code.views import app_zip

app = app_zip('config')

if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])

## Project description

Two endpoints have been realized in the application.
1. Endpoint 'code' accepts a zip code and returns geographical coordinates
2. Endpoint 'swap' accepts a question and returns an answer for this question based on the Api.ai
3. All pairs 'question-answer' are being saved in the file named date of the request

## Installation

```
$ git clone https://github.com/OlenaHolub/server_app.git
$ $ cd server_app
$ virtualenv --python=python3 venv
$ source venv/bin/activate
$ python setup.py install
```

## Run

Before to run the application you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:
```
$ export FLASK_APP=run.py
$ flask run
```
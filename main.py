#!/usr/bin/env python3

import flask
from flask import Flask, Response, request

app = Flask()

# register routes, etc.

if __name__ == '__main__':
    app.run(debug=True, threaded=True, debug=__debug__)

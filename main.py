#!/usr/bin/env python3
" flask server. Call main.app.run(threaded=True) to run or execute on the command line. "

#import flask
from flask import Flask, Response, request

app = Flask()

# register routes, etc.

if __name__ == '__main__':
    app.run(threaded=True, debug=__debug__)

#!/usr/bin/env python3
" flask server. Call main.app.run(threaded=True) to run or execute main.py on the command line. "

#import flask
import os
from flask import Flask, Response, request

app = Flask()

def load_template(name: str='basic') -> str:
    "load a template with id `name`"
    with open(os.path.join('html-templates', name+'.template.html')) as f:
        return f.read()
def load_page(name: str) -> str:
    "load a static page, without the template surround, using id `name`"
    with open(os.path.join('html-templates', name+'.html')) as f:
        return f.read()
def format_page(name: str, title: str="Captialist Bank") -> str:
    "load and format a static page with id `name` and title `title`"
    return load_template('basic').format(title=title, content=load_page(name))

# register routes, etc.
@app.route('/')
def index():
    "return the index.html page"
    return Response(format_page('index'))

if __name__ == '__main__':
    app.run(threaded=True, debug=__debug__)

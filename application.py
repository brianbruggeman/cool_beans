#!/usr/bin/env python
'''
COOL BEANS!
Simple application developed for amazon's elastic beanstalk.

Usage:
    cool_beans [options]

Options:
    -d --debug       Run in debug mode
    -p --port PORT   Use a different port [default: 80]
    -h --host HOST   Set host ip [default: 0.0.0.0]
'''
from textwrap import dedent

from flask import Flask


app = Flask(__name__)


def hello(username='World'):
    return 'Hello, {}!'.format(username)

def htmlize(text, back=None):
    if back is not None:
        back = '<p><a href="/">Back</a></p>'
    else:
        back = textwrap.dedent('''
            <p><em>Hint</em>: This is a RESTful web service! Append a username
            to the URL (for example: <code>/Thelonious</code>) to say hello to
            someone specific.</p>'
            ''')
    html = textwrap.dedent('''
    <html>
    <head>
        <title>AWS EB Flask Test</title>
    </head>
    <body>
        <p>{}</p>
        {}
    </body>
    </html>
    '''.format(text, back))
    return html

@app.route('/')
def hello_world():
    text = hello()
    return htmlize(text)

@app.route('/<username>')
def hello_user(username):
    text = hello(username, back=True)
    return htmlize(text)


if __name__ == '__main__':
    from docopt import docopt

    args = docopt(__doc__)
    port = int(args.get('--port', 80))
    debug = args.get('--debug')
    host = args.get('--host', '0.0.0.0')

    app.run(debug=debug, port=port, host=host)
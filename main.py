#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import (Flask, request, Response,
                   render_template, redirect, abort, session)


app = Flask(__name__, static_folder='public')
app.config['SECRET_KEY'] = 'asdfasdfsdf'


@app.route('/cert', methods=['POST'])
def cert():
    session['cert_key'] = "adfasdfasdfasdfsdf"
    return render_template('signup.html', cert_key=session['cert_key'])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('before_signup.html')
    else:
        cert_key = request.form.get('cert_key')
        if cert_key == session['cert_key']:
            return "Hello hoàng đập trai :D"
        else:
            return "DKM mày là bot cmnr :D"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

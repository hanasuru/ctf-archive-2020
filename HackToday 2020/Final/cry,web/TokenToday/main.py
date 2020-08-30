#!/usr/bin/python
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    url_for
)
import auth

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        try:
            assert(len(username) >= 2 and len(username) <= 40)
            assert(len(password) >= 2 and len(password) <= 40)
            token = auth.generate_token(username, password)
            response = make_response(render_template('index.html', data=auth.validate_token(token)))
            response.set_cookie('token', token)
            return response
        except:
            return 'invalid username and/or password'
    else:
        token = request.cookies.get('token')
        if token:
            return render_template('index.html', data=auth.validate_token(token))
        else:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)

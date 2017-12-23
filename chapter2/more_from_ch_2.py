from flask import Flask
app = Flask(__name__)

from flask import request
from flask import make_response
from flask import redirect

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/cookie')
def coookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/espn')
def goToEspn():
    return redirect('http://www.espn.com/')

from flask import abort

@app.route('/user/<id>')
def get_user(id):
    user = id == 'Matt'
    if not user:
        abort(404)
    return '<h1>Hello, %s!</h1>' % id
if __name__ == '__main__':
    app.run(debug=True)




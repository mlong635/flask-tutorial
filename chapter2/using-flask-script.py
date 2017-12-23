from flask import Flask
app = Flask(__name__)

# from flask.ext.script import Manager # gives error --> ExtDeprecationWarning: Importing flask.ext.script is deprecated, use flask_script instead.
from flask_script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()


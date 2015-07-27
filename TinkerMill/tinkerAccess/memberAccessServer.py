#!/usr/bin/python
#
#
#  This file may be deprecated!!!
#  TODO:  check with Matt P's simpleServer applications!!!
#
# The blow code is a very basic implementation of the flask
# module.  TODO:  verify which server side implementation will
# be used.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	
	return 'Andrew J Steffen'


if __name__== '__main__':
	app.run(host='0.0.0.0')

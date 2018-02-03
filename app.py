from flask import Flask
from flask import render_template, request, url_for, redirect, session

from flask_sqlalchemy import SQLAlchemy 
from flask.json import jsonify

from functions import *

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shydeee:1234qwer@localhost/flask101_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'not_so_secret_key'

import models

app.debug=True


@app.route('/')
def index():
	myUsers = models.User.query.all()
	return render_template('index.html', myUsers = myUsers)

@app.route('/signIn')
def signIn():
	return render_template('signin.html')


@app.route('/signUp')
def signUp():
	return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
	error = None
	name = request.form['inputName']
	email = request.form['inputEmail']
	password = request.form['inputPassword']

	newUser = models.User(name,email,password)
	if(checkExisting(email)==False):
		db.session.add(newUser)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		return ("This email is in use")
	
	
@app.route('/login', methods=['POST'])
def login():
	email = request.form['inputEmail']
	password = request.form['inputPassword']


	if(validate(email,password)==True):
		redirect(url_for('dashboard'))
		return "login particulars correct"
	else:
		return 'login fail'


@app.route('/dashboard')
def dashboard():
	myPosts = models.Post.query.filter_by('user')


if __name__ == '__main__':
	db.create_all()
	app.run()

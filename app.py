from flask import Flask
from flask import render_template, request, url_for, redirect, session

from flask_sqlalchemy import SQLAlchemy 
from flask.json import jsonify
from flask_heroku import Heroku




import os


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shydeee:1234qwer@localhost/flask101_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)
app.secret_key = 'not_so_secret_key'

from functions import *
import models

app.debug=True


@app.route('/')
def index():
	myUsers = models.User.query.all()
	return render_template('index.html', myUsers = myUsers)

@app.route('/signIn')
def signIn():
	return render_template('signIn.html')


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
		signUp()
	
	
@app.route('/login', methods=['POST'])
def login():
	email = request.form['inputEmail']
	password = request.form['inputPassword']


	if(validate(email,password)==True):
		return redirect(url_for('dashboard'))
		#return "login particulars correct"
	else:
		return redirect(url_for('signIn'))


@app.route('/dashboard')
def dashboard():
	myPosts = findPosts(session['id'])

	return render_template('dashboard.html', posts = myPosts, username = session['name'])

@app.route('/post', methods=['POST'])
def post():
	message = request.form['post']
	postMessage(session['id'],message)
	return redirect(url_for('dashboard'))

@app.route('/clearAll')
def clearAll():
	clearAllPosts(session['id'])
	return redirect(url_for('dashboard'))



if __name__ == '__main__':
	db.create_all()
	app.run(host='0.0.0.0')

from app import db
from flask import session
import models

def checkExisting(email):
	existing = models.User.query.filter_by(email=email).first()
	if existing!=None:
		return True
	else:
		return False

def validate(email,password):
	print(email,password)
	user = models.User.query.filter_by(email=email, password_hash=password).first()
	print("user: {}".format(user))
	if user==None:
		return False
	else:
		session['id'] = user.id
		session['name'] = user.name
		print(session['id'])
		return True

def findPosts(id):
	print(id)
	myPosts = models.Post.query.filter_by(user_id = id).all()
	print(myPosts)
	return myPosts
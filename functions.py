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
	if user==None:
		return False
	else:
		session['user_id'] = user.id
		print(session['user_id'])
		return True
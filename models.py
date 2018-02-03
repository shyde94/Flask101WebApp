from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64),index=True)
	email=db.Column(db.String(120), index=True, unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	posts = relationship('Post')

	def __init__(self, name, email, password_hash):
		self.name = name
		self.email = email
		self.password_hash = password_hash

	def __repr__(self):
		return '<User {}>'.format(self.name)


class Post(db.Model):
	__tablename__ = 'post'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	message = db.Column(db.String(500),index=True)
	user = relationship("User", foreign_keys= (user_id))

	def __init__(self, message):
		self.message = message

	def __repr__(self):
		return '<user_id {}>'.format(self.user_id)


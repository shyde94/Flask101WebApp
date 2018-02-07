# Flask101WebApp

A simple flask app to practice basic web dev, using SQLAlchemy on Postgresql, how to connect the flask app to Postgresql, 
setting routes, hence the name. 

What the app does?
Signups, logins, posting of messages. 




----------------------------------------------------------------------------------------------------------------------------

Basic notes to myself.

Flask app with postgresql deployed on heroku:

Python libraries required, along with their required libraries:
- flask - Flask, request, redirect, url_for, session
- flask_sqlalchemy
- flask_heroku

Specific files to have:
an app.py file, thats where you define your routes and call app.run(). ROUTES -> what to do for each link. 

Postgresql: - this is the database server, within it you need to set up the database, and create the tables defined in your models.py

For localhost:
the SQLALCHEMY_DATABASE_URI key should be 
'postgresql://user:password@localhost/database_name’ 

otherwise for deployment on heroku, make sure to uncomment this.

Deployment on heroku:
Get the heroku client at https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Commands into terminal:
heroku create - heroku creates an app with a random name, important part here is a remote repository is set up for you to push source code up into this repo. Servers will use whatever code in this repo to run your app. 
Rest of the steps in the link above is pretty easy to follow.

Conda environment was used here...

Important thing to note, some special files to include : 
- Procfile: not sure what this does yet (KIV)

- requirements.txt and environment.yml files, im not sure if you need both or one will just suffice. Kiv.

- runtime.txt, heroku runs on python 3.6 by default..so if your python dependency is set at 2.7, need to declare in this file. just write 'python-2.7.14’ in runtime.txt



Postgresql database needs to be set up on heroku as an add on as well. Follow tutorial at these links:

- https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python

and 

- http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/ 
some code for this link above is a bit outdated, but the general concept is still correct. The important part is to run python shell on the server to call db.create_all() so that the tables are created for whatever data needed to be stored. 

command to run python on heroku: heroku run python 



DISCLAIMER: This readme's kind of for my own learning, I'm pretty sure I got some stuff incorrect. This app was just something for me to go through the process of creating a simple app and deploying it. 

 - heroku app link : https://limitless-peak-12699.herokuapp.com/

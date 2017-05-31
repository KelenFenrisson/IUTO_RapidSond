import os.path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_restless import APIManager
from flask_bootstrap import Bootstrap

#########################  HELPER FUNCTIONS
def mkpath(p):
	return os.path.normpath(
		os.path.join(
			os.path.dirname(__file__),
			p))
###########################################




app = Flask(__name__)
Bootstrap(app)

app.config['DEBUG']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../sondages/quest.db'))



db=SQLAlchemy(app)

# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
api_manager = APIManager(app, flask_sqlalchemy_db=db)

manager = Manager(app)






#! /usr/bin/python3
from app import manager, api_manager
from models import Question, Sondage, User, SimpleQuestion
from commands import loaddb
# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
api_manager.create_api(Question, methods=['GET', 'POST', 'DELETE'])
api_manager.create_api(Sondage, methods=['GET'])

if __name__ == '__main__':

	manager.run()

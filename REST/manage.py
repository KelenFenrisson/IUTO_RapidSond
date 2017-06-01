#! /usr/bin/env python3
from sondages.application import *
from sondages.models import *
# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
api_manager.create_api(Utilisateur, methods=['GET'])
api_manager.create_api(Questionnaire, methods=['GET'])
api_manager.create_api(Client, methods=['GET'])
api_manager.create_api(Sonde, methods=['GET'])


if __name__ == '__main__':

	manager.run()

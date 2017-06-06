#! /usr/bin/env python3
from sondages.application import *
from sondages.models import *
from sondages.api import *
# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
# api_manager.create_api(Utilisateur, methods=['GET', 'POST'])
# api_manager.create_api(Questionnaire, methods=['GET', 'POST'])
# api_manager.create_api(Client, methods=['GET', 'POST'])
# api_manager.create_api(Sonde, methods=['GET', 'POST'])
# api_manager.create_api(Question, methods=['GET', 'POST'])


if __name__ == '__main__':

	manager.run()

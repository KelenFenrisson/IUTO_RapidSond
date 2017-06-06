################################### DESCRIPTION ET PARAMETRAGE DES API
from sondages.application import api_manager
from sondages.models import *



####### API UTILISATEUR


def pre_get_single_Utilisateur(**kw):
    print("PRE_GET_SINGLE_UTILISATEUR")


def pre_get_many_Utilisateur(**kw):
    print("PRE_GET_MANY_UTILISATEUR")


api_manager.create_api(Utilisateur, methods=['GET'], preprocessors={'GET_SINGLE':[pre_get_single_Utilisateur],
                                                                    'GET_MANY':[pre_get_many_Utilisateur]})


###### API QUESTIONNAIRE
def pre_get_single_Questionnaire(instance_id=None,**kw):
    print("PRE_GET_SINGLE_QUESTIONNAIRE")

def pre_get_many_Questionnaire(result=None, **kw):
    print("PRE_GET_MANY_QUESTIONNAIRE")

def post_get_single_Questionnaire(instance_id=None, result=None, **kw):
    print("POST_GET_SINGLE_QUESTIONNAIRE")
    result['client']= api_manager.url_for(Client, instid=result['id_client']);
    result['concepteur']= api_manager.url_for(Utilisateur, instid=result['id_concepteur'])
    result['panel']= api_manager.url_for(Panel, instid=result['id_panel'])


def post_get_many_Questionnaire(result=None, **kw):
    print("POST_GET_MANY_QUESTIONNAIRE")
    for item in result['objects']:
        item['client']= api_manager.url_for(Client, instid=item['id_client']);
        item['concepteur']= api_manager.url_for(Utilisateur, instid=item['id_concepteur'])
        item['panel']= api_manager.url_for(Panel, instid=item['id_panel'])



api_manager.create_api(Questionnaire,
                       methods=['GET'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Questionnaire],
                                      'GET_MANY':[pre_get_many_Questionnaire]},
                       postprocessors={'GET_SINGLE': [post_get_single_Questionnaire],
                                      'GET_MANY': [post_get_many_Questionnaire]}
                       )




###### API CLIENT
def pre_get_single_Client(**kw):
    print("PRE_GET_SINGLE_CLIENT")

def pre_get_many_Client(**kw):
    print("PRE_GET_MANY_CLIENT")

api_manager.create_api(Client, methods=['GET'], preprocessors={'GET_SINGLE':[pre_get_single_Client],
                                                                'GET_MANY':[pre_get_many_Client]})

###### API SONDE
def pre_get_single_Sonde(**kw):
    print("PRE_GET_SINGLE_SONDE")

def pre_get_many_Sonde(**kw):
    print("PRE_GET_MANY_SONDE")


api_manager.create_api(Sonde, methods=['GET'], preprocessors={'GET_SINGLE':[pre_get_single_Sonde],
                                                              'GET_MANY':[pre_get_many_Sonde]})



###### API QUESTION
def pre_get_single_Question(**kw):
    print("PRE_GET_SINGLE_QUESTION")

def pre_get_many_Question(**kw):
    print("PRE_GET_MANY_QUESTION")


api_manager.create_api(Question, methods=['GET'], preprocessors={'GET_SINGLE':[pre_get_single_Question],
                                                                 'GET_MANY':[pre_get_many_Question]})


###### API PANEL
def pre_get_single_Panel(**kw):
    print("PRE_GET_SINGLE_QUESTION")

def pre_get_many_Panel(**kw):
    print("PRE_GET_MANY_QUESTION")


api_manager.create_api(Panel, methods=['GET'], preprocessors={'GET_SINGLE':[pre_get_single_Panel],
                                                                 'GET_MANY':[pre_get_many_Panel]})
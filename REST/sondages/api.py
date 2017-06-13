################################### DESCRIPTION ET PARAMETRAGE DES API
from sondages.application import api_manager, app
from sondages.models import *



####### API UTILISATEUR


def pre_get_single_Utilisateur(**kw):
    print("PRE_GET_SINGLE_UTILISATEUR")

def pre_get_many_Utilisateur(**kw):
    print("PRE_GET_MANY_UTILISATEUR")

def post_get_single_Utilisateur(**kw):
    print("PRE_GET_SINGLE_UTILISATEUR")

def post_get_many_Utilisateur(**kw):
    print("PRE_GET_MANY_UTILISATEUR")

api_manager.create_api(Utilisateur, methods=['GET', 'POST'], preprocessors={'GET_SINGLE':[pre_get_single_Utilisateur],
                                                                    'GET_MANY':[pre_get_many_Utilisateur]})


###### API QUESTIONNAIRE
def pre_get_single_Questionnaire(instance_id=None, search_params=None, data=None,**kw):
    print("PRE_GET_SINGLE_QUESTIONNAIRE")
    print(search_params)

def pre_get_many_Questionnaire(instance_id=None, search_params=None, data=None,**kw):
    print("PRE_GET_MANY_QUESTIONNAIRE")
    print(search_params)


def post_get_single_Questionnaire(instance_id=None, result=None, **kw):
    print("POST_GET_SINGLE_QUESTIONNAIRE")
    result['client']= api_manager.url_for(Client, instid=result['id_client'])
    result['concepteur']= api_manager.url_for(Utilisateur, instid=result['id_concepteur'])
    result['panel']= api_manager.url_for(Panel, instid=result['id_panel'])
    result['testquestions'] = [ api_manager.url_for(Question)+"?q={\"filters\":[{\"id\":"+str(q['id'])+", \"numero\":"+str(q['numero'])+"}], \"single\":true}" for q in result['questions']]
    result['questions'] = [ api_manager.url_for(Question, instid=q['id']) for q in result['questions']]


def post_get_many_Questionnaire(result=None, **kw):
    print("POST_GET_MANY_QUESTIONNAIRE")
    for item in result['objects']:
        item['client']= api_manager.url_for(Client, instid=item['id_client'])
        item['concepteur']= api_manager.url_for(Utilisateur, instid=item['id_concepteur'])
        item['panel']= api_manager.url_for(Panel, instid=item['id_panel'])

api_manager.create_api(Questionnaire,
                       methods=['GET', 'POST', 'PATCH'],
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

def post_get_single_Client(result=None,**kw):
    print("POST_GET_SINGLE_CLIENT")

def post_get_many_Client(result=None,**kw):
    print("POST_GET_MANY_CLIENT")

api_manager.create_api(Client, methods=['GET', 'POST'], preprocessors={'GET_SINGLE':[pre_get_single_Client],
                                                                'GET_MANY':[pre_get_many_Client]})

###### API SONDE
def pre_get_single_Sonde(**kw):
    print("PRE_GET_SINGLE_SONDE")

def pre_get_many_Sonde(**kw):
    print("PRE_GET_MANY_SONDE")

def post_get_single_Sonde(result=None,**kw):
    print("POST_GET_SINGLE_SONDE")
    result['panels']=[api_manager.url_for(Panel, instid=p['id_panel']) for p in result['panels']]

def post_get_many_Sonde(result=None,**kw):
    print("POST_GET_MANY_SONDE")
    for item in result['objects']:
        item['panels'] = [api_manager.url_for(Panel, instid=p['id_panel']) for p in item['panels']]


api_manager.create_api(Sonde,
                       methods=['GET', 'PATCH'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Sonde], 'GET_MANY':[pre_get_many_Sonde]},
                       postprocessors={'GET_SINGLE':[post_get_single_Sonde], 'GET_MANY':[post_get_many_Sonde]})



###### API QUESTION

def pre_get_single_Question(instance_id=None, search_params=None, data=None,**kw):
    print("PRE_GET_SINGLE_QUESTION")
    print(search_params)

def pre_get_many_Question(instance_id=None, search_params=None, data=None,**kw):
    print("PRE_GET_MANY_QUESTION")
    print(search_params)


def post_get_single_Question(instance_id=None, search_params=None, result=None, **kw):
    print("POST_GET_SINGLE_QUESTION")
    result['questionnaire']=[api_manager.url_for(Questionnaire, instid=q['id']) for q in result['questionnaire']]

def post_get_many_Question(instance_id=None, search_params=None, result=None, **kw):
    print("POST_GET_MANY_QUESTION")
    for item in result['objects']:
        if item['id']==int(search_params['id']) and item['numero']==int(search_params['numero']):
            item['questionnaire'] = [api_manager.url_for(Questionnaire, instid=q['id']) for q in item['questionnaire']]


api_manager.create_api(Question,
                       methods=['GET', 'POST', 'PATCH', 'DELETE'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Question],
                                      'GET_MANY':[pre_get_many_Question]},
                       postprocessors={'GET_SINGLE':[post_get_single_Question],
                                      'GET_MANY':[post_get_many_Question]}
                       )


###### API PANEL
def pre_get_single_Panel(**kw):
    print("PRE_GET_SINGLE_QUESTION")

def pre_get_many_Panel(**kw):
    print("PRE_GET_MANY_QUESTION")

def post_get_single_Panel(result=None, **kw):
    print("POST_GET_SINGLE_QUESTION")
    result['sondes']=[api_manager.url_for(Sonde, instid=p['id_sonde']) for p in result['sondes']]


def post_get_many_Panel(result=None, **kw):
    print("POST_GET_MANY_QUESTION")
    for item in result['objects']:
        item['sondes'] = [api_manager.url_for(Sonde, instid=p['id_sonde']) for p in item['sondes']]


api_manager.create_api(Panel,
                       methods=['GET'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Panel],'GET_MANY':[pre_get_many_Panel]},
                       postprocessors={'GET_SINGLE':[post_get_single_Panel],'GET_MANY':[post_get_many_Panel]},
                       )

api_manager.create_api(ValeurPossible, methods=['GET'])
api_manager.create_api(Interroger, methods=['GET'])
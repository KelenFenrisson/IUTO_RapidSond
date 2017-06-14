################################### DESCRIPTION ET PARAMETRAGE DES API
from sondages.application import api_manager, app
from sondages.models import *
from flask_cors import CORS
import json


app.config['API_LIST']={}
####### API UTILISATEUR


def pre_get_single_Utilisateur(**kw):
    pass

def pre_get_many_Utilisateur(**kw):
    pass

def post_get_single_Utilisateur(**kw):
    pass

def post_get_many_Utilisateur(**kw):
    pass

app.config['API_LIST']['Utilisateur']=api_manager.create_api(Utilisateur, methods=['GET', 'POST', 'PATCH'], preprocessors={'GET_SINGLE':[pre_get_single_Utilisateur],
                                                                    'GET_MANY':[pre_get_many_Utilisateur]})


###### API QUESTIONNAIRE
def pre_get_single_Questionnaire(instance_id=None, search_params=None, data=None,**kw):
    pass

def pre_get_many_Questionnaire(instance_id=None, search_params=None, data=None,**kw):
    pass


def post_get_single_Questionnaire(instance_id=None, result=None, **kw):
    # print("POST_GET_SINGLE_QUESTIONNAIRE")
    result['client']= api_manager.url_for(Client, instid=result['id_client'])
    result['concepteur']= api_manager.url_for(Utilisateur, instid=result['id_concepteur'])
    result['panel']= api_manager.url_for(Panel, instid=result['id_panel'])

    l_questlink = [ api_manager.url_for(Question, q=json.dumps({"filters":[{"and":[{"name":"id","op":"==","val":quest['id']},{"name":"numero","op":"eq","val":quest['numero']}]}]})) for quest in result['questions']]
    result['questions'] = l_questlink

def post_get_many_Questionnaire(result=None, **kw):
    for item in result['objects']:
        item['client']= api_manager.url_for(Client, instid=item['id_client'])
        item['concepteur']= api_manager.url_for(Utilisateur, instid=item['id_concepteur'])
        item['panel']= api_manager.url_for(Panel, instid=item['id_panel'])
        l_questlink = [api_manager.url_for(Question, q=json.dumps({"filters": [{"and": [
            {"name": "id", "op": "==", "val": quest['id']}, {"name": "numero", "op": "eq", "val": quest['numero']}]}]}))
                       for quest in item['questions']]
        item['questions'] = l_questlink

app.config['API_LIST']['Questionnaire']=api_manager.create_api(Questionnaire,
                       methods=['GET', 'POST', 'PATCH','DELETE'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Questionnaire],
                                      'GET_MANY':[pre_get_many_Questionnaire]},
                       postprocessors={'GET_SINGLE': [post_get_single_Questionnaire],
                                      'GET_MANY': [post_get_many_Questionnaire]}
                       )




###### API CLIENT
def pre_get_single_Client(**kw):
    pass

def pre_get_many_Client(**kw):
    pass

def post_get_single_Client(result=None,**kw):
    pass

def post_get_many_Client(result=None,**kw):
    pass

app.config['API_LIST']['Client']=api_manager.create_api(Client, methods=['GET', 'POST', 'PATCH'], preprocessors={'GET_SINGLE':[pre_get_single_Client],
                                                                'GET_MANY':[pre_get_many_Client]})

###### API SONDE
def pre_get_single_Sonde(**kw):
    pass

def pre_get_many_Sonde(**kw):
    pass

def post_get_single_Sonde(result=None,**kw):
    # print("POST_GET_SINGLE_SONDE")
    result['panels']=[api_manager.url_for(Panel, instid=p['id_panel']) for p in result['panels']]

def post_get_many_Sonde(result=None,**kw):
    # print("POST_GET_MANY_SONDE")
    for item in result['objects']:
        item['panels'] = [api_manager.url_for(Panel, instid=p['id_panel']) for p in item['panels']]


app.config['API_LIST']['Sonde']=api_manager.create_api(Sonde,
                       methods=['GET', 'PATCH', 'POST'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Sonde], 'GET_MANY':[pre_get_many_Sonde]},
                       postprocessors={'GET_SINGLE':[post_get_single_Sonde], 'GET_MANY':[post_get_many_Sonde]})



###### API QUESTION

def pre_get_single_Question(instance_id=None, search_params=None, data=None,**kw):
    # print("PRE_GET_SINGLE_QUESTION")
    pass

def pre_get_many_Question(instance_id=None, search_params=None, data=None,**kw):
    # print("PRE_GET_MANY_QUESTION")
    pass


def post_get_single_Question(instance_id=None, search_params=None, result=None, **kw):
    # print("POST_GET_SINGLE_QUESTION")
    # print("POST_GET", search_params)
    result['questionnaire']=[api_manager.url_for(Questionnaire, instid=q['id']) for q in result['questionnaire']]
    result['reponses'] = [api_manager.url_for(ValeurPossible, q=json.dumps({"filters": [{"and": [
        {"name": "question_id", "op": "==", "val": rep['question_id']},
        {"name": "question_num", "op": "eq", "val": rep['question_num']}, {"name": "id", "op": "eq", "val": rep['id']}]}]}))
                        for rep in result['reponses']]

def post_get_many_Question(instance_id=None, search_params=None, result=None, **kw):
    # print("POST_GET_MANY_QUESTION")
    # print("POST_GET", search_params)
    for item in result['objects']:
        item['questionnaire'] = [api_manager.url_for(Questionnaire, instid=q['id']) for q in item['questionnaire']]
        item['reponses'] = [api_manager.url_for(ValeurPossible, q=json.dumps({"filters": [{"and": [{"name": "question_id", "op": "==", "val": rep['question_id']}, {"name": "question_num", "op": "eq", "val": rep['question_num']},{"name": "id", "op": "eq", "val": rep['id']}]}]}))
                       for rep in item['reponses']]

app.config['API_LIST']['Question']=api_manager.create_api(Question,
                       methods=['GET', 'POST', 'PATCH', 'DELETE'],
                       primary_key='numero',
                       preprocessors={'GET_SINGLE':[pre_get_single_Question],
                                      'GET_MANY':[pre_get_many_Question]},
                       postprocessors={'GET_SINGLE':[post_get_single_Question],
                                      'GET_MANY':[post_get_many_Question]}
                       )


###### API PANEL
def pre_get_single_Panel(**kw):
    # print("PRE_GET_SINGLE_QUESTION")
    pass

def pre_get_many_Panel(**kw):
    # print("PRE_GET_MANY_QUESTION")
    pass

def post_get_single_Panel(result=None, **kw):
    # print("POST_GET_SINGLE_QUESTION")
    result['sondes']=[api_manager.url_for(Sonde, instid=p['id_sonde']) for p in result['sondes']]


def post_get_many_Panel(result=None, **kw):
    print("POST_GET_MANY_QUESTION")
    for item in result['objects']:
        item['sondes'] = [api_manager.url_for(Sonde, instid=p['id_sonde']) for p in item['sondes']]


app.config['API_LIST']['Panel']=api_manager.create_api(Panel,
                       methods=['GET', 'POST'],
                       preprocessors={'GET_SINGLE':[pre_get_single_Panel],'GET_MANY':[pre_get_many_Panel]},
                       postprocessors={'GET_SINGLE':[post_get_single_Panel],'GET_MANY':[post_get_many_Panel]},
                       )

app.config['API_LIST']['ValeurPossible']=api_manager.create_api(ValeurPossible, methods=['GET','POST','PATCH'], exclude_columns=['question'])
app.config['API_LIST']['Interroger']=api_manager.create_api(Interroger, methods=['GET','POST','PATCH'])
app.config['API_LIST']['Constituer']=api_manager.create_api(Constituer, methods=['GET','POST','PATCH'])
CORS(app)
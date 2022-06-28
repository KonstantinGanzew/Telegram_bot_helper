import requests
import config


# Аутенфицирует сотрудников
def authentications(TEL_ID):
    return requests.get(config.URL_FOR_AUTH + str(TEL_ID)).json()['status'] == 'ok'


# Создает процесс в ерпе и возращает его в ответе бота
def create_process(message_text):
    param = {
        'action': 'processCreate',
        'typeId': 10470,
        'description': message_text,
        'responseType': 'json',
    }
    URL = config.URL_CREATE_ERP
    response = requests.get(URL, params=param)
    id_process = response.json()['data']['process']['id']
    param = {
    'id': id_process,
    'action': 'processGroupsUpdate',
    'groupRole': '533:0',
    'responseType': 'json',
    }
    response = requests.get(URL, params=param)
    return id_process

import requests
import config

# Список для экранирования запросов
LIST_IJECTOR = ['SELECT', 'CREATE', 'DATABASE', 'USE', 'TABLES', 'SOURCE', 'DESCRIBE', 'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'WHERE', 'PRIMARY', 'FOREIGN ',
                'KEY', 'REFERENCES', 'DROP', 'SHOW', 'FROM', 'OPENQUERY', 'INNER', 'JOIN', 'VIEW', 'ORDER', 'BETWEEN', 'LIKE', 'BY', 'IN', 'AND', 'link', 'param_text', 'DELETE',
                'GROUP', 'DECLARE', 'REPLACE', 'DISTINCT', 'HAVING', 'COUNT', 'TABLE', '\0', '\'', '\"', '\b', '\n', '\r', '\t', '\Z', '\\', '\%', '\_', '<', '>', '\<', '\>']

# Аутенфицирует сотрудников
def authentications(TEL_ID):
    return requests.get(config.URL_FOR_AUTH + str(TEL_ID)).json()['status'] == 'ok'


# Создает процесс в ерпе и возращает его в ответе бота
def create_process(message, dog_ul):
    message_text = message[3]
    for item in LIST_IJECTOR:
        message_text = message_text.replace(item, '')
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
    if dog_ul != '':
        param = {
            'processId': id_process,
            'billingId': 'rb',
            'action': 'addProcessContractLink',
            'contractTitle': dog_ul,
            'responseType': 'json',
        }
        response = requests.post(config.URL_ADD_CONTRACT, params=param)
    return id_process

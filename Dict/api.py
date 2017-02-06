import requests
from conf import dictionary

data = {}


def add_word(word, meaning, tr=''):
    data['name'] = word
    data['translation'] = meaning
    data['transcription'] = '[ ' + tr + ' ]'

    ans = requests.post(dictionary.apiWordlist, json=data,
                        auth=requests.auth.HTTPBasicAuth(dictionary.login, dictionary.pswd))
    if ans.status_code == 201:
        # print('Success.')
        return True
    else:
        print('An error was occurred.')
        return False
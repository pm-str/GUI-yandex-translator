import requests
from conf import dictionary


def add_word(word, meaning, tr=''):
    data = dict()
    data['name'] = word
    data['translation'] = meaning
    if tr.strip() not in ['-', '', None]:
        data['transcription'] = '[ ' + tr + ' ]'
    ans = requests.post(dictionary.apiWordlist, json=data,
                        auth=requests.auth.HTTPBasicAuth(dictionary.login, dictionary.pswd))
    if ans.status_code == 201:
        # print('Success.')
        return True
    else:
        print('An error was occurred.')
        return False

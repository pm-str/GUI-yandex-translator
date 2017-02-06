import requests

from conf.yandexAPI import DoTr


def trans_request(lang, text):
    body = DoTr.format(lang=lang, text='+'.join(text.split()))
    ans = {}
    r = requests.post(body)
    if r.status_code == 200 and r.json().get('code') == 200:
        ans['ans'] = r.json().get('text', [])
    else:
        print(r.json())
        ans['error'] = 'An error was occurred.'
    return ans

'''{
    "text":["привет мой друг"]
}'''

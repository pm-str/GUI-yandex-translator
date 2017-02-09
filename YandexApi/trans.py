import requests

from conf.APIconf import DoTr


def trans_request(lang, text):
    body = DoTr.format(lang=lang, text='+'.join(text.split()))
    ans = {}
    try:
        r = requests.post(body)
    except (requests.ConnectionError,) as r:
        ans['error'] = 'Translator: Check your internet connections.'
    else:
        if r.status_code == 200 and r.json().get('code') == 200:
            ans['ans'] = r.json().get('text', [])
        else:
            ans['error'] = r.json().get('message', '') or 'Translator: An error was occurred.'
    return ans

'''{
    "text":["привет мой друг"]
}'''

import requests

from conf.yandexAPI import DictLookup


def dict_request(lang, text):
    body = DictLookup.format(lang=lang, text='+'.join(text.split()))
    ans = {}

    r = requests.post(body)
    if r.status_code == 200:
        ans['ans'] = r.json().get('def')
    else:
        ans['error'] = 'An error was occurred.'
    return ans


'''ans = {"def": [
    {
        "text": "hello", "pos": "noun", "ts": "ˈheˈləʊ", "tr": [{"text": "привет", "pos": "noun"}]
     },
    {
        "text": "hello", "pos": "verb", "ts": "ˈheˈləʊ", "tr": [{"text": "поздороваться", "pos": "verb"}]
    }
]}'''
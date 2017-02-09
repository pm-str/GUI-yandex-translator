import requests

from conf.APIconf import DictLookup


def dict_request(lang, text):
    body = DictLookup.format(lang=lang, text='+'.join(text.split()))
    ans = {}

    try:
        r = requests.post(body)
    except (requests.ConnectionError,) as r:
        ans['error'] = 'Dictionary: Check your internet connections.'
    else:
        if r.status_code == 200:
            ans['ans'] = r.json().get('def')
        else:
            ans['error'] = 'Dictionary: An error was occurred.'
    return ans


'''ans = {"def": [
    {
        "text": "hello", "pos": "noun", "ts": "ˈheˈləʊ", "tr": [{"text": "привет", "pos": "noun"}]
     },
    {
        "text": "hello", "pos": "verb", "ts": "ˈheˈləʊ", "tr": [{"text": "поздороваться", "pos": "verb"}]
    }
]}'''
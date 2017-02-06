from PyQt5 import QtGui
from PyQt5.QtWidgets import QListWidgetItem


def output(trans, dict):
    data = []
    w_tr_tl = {}

    # print(dict)
    if 'error' in trans:
        print(dict['error'])
    else:
        text = trans['ans'][0]
        item = QListWidgetItem()
        item.setText(text)
        item.setBackground(QtGui.QBrush(QtGui.QColor(70, 231, 223)))
        data.append(item)

    if 'error' in dict:
        print(dict['error'])
    else:
        dict = dict.get('ans', [])
        for i in dict:
            item = QListWidgetItem()
            item.setText('\n' + i.get('ts', ' - ') + ' / ' + i.get('pos', ' - '))
            data.append(item)
            for j in i.get('tr', []):
                item = QListWidgetItem()
                item.setText(j.get('text', ''))
                item.setBackground(QtGui.QBrush(QtGui.QColor(167, 238, 143)))
                data.append(item)
    return data


'''ans = {"def": [
    {
        "text": "hello", "pos": "noun", "ts": "ˈheˈləʊ", "tr": [{"text": "привет", "pos": "noun"}]
     },
    {
        "text": "hello", "pos": "verb", "ts": "ˈheˈləʊ", "tr": [{"text": "поздороваться", "pos": "verb"}]
    }
]}'''
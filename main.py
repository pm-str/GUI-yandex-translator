#!/usr/bin/python3
import sys
from time import sleep

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from Dict.api import add_word
from Views import mainWindow
from YandexApi import formaters
from YandexApi.dict import dict_request
from YandexApi.trans import trans_request
from conf import yandexAPI


class UpdateTr(QtCore.QThread):

    changed = QtCore.pyqtSignal(object)
    stop = False

    def __init__(self, lang, text):
        QtCore.QThread.__init__(self)
        self.lang = lang
        self.text = text

    def run(self):
        sleep(yandexAPI.update_time)
        if not self.stop:
            ans = trans_request(self.lang, self.text), dict_request(self.lang, self.text)
            self.changed.emit(ans)


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(QMainWindow, self).__init__(*args)

        self.ui = mainWindow.Ui_Form()
        self.ui.setupUi(self)

        self.langs_from = sorted(yandexAPI.langs.keys())
        self.langs_to = self.langs_from.copy()

        self.langs_from.remove('английский')
        self.langs_from.insert(0, 'английский')
        self.ui.lang_from.addItems(self.langs_from)

        self.langs_to.remove('русский')
        self.langs_to.insert(0, 'русский')
        self.ui.lang_to.addItems(self.langs_to)

    def swap_langs(self):
        self.langs_from, self.langs_to = self.langs_to, self.langs_from
        self.ui.lang_from.clear()
        self.ui.lang_to.clear()
        self.ui.lang_from.addItems(self.langs_from)
        self.ui.lang_to.addItems(self.langs_to)

    def update_ready(self, param):
        self.ui.translation.clear()
        data = formaters.output(*param)
        for i in data:
            self.ui.translation.addItem(i)

    threads = []

    def ready(self):

        lang = yandexAPI.langs[self.ui.lang_from.currentText()] + '-' + yandexAPI.langs[self.ui.lang_to.currentText()]
        text = self.ui.text.toPlainText()

        if text.strip():
            cur_threads = []
            for i in self.threads:
                i.stop = True
                if not i.isFinished():
                    cur_threads.append(i)
            self.threads = cur_threads

            update = UpdateTr(lang, text)
            update.changed.connect(self.update_ready)
            self.threads.append(update)
            update.start()
        else:
            self.ui.translation.clear()

    def add_by_api(self, opt):
        ind = opt.row()
        word = self.ui.text.toPlainText()
        ts = self.ui.translation.item(ind).text()
        tl = ''

        if ' / ' not in ts:
            for i in range(ind, -1, -1):
                k = self.ui.translation.item(i).text()
                if ' / ' in k:
                    tl = k.split(' / ')[0].strip()
            res = add_word(word, ts, tl)
            if res:
                self.ui.translation.item(ind).setBackground(QtGui.QBrush(QtGui.QColor(255, 234, 2)))


# -----------------------------------------------------#
app = QApplication(sys.argv)
app.setApplicationName('GUI')

form = MainWindow()
form.setWindowTitle('Translator')
form.show()

sys.exit(app.exec_())
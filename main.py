#!/usr/bin/python3
import sys
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Dict.api import add_word
from Views import mainWindow
from YandexApi import formaters
from YandexApi.dict import dict_request
from YandexApi.trans import trans_request
from multiprocessing import Process
from conf import APIconf
import urllib
import pygame
import os


class Options(QtCore.QThread):
    changed = QtCore.pyqtSignal(object)
    stop = False

    def __init__(self, lang, text, option):
        QtCore.QThread.__init__(self)
        self.lang = lang
        self.text = text
        self.option = option

    def run(self):
        if self.option == 'transl':
            sleep(APIconf.update_time)
            if not self.stop:
                ans = trans_request(self.lang, self.text), dict_request(self.lang, self.text)
                self.changed.emit(ans)
        elif self.option == 'download':
            try:
                os.system(APIconf.audio_link.format(self.text, self.lang))
            except BaseException as r:
                # self.changed.emit('failed')
                print('Traceback:', r)
            else:
                self.changed.emit('ok')


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(QMainWindow, self).__init__(*args)

        self.ui = mainWindow.Ui_Form()
        self.ui.setupUi(self)

        self.langs_from = sorted(APIconf.langs.keys())
        self.langs_to = self.langs_from.copy()

        self.langs_from.remove('английский')
        self.langs_from.insert(0, 'английский')
        self.ui.lang_from.addItems(self.langs_from)

        self.langs_to.remove('русский')
        self.langs_to.insert(0, 'русский')
        self.ui.lang_to.addItems(self.langs_to)

        self.chang_lang = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+F"), self)
        self.chang_lang.activated.connect(self.swap_langs)
        self.chang_lang.activated.connect(self.ready)

        self.speech_text = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+1"), self)
        self.speech_text.activated.connect(self.sound_text)

        self.speech_trans = QtWidgets.QShortcut(QtGui.QKeySequence("Alt+2"), self)
        self.speech_trans.activated.connect(self.sound_translate)

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

        lang = APIconf.langs[self.ui.lang_from.currentText()] + '-' + APIconf.langs[self.ui.lang_to.currentText()]
        text = self.ui.text.toPlainText()

        if text.strip():
            cur_threads = []
            for i in self.threads:
                i.stop = True
                if not i.isFinished():
                    cur_threads.append(i)
            self.threads = cur_threads

            update = Options(lang, text, 'transl')
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
            for i in range(self.ui.translation.count()):
                k = self.ui.translation.item(i).text()
                if ' / ' in k:
                    tl = k.split(' / ')[0].strip()
            res = add_word(word, ts, tl)
            if res:
                self.ui.translation.item(ind).setBackground(QtGui.QBrush(QtGui.QColor(255, 234, 2)))

    cur_sound = None

    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./Temp/speech.mp3")
        pygame.mixer.music.play()

    def sound_text(self):
        text = self.ui.text.toPlainText()
        lang = APIconf.langs[self.ui.lang_from.currentText()] + '-' + APIconf.langs[self.ui.lang_to.currentText()]

        if text:
            if self.cur_sound and self.cur_sound.isRunning():
                self.cur_sound.join(2)
            self.cur_sound = Options(lang, text, 'download')
            self.cur_sound.start()
            self.cur_sound.changed.connect(self.play_sound)

    def sound_translate(self):
        text = self.ui.translation.item(0).text()
        lang = APIconf.langs[self.ui.lang_from.currentText()] + '-' + APIconf.langs[self.ui.lang_to.currentText()]

        if text:
            if self.cur_sound and self.cur_sound.isRunning():
                self.cur_sound.join(2)
            self.cur_sound = Options(lang, text, 'download')
            self.cur_sound.start()
            self.cur_sound.changed.connect(self.play_sound)


# -----------------------------------------------------#
app = QApplication(sys.argv)
app.setApplicationName('GUI')

form = MainWindow()
form.setWindowTitle('Translator')
form.show()

sys.exit(app.exec_())
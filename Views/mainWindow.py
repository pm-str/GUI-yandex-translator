# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(655, 213)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowOpacity(1.0)
        self.text = QtWidgets.QTextBrowser(Form)
        self.text.setGeometry(QtCore.QRect(1, 30, 323, 181))
        self.text.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.text.setReadOnly(False)
        self.text.setAcceptRichText(False)
        self.text.setObjectName("text")
        self.translation = QtWidgets.QListWidget(Form)
        self.translation.setGeometry(QtCore.QRect(330, 30, 323, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translation.sizePolicy().hasHeightForWidth())
        self.translation.setSizePolicy(sizePolicy)
        self.translation.setAutoFillBackground(False)
        self.translation.setLineWidth(1)
        self.translation.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.translation.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.translation.setAutoScroll(True)
        self.translation.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.translation.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.translation.setProperty("isWrapping", False)
        self.translation.setWordWrap(True)
        self.translation.setObjectName("translation")
        self.swapl = QtWidgets.QPushButton(Form)
        self.swapl.setGeometry(QtCore.QRect(310, 0, 31, 29))
        self.swapl.setStyleSheet("border-image: url(:/newPrefix/Views/1486387886_exchange.png);")
        self.swapl.setText("")
        self.swapl.setObjectName("swapl")
        self.lang_from = QtWidgets.QComboBox(Form)
        self.lang_from.setGeometry(QtCore.QRect(122, 1, 151, 28))
        self.lang_from.setObjectName("lang_from")
        self.lang_to = QtWidgets.QComboBox(Form)
        self.lang_to.setGeometry(QtCore.QRect(380, 1, 151, 28))
        self.lang_to.setObjectName("lang_to")
        self.sound_te = QtWidgets.QPushButton(Form)
        self.sound_te.setGeometry(QtCore.QRect(1, 2, 25, 25))
        self.sound_te.setStyleSheet("border-image: url(:/newPrefix/Views/1486598014_volume-24.png);")
        self.sound_te.setText("")
        self.sound_te.setObjectName("sound_te")
        self.sound_tr = QtWidgets.QPushButton(Form)
        self.sound_tr.setGeometry(QtCore.QRect(625, 2, 25, 25))
        self.sound_tr.setStyleSheet("border-image: url(:/newPrefix/Views/1486598014_volume-24.png);")
        self.sound_tr.setText("")
        self.sound_tr.setObjectName("sound_tr")

        self.retranslateUi(Form)
        self.swapl.clicked.connect(Form.swap_langs)
        self.text.textChanged.connect(Form.ready)
        self.swapl.clicked.connect(Form.ready)
        self.lang_from.activated['int'].connect(Form.ready)
        self.lang_to.activated['int'].connect(Form.ready)
        self.translation.doubleClicked['QModelIndex'].connect(Form.add_by_api)
        self.sound_te.clicked.connect(Form.sound_text)
        self.sound_tr.clicked.connect(Form.sound_translate)
        self.lang_to.activated['QString'].connect(Form.change_langs_to)
        self.lang_from.activated['QString'].connect(Form.change_langs_from)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form1"))
        self.text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import exchange_rc

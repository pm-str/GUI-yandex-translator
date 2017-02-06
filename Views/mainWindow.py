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
        self.text.setReadOnly(False)
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
        self.swapl.setStyleSheet("border-image: url(:/newPrefix/1486387886_exchange.png);")
        self.swapl.setText("")
        self.swapl.setObjectName("swapl")
        self.lang_from = QtWidgets.QComboBox(Form)
        self.lang_from.setGeometry(QtCore.QRect(122, 1, 151, 28))
        self.lang_from.setObjectName("lang_from")
        self.lang_to = QtWidgets.QComboBox(Form)
        self.lang_to.setGeometry(QtCore.QRect(380, 1, 151, 28))
        self.lang_to.setObjectName("lang_to")

        self.retranslateUi(Form)
        self.swapl.clicked.connect(Form.swap_langs)
        self.text.textChanged.connect(Form.ready)
        self.swapl.clicked.connect(Form.ready)
        self.lang_from.activated['int'].connect(Form.ready)
        self.lang_to.activated['int'].connect(Form.ready)
        self.translation.doubleClicked['QModelIndex'].connect(Form.add_by_api)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form1"))

import exchange_rc

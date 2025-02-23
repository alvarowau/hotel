# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_clientes.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)

class Ui_Clientes(object):
    def setupUi(self, Clientes):
        if not Clientes.objectName():
            Clientes.setObjectName(u"Clientes")
        Clientes.resize(1080, 640)
        Clientes.setMinimumSize(QSize(1080, 640))
        Clientes.setStyleSheet(u"")
        self.title_label = QLabel(Clientes)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(30, 10, 171, 51))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"QLabel {\n"
"    color: #FFFFFF;  /* Texto blanco */\n"
"    font-size: 24px;  /* Tama\u00f1o de la fuente m\u00e1s grande */\n"
"    font-weight: 600;\n"
"    padding: 10px;  /* Espaciado */\n"
"}\n"
"")
        self.clientes_tableView = QTableView(Clientes)
        self.clientes_tableView.setObjectName(u"clientes_tableView")
        self.clientes_tableView.setGeometry(QRect(40, 80, 981, 461))
        self.widget = QWidget(Clientes)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(270, 560, 572, 61))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nuevo_pushButton = QPushButton(self.widget)
        self.nuevo_pushButton.setObjectName(u"nuevo_pushButton")
        self.nuevo_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6200EE; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 12px 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3700B3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3100A0;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.nuevo_pushButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.saber_pushButton = QPushButton(self.widget)
        self.saber_pushButton.setObjectName(u"saber_pushButton")
        self.saber_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #6200EE; \n"
"    color: #FFFFFF; \n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 12px 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3700B3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3100A0;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.saber_pushButton, 0, 2, 1, 1)


        self.retranslateUi(Clientes)

        QMetaObject.connectSlotsByName(Clientes)
    # setupUi

    def retranslateUi(self, Clientes):
        Clientes.setWindowTitle(QCoreApplication.translate("Clientes", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Clientes", u"CLIENTES", None))
        self.nuevo_pushButton.setText(QCoreApplication.translate("Clientes", u"Nueva Reserva", None))
        self.saber_pushButton.setText(QCoreApplication.translate("Clientes", u"Saber mas", None))
    # retranslateUi


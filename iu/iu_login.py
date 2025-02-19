# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(391, 501)
        Form.setMinimumSize(QSize(391, 501))
        Form.setMaximumSize(QSize(391, 501))
        Form.setStyleSheet(u"/* Estilos generales del formulario */\n"
"QWidget {\n"
"    background-color: #E8EAF6;\n"
"    border-radius: 12px;\n"
"    padding: 24px;\n"
"}\n"
"\n"
"/* Estilos para etiquetas (QLabel) */\n"
"QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    color: #333333; \n"
"}\n"
"\n"
"/* Estilos para campos de entrada (QLineEdit) */\n"
"QLineEdit {\n"
"    border: 2px solid #6200EE; /* Borde del color primario de Android */\n"
"    border-radius: 8px;\n"
"    padding: 10px 14px;\n"
"    background-color: #FFFFFF;\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #03DAC5; /* Cambio al color secundario */\n"
"    box-shadow: 0 0 6px rgba(3, 218, 197, 0.5);\n"
"}\n"
"\n"
"/* Estilos para botones (QPushButton) */\n"
"QPushButton {\n"
"    background-color: #6200EE; /* Color primario de Android */\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
""
                        "    padding: 12px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    transition: background-color 0.3s ease-in-out, box-shadow 0.2s ease-in-out;\n"
"    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3700B3; /* Versi\u00f3n m\u00e1s oscura del primario */\n"
"    box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3100A0;\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 391, 501))
        self.widget.setMinimumSize(QSize(391, 501))
        self.widget.setMaximumSize(QSize(391, 501))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    color: #6200EE;\n"
"    text-align: center;\n"
"    margin-bottom: 25px;\n"
"}")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 4)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #03DAC5; /* Color secundario de Android */\n"
"    color: #000000; /* Texto oscuro para contraste */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #018786; /* Versi\u00f3n m\u00e1s oscura del secundario */\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"HOTEL", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"USUARIO:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"CONTRASE\u00d1A:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SALIR", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"LOGUEAR", None))
    # retranslateUi


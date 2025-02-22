# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)


class Ui_Loguin(object):
    def setupUi(self, Loguin):
        if not Loguin.objectName():
            Loguin.setObjectName("Loguin")
        Loguin.resize(391, 501)
        Loguin.setMinimumSize(QSize(391, 501))
        Loguin.setMaximumSize(QSize(391, 501))
        Loguin.setStyleSheet(
            "/* Estilos generales del formulario */\n"
            "QWidget {\n"
            "    background-color: #121212;  /* Fondo oscuro */\n"
            "    border-radius: 12px;\n"
            "    padding: 24px;\n"
            "}\n"
            "\n"
            "/* Estilos para etiquetas (QLabel) */\n"
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E0E0E0;  /* Texto en gris claro */\n"
            "}\n"
            "\n"
            "/* Estilos para QLineEdit */\n"
            "QLineEdit {\n"
            "    border: 2px solid #BB86FC;  /* Color violeta claro */\n"
            "    border-radius: 8px;\n"
            "    padding: 10px 14px;\n"
            "    background-color: #333333;  /* Fondo oscuro para el input */\n"
            "    font-size: 14px;\n"
            "    color: #E0E0E0;  /* Texto claro en los inputs */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #03DAC5;  /* Color verde cuando el input est\u00e1 enfocado */\n"
            "}\n"
            "\n"
            "/* Estilos para QPushButton */\n"
            "QPushButton {\n"
            "    background-color: #6200EE;  /* Violeta principal */\n"
            "    color: #FFFFFF;  /* Texto blanco */\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    padding: 12px 20px;\n"
            ""
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3700B3;  /* Violeta m\u00e1s oscuro al pasar el mouse */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #3100A0;  /* Violeta m\u00e1s oscuro al presionar el bot\u00f3n */\n"
            "}\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            ""
        )
        self.widget = QWidget(Loguin)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(0, 0, 391, 501))
        self.widget.setMinimumSize(QSize(391, 501))
        self.widget.setMaximumSize(QSize(391, 501))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalSpacer = QSpacerItem(
            97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "QLabel{\n"
            "    font-size: 26px;\n"
            "    font-weight: bold;\n"
            "    color: #6200EE;\n"
            "    text-align: center;\n"
            "    margin-bottom: 25px;\n"
            "}"
        )

        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(
            97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 4)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #03DAC5; /* Color secundario de Android */\n"
            "    color: #000000; /* Texto oscuro para contraste */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #018786; /* Versi\u00f3n m\u00e1s oscura del secundario */\n"
            "}"
        )

        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 2)

        self.retranslateUi(Loguin)

        QMetaObject.connectSlotsByName(Loguin)

    # setupUi

    def retranslateUi(self, Loguin):
        Loguin.setWindowTitle(QCoreApplication.translate("Loguin", "ACCESO", None))
        self.label.setText(QCoreApplication.translate("Loguin", "HOTEL", None))
        self.label_2.setText(QCoreApplication.translate("Loguin", "USUARIO:", None))
        self.label_3.setText(
            QCoreApplication.translate("Loguin", "CONTRASE\u00d1A:", None)
        )
        self.pushButton.setText(QCoreApplication.translate("Loguin", "SALIR", None))
        self.pushButton_2.setText(QCoreApplication.translate("Loguin", "LOGUEAR", None))

    # retranslateUi

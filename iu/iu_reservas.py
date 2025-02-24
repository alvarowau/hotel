# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableView,
    QWidget,
)


class Ui_Reservas(object):
    def setupUi(self, Reservas):
        if not Reservas.objectName():
            Reservas.setObjectName("Reservas")
        Reservas.resize(1080, 640)
        Reservas.setMinimumSize(QSize(1080, 640))
        Reservas.setStyleSheet(
            "QWidget {\n"
            "    background-color: #121212; \n"
            "    color: #E8EAF6; \n"
            "}"
        )
        self.title_label = QLabel(Reservas)
        self.title_label.setObjectName("title_label")
        self.title_label.setGeometry(QRect(30, 10, 171, 51))
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(
            "QLabel {\n"
            "    color: #FFFFFF;  /* Texto blanco */\n"
            "    font-size: 24px;  /* Tama\u00f1o de la fuente m\u00e1s grande */\n"
            "    font-weight: 600;\n"
            "    padding: 10px;  /* Espaciado */\n"
            "}\n"
            ""
        )
        self.reservas_tableView = QTableView(Reservas)
        self.reservas_tableView.setObjectName("reservas_tableView")
        self.reservas_tableView.setGeometry(QRect(180, 80, 871, 431))
        self.salones_listWidget = QListWidget(Reservas)
        self.salones_listWidget.setObjectName("salones_listWidget")
        self.salones_listWidget.setGeometry(QRect(10, 180, 151, 331))
        self.salones_label = QLabel(Reservas)
        self.salones_label.setObjectName("salones_label")
        self.salones_label.setGeometry(QRect(10, 120, 141, 41))
        self.salones_label.setStyleSheet(
            "QLabel {\n"
            "    color: #FFFFFF;  /* Texto blanco */\n"
            "    font-size: 18px;  /* Tama\u00f1o de la fuente m\u00e1s grande */\n"
            "    font-weight: 600;\n"
            "    padding: 10px;  /* Espaciado */\n"
            "}\n"
            ""
        )
        self.widget = QWidget(Reservas)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(270, 550, 572, 61))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.nuevo_pushButton = QPushButton(self.widget)
        self.nuevo_pushButton.setObjectName("nuevo_pushButton")
        self.nuevo_pushButton.setStyleSheet(
            "QPushButton {\n"
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
            ""
        )

        self.gridLayout.addWidget(self.nuevo_pushButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.saber_pushButton = QPushButton(self.widget)
        self.saber_pushButton.setObjectName("saber_pushButton")
        self.saber_pushButton.setStyleSheet(
            "QPushButton {\n"
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
            ""
        )

        self.gridLayout.addWidget(self.saber_pushButton, 0, 2, 1, 1)

        self.retranslateUi(Reservas)

        QMetaObject.connectSlotsByName(Reservas)

    # setupUi

    def retranslateUi(self, Reservas):
        Reservas.setWindowTitle(QCoreApplication.translate("Reservas", "Form", None))
        self.title_label.setText(
            QCoreApplication.translate("Reservas", "RESERVAS", None)
        )
        self.salones_label.setText(
            QCoreApplication.translate("Reservas", "SALONES:", None)
        )
        self.nuevo_pushButton.setText(
            QCoreApplication.translate("Reservas", "Nueva Reserva", None)
        )
        self.saber_pushButton.setText(
            QCoreApplication.translate("Reservas", "Saber mas", None)
        )

    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_conexion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton


class Ui_conexion(object):
    def setupUi(self, conexion):
        if not conexion.objectName():
            conexion.setObjectName("conexion")
        conexion.resize(719, 674)
        conexion.setMinimumSize(QSize(719, 674))
        conexion.setMaximumSize(QSize(719, 674))
        conexion.setStyleSheet(
            "QWidget {\n"
            "    background-color: #121212;  \n"
            "    border-radius: 12px;\n"
            "    padding: 24px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E0E0E0;\n"
            "    padding: 2px;  \n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    border: 2px solid #BB86FC;  \n"
            "    border-radius: 8px;\n"
            "    background-color: #333333;\n"
            "    font-size: 12px;\n"
            "    color: #E0E0E0;  \n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #03DAC5;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #6200EE;  \n"
            "    color: #FFFFFF;  \n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    padding: 12px 20px;\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3700B3;  \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #3100A0;  \n"
            "}\n"
            "\n"
            ""
        )
        self.label_img = QLabel(conexion)
        self.label_img.setObjectName("label_img")
        self.label_img.setGeometry(QRect(0, 0, 721, 401))
        self.label_img.setPixmap(QPixmap(":/prefijoNuevo/imagenes/no_conexion.jpg"))
        self.label_host = QLabel(conexion)
        self.label_host.setObjectName("label_host")
        self.label_host.setGeometry(QRect(20, 430, 71, 21))
        self.label_host.setStyleSheet("")
        self.lineEdit_host = QLineEdit(conexion)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.lineEdit_host.setGeometry(QRect(120, 430, 171, 31))
        self.label_user = QLabel(conexion)
        self.label_user.setObjectName("label_user")
        self.label_user.setGeometry(QRect(20, 490, 71, 21))
        self.label_user.setStyleSheet("")
        self.lineEdit_user = QLineEdit(conexion)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_user.setGeometry(QRect(120, 490, 171, 31))
        self.label_pass = QLabel(conexion)
        self.label_pass.setObjectName("label_pass")
        self.label_pass.setGeometry(QRect(20, 550, 71, 21))
        self.label_pass.setStyleSheet("")
        self.lineEdit_pass = QLineEdit(conexion)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_pass.setGeometry(QRect(120, 550, 171, 31))
        self.lineEdit_db = QLineEdit(conexion)
        self.lineEdit_db.setObjectName("lineEdit_db")
        self.lineEdit_db.setGeometry(QRect(410, 460, 171, 31))
        self.label_db = QLabel(conexion)
        self.label_db.setObjectName("label_db")
        self.label_db.setGeometry(QRect(310, 460, 71, 21))
        self.label_db.setStyleSheet("")
        self.lineEdit_port = QLineEdit(conexion)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.lineEdit_port.setGeometry(QRect(410, 520, 171, 31))
        self.label_port = QLabel(conexion)
        self.label_port.setObjectName("label_port")
        self.label_port.setGeometry(QRect(310, 520, 71, 21))
        self.label_port.setStyleSheet("")
        self.pushButton_probar = QPushButton(conexion)
        self.pushButton_probar.setObjectName("pushButton_probar")
        self.pushButton_probar.setGeometry(QRect(90, 600, 211, 51))
        self.pushButton_conectar = QPushButton(conexion)
        self.pushButton_conectar.setObjectName("pushButton_conectar")
        self.pushButton_conectar.setGeometry(QRect(400, 600, 211, 51))

        self.retranslateUi(conexion)

        QMetaObject.connectSlotsByName(conexion)

    # setupUi

    def retranslateUi(self, conexion):
        conexion.setWindowTitle(
            QCoreApplication.translate("conexion", "conexion", None)
        )
        self.label_img.setText("")
        self.label_host.setText(QCoreApplication.translate("conexion", "HOST:", None))
        self.label_user.setText(QCoreApplication.translate("conexion", "USER:", None))
        self.label_pass.setText(QCoreApplication.translate("conexion", "PASS:", None))
        self.label_db.setText(QCoreApplication.translate("conexion", "DB:", None))
        self.label_port.setText(QCoreApplication.translate("conexion", "PORT:", None))
        self.pushButton_probar.setText(
            QCoreApplication.translate("conexion", "PROBAR", None)
        )
        self.pushButton_conectar.setText(
            QCoreApplication.translate("conexion", "CONECTAR", None)
        )

    # retranslateUi

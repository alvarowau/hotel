# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_conexion.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QFormLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


class Ui_conexion(object):
    def setupUi(self, conexion):
        if not conexion.objectName():
            conexion.setObjectName("conexion")
        conexion.resize(561, 301)
        conexion.setMinimumSize(QSize(561, 301))
        conexion.setMaximumSize(QSize(561, 301))
        conexion.setStyleSheet(
            "QWidget {\n"
            "    background-color: #121212;\n"
            "    font-family: 'Roboto', sans-serif;\n"
            "    font-size: 14px;\n"
            "    color: #E0E0E0;\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
            "    border: 1px solid #424242;\n"
            "    border-radius: 4px;\n"
            "    padding: 6px;\n"
            "    background-color: #1E1E1E;\n"
            "    color: #E0E0E0;\n"
            "    selection-background-color: #64B5F6;\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid #BB86FC;\n"
            "}\n"
            "\n"
            "\n"
            "QDateEdit {\n"
            "    border: 1px solid #424242;\n"
            "    border-radius: 4px;\n"
            "    padding: 6px;\n"
            "    background-color: #1E1E1E;\n"
            "    color: #E0E0E0;\n"
            "}\n"
            "QDateEdit::drop-down {\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: #BB86FC;\n"
            "    color: black;\n"
            "    border-radius: 4px;\n"
            "    padding: 8px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "    background-color: #9B5DE5;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #7A3E9D;\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    border: 1px solid #424242;\n"
            "    border-radius: 4px;\n"
            "    padding: 6px"
            ";\n"
            "    background-color: #1E1E1E;\n"
            "    color: #E0E0E0;\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    border: none;\n"
            "}\n"
            "\n"
            "QCheckBox {\n"
            "    spacing: 5px;\n"
            "}\n"
            "QCheckBox::indicator {\n"
            "    width: 16px;\n"
            "    height: 16px;\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "    border: 1px solid #757575;\n"
            "    background-color: #1E1E1E;\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background-color: #BB86FC;\n"
            "    border: 1px solid #BB86FC;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    font-weight: bold;\n"
            "    color: #E0E0E0;\n"
            "}\n"
            ""
        )
        self.widget_5 = QWidget(conexion)
        self.widget_5.setObjectName("widget_5")
        self.widget_5.setGeometry(QRect(0, 0, 561, 301))
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_conectar = QPushButton(self.widget_4)
        self.pushButton_conectar.setObjectName("pushButton_conectar")

        self.gridLayout_3.addWidget(self.pushButton_conectar, 0, 1, 1, 1)

        self.pushButton_probar = QPushButton(self.widget_4)
        self.pushButton_probar.setObjectName("pushButton_probar")

        self.gridLayout_3.addWidget(self.pushButton_probar, 0, 0, 1, 1)

        self.gridLayout_4.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label_host = QLabel(self.widget)
        self.label_host.setObjectName("label_host")
        self.label_host.setStyleSheet("")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_host)

        self.lineEdit_host = QLineEdit(self.widget)
        self.lineEdit_host.setObjectName("lineEdit_host")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_host)

        self.label_user = QLabel(self.widget)
        self.label_user.setObjectName("label_user")
        self.label_user.setStyleSheet("")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_user)

        self.lineEdit_user = QLineEdit(self.widget)
        self.lineEdit_user.setObjectName("lineEdit_user")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_user)

        self.label_pass = QLabel(self.widget)
        self.label_pass.setObjectName("label_pass")
        self.label_pass.setStyleSheet("")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_pass)

        self.lineEdit_pass = QLineEdit(self.widget)
        self.lineEdit_pass.setObjectName("lineEdit_pass")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_pass)

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_db = QLabel(self.widget_2)
        self.label_db.setObjectName("label_db")
        self.label_db.setStyleSheet("")

        self.gridLayout.addWidget(self.label_db, 0, 0, 1, 1)

        self.lineEdit_db = QLineEdit(self.widget_2)
        self.lineEdit_db.setObjectName("lineEdit_db")

        self.gridLayout.addWidget(self.lineEdit_db, 0, 1, 1, 1)

        self.label_port = QLabel(self.widget_2)
        self.label_port.setObjectName("label_port")
        self.label_port.setStyleSheet("")

        self.gridLayout.addWidget(self.label_port, 1, 0, 1, 1)

        self.lineEdit_port = QLineEdit(self.widget_2)
        self.lineEdit_port.setObjectName("lineEdit_port")

        self.gridLayout.addWidget(self.lineEdit_port, 1, 1, 1, 1)

        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.gridLayout_4.addWidget(self.widget_3, 0, 0, 1, 1)

        self.retranslateUi(conexion)

        QMetaObject.connectSlotsByName(conexion)

    # setupUi

    def retranslateUi(self, conexion):
        conexion.setWindowTitle(
            QCoreApplication.translate("conexion", "conexion", None)
        )
        self.pushButton_conectar.setText(
            QCoreApplication.translate("conexion", "CONECTAR", None)
        )
        self.pushButton_probar.setText(
            QCoreApplication.translate("conexion", "PROBAR", None)
        )
        self.label_host.setText(QCoreApplication.translate("conexion", "HOST:", None))
        self.label_user.setText(QCoreApplication.translate("conexion", "USER:", None))
        self.label_pass.setText(QCoreApplication.translate("conexion", "PASS:", None))
        self.label_db.setText(QCoreApplication.translate("conexion", "DB:", None))
        self.label_port.setText(QCoreApplication.translate("conexion", "PORT:", None))

    # retranslateUi

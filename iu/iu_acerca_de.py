# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_acerca_de.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import QLabel, QPushButton


class Ui_a(object):
    def setupUi(self, a):
        if not a.objectName():
            a.setObjectName("a")
        a.resize(1080, 640)
        a.setMinimumSize(QSize(1080, 640))
        a.setMaximumSize(QSize(1080, 640))
        a.setStyleSheet(
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
            "}"
        )
        self.label = QLabel(a)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(30, 40, 241, 51))
        self.label_2 = QLabel(a)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(30, 120, 561, 391))
        self.label_3 = QLabel(a)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(630, 20, 401, 281))
        self.label_3.setStyleSheet("image: url(:/prefijoNuevo/acerca_de_imagen.png);")
        self.label_4 = QLabel(a)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(630, 320, 401, 281))
        self.label_4.setStyleSheet("image: url(:/prefijoNuevo/acerca_de_2.png);")
        self.pushButton = QPushButton(a)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(190, 560, 171, 41))

        self.retranslateUi(a)

        QMetaObject.connectSlotsByName(a)

    # setupUi

    def retranslateUi(self, a):
        a.setWindowTitle(QCoreApplication.translate("a", "Form", None))
        self.label.setText(
            QCoreApplication.translate(
                "a",
                '<html><head/><body><p><span style=" font-size:18pt; font-weight:700;">ACERCA DE:</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "a",
                '<html><head/><body><p><span style=" font-size:14pt; font-weight:700;">Nombre:</span><span style=" font-size:14pt;"> Reservas Manager</span></p><p><span style=" font-size:14pt; font-weight:700;">Versi\u00f3n:</span><span style=" font-size:14pt;"> 1.0.0</span></p><p><span style=" font-size:14pt; font-weight:700;">Descripci\u00f3n:</span><span style=" font-size:14pt;"> Aplicaci\u00f3n para gestionar reserva</span></p><p><span style=" font-size:14pt;">y clientes de manera r\u00e1pida y eficiente.</span></p><p><span style=" font-size:14pt; font-weight:700;">Desarrollador:</span><span style=" font-size:14pt;"> \u00c1lvaro Bajo</span></p><p><span style=" font-size:14pt; font-weight:700;">Contacto:</span><span style=" font-size:14pt;"> alvarobajo893@gmail.com</span></p><p><span style=" font-size:14pt; font-weight:700;">Licencia:</span><span style=" font-size:14pt;"> MIT</span></p><p><span style=" font-size:14pt; font-weight:700;">Tecnolog\u00edas:</span><span style=" font-size:14pt;"> Des'
                "arrollado con PySide6 y MySql</span></p></body></html>",
                None,
            )
        )
        self.label_3.setText("")
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("a", "Repositorio", None))

    # retranslateUi

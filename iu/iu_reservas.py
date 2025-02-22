# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtWidgets import (
    QFormLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QWidget,
)


class Ui_RESERVAS(object):
    def setupUi(self, RESERVAS):
        if not RESERVAS.objectName():
            RESERVAS.setObjectName("RESERVAS")
        RESERVAS.resize(900, 600)
        RESERVAS.setMinimumSize(QSize(900, 600))
        RESERVAS.setMaximumSize(QSize(900, 600))
        RESERVAS.setStyleSheet(
            "QWidget {\n"
            "    background-color: #121212;  \n"
            "    border-radius: 12px;\n"
            "    padding: 24px;\n"
            "    color: #E8EAF6;  \n"
            "}\n"
            "\n"
            "\n"
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E8EAF6;  \n"
            "}\n"
            "\n"
            "\n"
            "QLineEdit {\n"
            "    border: 2px solid #6200EE;\n"
            "    border-radius: 8px;\n"
            "    padding: 10px 14px;\n"
            "    background-color: #333333;  \n"
            "    font-size: 14px;\n"
            "    color: #E8EAF6;  \n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #03DAC5; \n"
            "}\n"
            "\n"
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
            "    background-color: #3700B3;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #3100A0;\n"
            "}\n"
            "\n"
            ""
        )
        self.tableWidget_reservas = QTableWidget(RESERVAS)
        self.tableWidget_reservas.setObjectName("tableWidget_reservas")
        self.tableWidget_reservas.setGeometry(QRect(20, 10, 701, 571))
        self.widget_2 = QWidget(RESERVAS)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(740, 0, 144, 591))
        self.formLayout_2 = QFormLayout(self.widget_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalSpacer = QSpacerItem(
            20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_2.setItem(0, QFormLayout.LabelRole, self.verticalSpacer)

        self.modificar_button = QPushButton(self.widget_2)
        self.modificar_button.setObjectName("modificar_button")
        self.modificar_button.setMinimumSize(QSize(120, 40))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.modificar_button)

        self.verticalSpacer_2 = QSpacerItem(
            20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_2.setItem(2, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.nueva_button = QPushButton(self.widget_2)
        self.nueva_button.setObjectName("nueva_button")
        self.nueva_button.setMinimumSize(QSize(120, 40))

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.nueva_button)

        self.verticalSpacer_3 = QSpacerItem(
            20, 53, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_2.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.eliminar_button = QPushButton(self.widget_2)
        self.eliminar_button.setObjectName("eliminar_button")
        self.eliminar_button.setMinimumSize(QSize(120, 40))

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.eliminar_button)

        self.verticalSpacer_4 = QSpacerItem(
            20, 188, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_2.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.salir_button = QPushButton(self.widget_2)
        self.salir_button.setObjectName("salir_button")
        self.salir_button.setMinimumSize(QSize(120, 40))
        self.salir_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #03DAC5; \n"
            "    color: #000000; \n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #018786;  \n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #01675B;  \n"
            "}"
        )

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.salir_button)

        self.retranslateUi(RESERVAS)

        QMetaObject.connectSlotsByName(RESERVAS)

    # setupUi

    def retranslateUi(self, RESERVAS):
        RESERVAS.setWindowTitle(
            QCoreApplication.translate("RESERVAS", "RESERVAS", None)
        )
        self.modificar_button.setText(
            QCoreApplication.translate("RESERVAS", "Modificar", None)
        )
        self.nueva_button.setText(QCoreApplication.translate("RESERVAS", "Nueva", None))
        self.eliminar_button.setText(
            QCoreApplication.translate("RESERVAS", "Eliminar", None)
        )
        self.salir_button.setText(QCoreApplication.translate("RESERVAS", "SALIR", None))

    # retranslateUi

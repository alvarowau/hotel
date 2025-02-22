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
    QTableView,
    QWidget,
)


class Ui_reservas(object):
    def setupUi(self, reservas):
        if not reservas.objectName():
            reservas.setObjectName("reservas")
        reservas.resize(900, 600)
        reservas.setMinimumSize(QSize(900, 600))
        reservas.setMaximumSize(QSize(900, 600))
        reservas.setStyleSheet(
            "/* Estilos generales del formulario */\n"
            "QWidget {\n"
            "    background-color: #121212;  /* Fondo oscuro */\n"
            "    border-radius: 12px;\n"
            "    padding: 24px;\n"
            "    color: #E8EAF6;  /* Texto claro */\n"
            "}\n"
            "\n"
            "/* Estilos para etiquetas (QLabel) */\n"
            "QLabel {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E8EAF6;  /* Texto claro en modo oscuro */\n"
            "}\n"
            "\n"
            "/* Estilo para los campos de texto (QLineEdit) */\n"
            "QLineEdit {\n"
            "    border: 2px solid #6200EE;\n"
            "    border-radius: 8px;\n"
            "    padding: 10px 14px;\n"
            "    background-color: #333333;  /* Fondo oscuro para el campo de texto */\n"
            "    font-size: 14px;\n"
            "    color: #E8EAF6;  /* Texto claro */\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #03DAC5;  /* Resalta el borde cuando est\u00e1 enfocado */\n"
            "}\n"
            "\n"
            "/* Estilo para los botones (QPushButton) */\n"
            "QPushButton {\n"
            "    background-color: #6200EE;  /* Fondo del bot\u00f3n */\n"
            "    color: #FFFFFF;  /* Texto blanco */\n"
            "    border: none;\n"
            "    b"
            "order-radius: 8px;\n"
            "    padding: 12px 20px;\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3700B3;  /* Fondo m\u00e1s oscuro cuando se pasa el mouse */\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #3100A0;  /* Fondo a\u00fan m\u00e1s oscuro cuando se presiona */\n"
            "}\n"
            ""
        )
        self.widget_2 = QWidget(reservas)
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
            "   background-color: #03DAC5;\n"
            "    color: #000000;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #018786;\n"
            "	background-color: #018786;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: #01675B;  /* Fondo a\u00fan m\u00e1s oscuro cuando se presiona el bot\u00f3n */\n"
            "}"
        )

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.salir_button)

        self.tableView_reservas = QTableView(reservas)
        self.tableView_reservas.setObjectName("tableView_reservas")
        self.tableView_reservas.setGeometry(QRect(10, 20, 711, 571))
        self.tableView_reservas.setStyleSheet(
            "QTableView {\n"
            "    background-color: #2C2C2C;  /* Fondo oscuro para la tabla */\n"
            "    border-radius: 8px;  /* Bordes redondeados */\n"
            "    color: #E8EAF6;  /* Texto claro */\n"
            "}"
        )

        self.retranslateUi(reservas)

        QMetaObject.connectSlotsByName(reservas)

    # setupUi

    def retranslateUi(self, reservas):
        reservas.setWindowTitle(
            QCoreApplication.translate("reservas", "Reservas", None)
        )
        self.modificar_button.setText(
            QCoreApplication.translate("reservas", "Modificar", None)
        )
        self.nueva_button.setText(QCoreApplication.translate("reservas", "Nueva", None))
        self.eliminar_button.setText(
            QCoreApplication.translate("reservas", "Eliminar", None)
        )
        self.salir_button.setText(QCoreApplication.translate("reservas", "SALIR", None))

    # retranslateUi

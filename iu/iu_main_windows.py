# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_main_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QMenuBar, QStackedWidget, QStatusBar, QWidget


class Ui_HOTEL(object):
    def setupUi(self, HOTEL):
        if not HOTEL.objectName():
            HOTEL.setObjectName("HOTEL")
        HOTEL.resize(915, 663)
        HOTEL.setMinimumSize(QSize(915, 663))
        HOTEL.setMaximumSize(QSize(915, 663))
        HOTEL.setStyleSheet(
            "/* Estilo para el fondo del QWidget en modo oscuro */\n"
            "QWidget {\n"
            "    background-color: #121212; /* Fondo oscuro */\n"
            "    color: #E8EAF6; /* Texto claro en el fondo oscuro */\n"
            "}\n"
            "\n"
            "/* Estilo para la barra de men\u00fas */\n"
            "QMenuBar {\n"
            "    background-color: #333333; /* Fondo oscuro de la barra */\n"
            "    color: #E8EAF6; /* Texto claro en el men\u00fa */\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "}\n"
            "\n"
            "/* Elementos de los men\u00fas en la barra */\n"
            "QMenuBar::item {\n"
            "    background-color: transparent;\n"
            "    color: #E8EAF6;\n"
            "}\n"
            "\n"
            "/* Elementos seleccionados en la barra de men\u00fas */\n"
            "QMenuBar::item:selected {\n"
            "    background-color: #6200EE; /* Color de selecci\u00f3n */\n"
            "    color: #FFFFFF; /* Texto blanco cuando se selecciona */\n"
            "}\n"
            "\n"
            "/* Estilo para las acciones (QAction) */\n"
            "QAction {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E8EAF6; /* Texto claro */\n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "/* A"
            "cci\u00f3n en hover */\n"
            "QAction:hover {\n"
            "    background-color: #6200EE; /* Fondo al pasar el mouse */\n"
            "    color: #FFFFFF; /* Texto blanco */\n"
            "}\n"
            "\n"
            "/* Acci\u00f3n presionada */\n"
            "QAction:pressed {\n"
            "    background-color: #3700B3; /* Fondo m\u00e1s oscuro al presionar */\n"
            "    color: #FFFFFF; /* Texto blanco */\n"
            "}\n"
            "\n"
            "/* Botones (QPushButton) en modo oscuro */\n"
            "QPushButton {\n"
            "    background-color: #6200EE; /* Fondo de bot\u00f3n */\n"
            "    color: #FFFFFF; /* Texto claro */\n"
            "    border-radius: 8px;\n"
            "    font-size: 14px;\n"
            "    font-weight: bold;\n"
            "    padding: 12px 20px;\n"
            "}\n"
            "\n"
            "/* Hover y pressed para botones */\n"
            "QPushButton:hover {\n"
            "    background-color: #3700B3;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #3100A0;\n"
            "}\n"
            "\n"
            "/* Campos de texto (QLineEdit) en modo oscuro */\n"
            "QLineEdit {\n"
            "    border: 2px solid #6200EE;\n"
            "    border-radius: 8px;\n"
            "    background-color: #333333; /* Fondo oscuro */\n"
            "    color: #E8EAF6; "
            "/* Texto claro */\n"
            "    font-size: 14px;\n"
            "    padding: 10px 14px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border-color: #03DAC5; /* Resaltar el borde al enfocar */\n"
            "}\n"
            "\n"
            "/* Otros componentes como labels */\n"
            "QLabel {\n"
            "    color: #E8EAF6; /* Texto claro */\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "}\n"
            "\n"
            ""
        )
        self.actionReservar = QAction(HOTEL)
        self.actionReservar.setObjectName("actionReservar")
        self.actionClientes = QAction(HOTEL)
        self.actionClientes.setObjectName("actionClientes")
        self.actionAcerca = QAction(HOTEL)
        self.actionAcerca.setObjectName("actionAcerca")
        self.actionDocumentaci_n = QAction(HOTEL)
        self.actionDocumentaci_n.setObjectName("actionDocumentaci_n")
        self.centralwidget = QWidget(HOTEL)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QSize(915, 620))
        self.centralwidget.setMaximumSize(QSize(915, 620))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 900, 600))
        self.stackedWidget.setMinimumSize(QSize(900, 600))
        self.stackedWidget.setMaximumSize(QSize(900, 600))
        self.page = QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        HOTEL.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HOTEL)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 915, 25))
        self.menuAplicaciones = QMenu(self.menubar)
        self.menuAplicaciones.setObjectName("menuAplicaciones")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        HOTEL.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HOTEL)
        self.statusbar.setObjectName("statusbar")
        HOTEL.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAplicaciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuAplicaciones.addAction(self.actionReservar)
        self.menuAplicaciones.addAction(self.actionClientes)
        self.menuAyuda.addAction(self.actionAcerca)
        self.menuAyuda.addAction(self.actionDocumentaci_n)

        self.retranslateUi(HOTEL)

        QMetaObject.connectSlotsByName(HOTEL)

    # setupUi

    def retranslateUi(self, HOTEL):
        HOTEL.setWindowTitle(QCoreApplication.translate("HOTEL", "HOTEL", None))
        self.actionReservar.setText(
            QCoreApplication.translate("HOTEL", "Reservar", None)
        )
        self.actionClientes.setText(
            QCoreApplication.translate("HOTEL", "Clientes", None)
        )
        self.actionAcerca.setText(QCoreApplication.translate("HOTEL", "Acerca", None))
        self.actionDocumentaci_n.setText(
            QCoreApplication.translate("HOTEL", "Documentaci\u00f3n", None)
        )
        self.menuAplicaciones.setTitle(
            QCoreApplication.translate("HOTEL", "Aplicaciones", None)
        )
        self.menuAyuda.setTitle(QCoreApplication.translate("HOTEL", "Ayuda", None))

    # retranslateUi

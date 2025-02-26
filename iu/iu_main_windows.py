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
        HOTEL.resize(1100, 681)
        HOTEL.setMinimumSize(QSize(1100, 681))
        HOTEL.setMaximumSize(QSize(1100, 681))
        HOTEL.setStyleSheet(
            "QWidget {\n"
            "    background-color: #121212; \n"
            "    color: #E8EAF6; \n"
            "}\n"
            "\n"
            "QMenuBar {\n"
            "    background-color: #333333; \n"
            "    color: #E8EAF6; \n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "}\n"
            "\n"
            "QMenuBar::item {\n"
            "    background-color: transparent;\n"
            "    color: #E8EAF6;\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "    background-color: #6200EE; \n"
            "    color: #FFFFFF; \n"
            "}\n"
            "\n"
            "QAction {\n"
            "    font-size: 14px;\n"
            "    font-weight: 600;\n"
            "    color: #E8EAF6; \n"
            "    background-color: transparent;\n"
            "}\n"
            "\n"
            "QAction:hover {\n"
            "    background-color: #6200EE; \n"
            "    color: #FFFFFF; \n"
            "}\n"
            "\n"
            "\n"
            "QAction:pressed {\n"
            "    background-color: #3700B3; \n"
            "    color: #FFFFFF; \n"
            "}"
        )
        self.actionReserva = QAction(HOTEL)
        self.actionReserva.setObjectName("actionReserva")
        self.actionReservar = QAction(HOTEL)
        self.actionReservar.setObjectName("actionReservar")
        self.actionAcerca_de = QAction(HOTEL)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionDocumentaci_n = QAction(HOTEL)
        self.actionDocumentaci_n.setObjectName("actionDocumentaci_n")
        self.centralwidget = QWidget(HOTEL)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1081, 641))
        self.stackedWidget.setMinimumSize(QSize(1081, 641))
        self.page = QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        HOTEL.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HOTEL)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 25))
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
        self.menuAplicaciones.addAction(self.actionReserva)
        self.menuAplicaciones.addAction(self.actionReservar)
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuAyuda.addAction(self.actionDocumentaci_n)

        self.retranslateUi(HOTEL)

        QMetaObject.connectSlotsByName(HOTEL)

    # setupUi

    def retranslateUi(self, HOTEL):
        HOTEL.setWindowTitle(QCoreApplication.translate("HOTEL", "Hotel", None))
        self.actionReserva.setText(
            QCoreApplication.translate("HOTEL", "Clientes", None)
        )
        self.actionReservar.setText(
            QCoreApplication.translate("HOTEL", "Reservar", None)
        )
        self.actionAcerca_de.setText(
            QCoreApplication.translate("HOTEL", "Acerca de", None)
        )
        self.actionDocumentaci_n.setText(
            QCoreApplication.translate("HOTEL", "Documentaci\u00f3n", None)
        )
        self.menuAplicaciones.setTitle(
            QCoreApplication.translate("HOTEL", "Aplicaciones", None)
        )
        self.menuAyuda.setTitle(QCoreApplication.translate("HOTEL", "Ayuda", None))

    # retranslateUi

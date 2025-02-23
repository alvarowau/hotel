# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_clientes_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QFormLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Ui_clientes_edit(object):
    def setupUi(self, clientes_edit):
        if not clientes_edit.objectName():
            clientes_edit.setObjectName("clientes_edit")
        clientes_edit.resize(422, 619)
        clientes_edit.setStyleSheet(
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
        self.widget_2 = QWidget(clientes_edit)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(10, 0, 411, 611))
        self.widget_2.setMinimumSize(QSize(411, 611))
        self.widget_2.setMaximumSize(QSize(411, 611))
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.title_label = QLabel(self.widget_2)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(
            "QLabel#titulo {\n"
            "    font-size: 24px;\n"
            "    font-weight: bold;\n"
            "    color: #BB86FC;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 1.5px;\n"
            "    qproperty-alignment: AlignCenter;\n"
            "}"
        )

        self.gridLayout_7.addWidget(self.title_label, 0, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_secret = QWidget(self.widget)
        self.widget_secret.setObjectName("widget_secret")
        self.formLayout = QFormLayout(self.widget_secret)
        self.formLayout.setObjectName("formLayout")
        self.nombre_label = QLabel(self.widget_secret)
        self.nombre_label.setObjectName("nombre_label")
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setBold(True)
        self.nombre_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nombre_label)

        self.nombre_lineEdit = QLineEdit(self.widget_secret)
        self.nombre_lineEdit.setObjectName("nombre_lineEdit")
        self.nombre_lineEdit.setEnabled(True)
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        self.nombre_lineEdit.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre_lineEdit)

        self.apellidos_label = QLabel(self.widget_secret)
        self.apellidos_label.setObjectName("apellidos_label")
        self.apellidos_label.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.apellidos_label)

        self.apellidos_lineEdit = QLineEdit(self.widget_secret)
        self.apellidos_lineEdit.setObjectName("apellidos_lineEdit")
        self.apellidos_lineEdit.setEnabled(True)
        self.apellidos_lineEdit.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.apellidos_lineEdit)

        self.dani_label = QLabel(self.widget_secret)
        self.dani_label.setObjectName("dani_label")
        self.dani_label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.dani_label)

        self.dni_lineEdit = QLineEdit(self.widget_secret)
        self.dni_lineEdit.setObjectName("dni_lineEdit")
        self.dni_lineEdit.setEnabled(True)
        self.dni_lineEdit.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dni_lineEdit)

        self.verticalLayout.addWidget(self.widget_secret)

        self.widget_origen = QWidget(self.widget)
        self.widget_origen.setObjectName("widget_origen")
        self.gridLayout = QGridLayout(self.widget_origen)
        self.gridLayout.setObjectName("gridLayout")
        self.fecha_dateEdit = QDateEdit(self.widget_origen)
        self.fecha_dateEdit.setObjectName("fecha_dateEdit")
        self.fecha_dateEdit.setFont(font1)

        self.gridLayout.addWidget(self.fecha_dateEdit, 0, 1, 1, 1)

        self.fecha_label = QLabel(self.widget_origen)
        self.fecha_label.setObjectName("fecha_label")
        self.fecha_label.setFont(font)

        self.gridLayout.addWidget(self.fecha_label, 0, 0, 1, 1)

        self.pais_lineEdit = QLineEdit(self.widget_origen)
        self.pais_lineEdit.setObjectName("pais_lineEdit")
        self.pais_lineEdit.setEnabled(True)
        self.pais_lineEdit.setFont(font1)

        self.gridLayout.addWidget(self.pais_lineEdit, 1, 1, 1, 1)

        self.pasi_label = QLabel(self.widget_origen)
        self.pasi_label.setObjectName("pasi_label")
        self.pasi_label.setFont(font)

        self.gridLayout.addWidget(self.pasi_label, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_origen)

        self.widget_personal = QWidget(self.widget)
        self.widget_personal.setObjectName("widget_personal")
        self.gridLayout_2 = QGridLayout(self.widget_personal)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.telefono_label = QLabel(self.widget_personal)
        self.telefono_label.setObjectName("telefono_label")
        self.telefono_label.setFont(font)

        self.gridLayout_2.addWidget(self.telefono_label, 0, 0, 1, 1)

        self.telefono_lineEdit = QLineEdit(self.widget_personal)
        self.telefono_lineEdit.setObjectName("telefono_lineEdit")
        self.telefono_lineEdit.setEnabled(True)
        self.telefono_lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.telefono_lineEdit, 0, 1, 1, 1)

        self.mail_label = QLabel(self.widget_personal)
        self.mail_label.setObjectName("mail_label")
        self.mail_label.setFont(font)

        self.gridLayout_2.addWidget(self.mail_label, 1, 0, 1, 1)

        self.mail_lineEdit = QLineEdit(self.widget_personal)
        self.mail_lineEdit.setObjectName("mail_lineEdit")
        self.mail_lineEdit.setEnabled(True)
        self.mail_lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.mail_lineEdit, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.widget_personal)

        self.widget_select = QWidget(self.widget)
        self.widget_select.setObjectName("widget_select")
        self.gridLayout_5 = QGridLayout(self.widget_select)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_3 = QWidget(self.widget_select)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.menores_label = QLabel(self.widget_3)
        self.menores_label.setObjectName("menores_label")
        self.menores_label.setFont(font)

        self.gridLayout_3.addWidget(self.menores_label, 0, 0, 1, 1)

        self.menores_checkBox = QCheckBox(self.widget_3)
        self.menores_checkBox.setObjectName("menores_checkBox")

        self.gridLayout_3.addWidget(self.menores_checkBox, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_sex = QWidget(self.widget_select)
        self.widget_sex.setObjectName("widget_sex")
        self.gridLayout_4 = QGridLayout(self.widget_sex)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sex_label = QLabel(self.widget_sex)
        self.sex_label.setObjectName("sex_label")
        self.sex_label.setFont(font)

        self.gridLayout_4.addWidget(self.sex_label, 0, 0, 1, 1)

        self.sex_comboBox = QComboBox(self.widget_sex)
        self.sex_comboBox.setObjectName("sex_comboBox")

        self.gridLayout_4.addWidget(self.sex_comboBox, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.widget_sex, 1, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_select)

        self.widget_botones = QWidget(self.widget)
        self.widget_botones.setObjectName("widget_botones")
        self.gridLayout_6 = QGridLayout(self.widget_botones)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.boton_izquierdo_pushButton = QPushButton(self.widget_botones)
        self.boton_izquierdo_pushButton.setObjectName("boton_izquierdo_pushButton")

        self.gridLayout_6.addWidget(self.boton_izquierdo_pushButton, 0, 0, 1, 1)

        self.boton_derecho_pushButton = QPushButton(self.widget_botones)
        self.boton_derecho_pushButton.setObjectName("boton_derecho_pushButton")

        self.gridLayout_6.addWidget(self.boton_derecho_pushButton, 0, 1, 1, 1)

        self.verticalLayout.addWidget(self.widget_botones)

        self.gridLayout_7.addWidget(self.widget, 1, 0, 1, 1)

        self.retranslateUi(clientes_edit)

        QMetaObject.connectSlotsByName(clientes_edit)

    # setupUi

    def retranslateUi(self, clientes_edit):
        clientes_edit.setWindowTitle(
            QCoreApplication.translate("clientes_edit", "Form", None)
        )
        self.title_label.setText(
            QCoreApplication.translate("clientes_edit", "TITULO", None)
        )
        # if QT_CONFIG(tooltip)
        self.nombre_label.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Nombre del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.nombre_label.setText(
            QCoreApplication.translate("clientes_edit", "Nombre", None)
        )
        # if QT_CONFIG(tooltip)
        self.nombre_lineEdit.setToolTip(
            QCoreApplication.translate("clientes_edit", "Nombre del/la cliente/a", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.apellidos_label.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Nombre del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.apellidos_label.setText(
            QCoreApplication.translate("clientes_edit", "Apellidos", None)
        )
        # if QT_CONFIG(tooltip)
        self.apellidos_lineEdit.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Apellidos del/la cliente/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.dani_label.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.dani_label.setText(
            QCoreApplication.translate("clientes_edit", "DNI", None)
        )
        # if QT_CONFIG(tooltip)
        self.dni_lineEdit.setToolTip(
            QCoreApplication.translate("clientes_edit", "DNI del/la cliente/a", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.fecha_dateEdit.setToolTip(
            QCoreApplication.translate("clientes_edit", "Fecha de nacimiento", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.fecha_label.setToolTip(
            QCoreApplication.translate("clientes_edit", "Fecha del evento", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.fecha_label.setText(
            QCoreApplication.translate("clientes_edit", "Fecha Nacimiento", None)
        )
        # if QT_CONFIG(tooltip)
        self.pais_lineEdit.setToolTip(
            QCoreApplication.translate("clientes_edit", "Pa\u00eds de origen", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.pasi_label.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pasi_label.setText(
            QCoreApplication.translate("clientes_edit", "Pais", None)
        )
        # if QT_CONFIG(tooltip)
        self.telefono_label.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.telefono_label.setText(
            QCoreApplication.translate("clientes_edit", "Telefono", None)
        )
        # if QT_CONFIG(tooltip)
        self.telefono_lineEdit.setToolTip(
            QCoreApplication.translate(
                "clientes_edit", "Telefono del/la cliente/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.mail_label.setToolTip(
            QCoreApplication.translate("clientes_edit", "Fecha del evento", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.mail_label.setText(
            QCoreApplication.translate("clientes_edit", "Email", None)
        )
        # if QT_CONFIG(tooltip)
        self.mail_lineEdit.setToolTip(
            QCoreApplication.translate("clientes_edit", "Email del/la cliente/a", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.menores_label.setText(
            QCoreApplication.translate(
                "clientes_edit", "\u00bfse ospeda con menores?", None
            )
        )
        self.menores_checkBox.setText("")
        # if QT_CONFIG(tooltip)
        self.sex_label.setToolTip(
            QCoreApplication.translate("clientes_edit", "Fecha del evento", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.sex_label.setText(
            QCoreApplication.translate("clientes_edit", "Sexo:", None)
        )
        self.boton_izquierdo_pushButton.setText(
            QCoreApplication.translate("clientes_edit", "boton2", None)
        )
        self.boton_derecho_pushButton.setText(
            QCoreApplication.translate("clientes_edit", "boton2", None)
        )

    # retranslateUi

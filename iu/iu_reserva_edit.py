# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_reserva_edit.ui'
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
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QWidget,
)


class Ui_reserva_edit(object):
    def setupUi(self, reserva_edit):
        if not reserva_edit.objectName():
            reserva_edit.setObjectName("reserva_edit")
        reserva_edit.resize(490, 728)
        reserva_edit.setMinimumSize(QSize(490, 728))
        reserva_edit.setMaximumSize(QSize(490, 728))
        reserva_edit.setStyleSheet(
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
        self.title_label = QLabel(reserva_edit)
        self.title_label.setObjectName("title_label")
        self.title_label.setGeometry(QRect(0, 10, 481, 31))
        self.title_label.setStyleSheet(
            "QLabel {\n"
            "    font-size: 24px;\n"
            "    font-weight: bold;\n"
            "    color: #BB86FC;\n"
            "    text-transform: uppercase;\n"
            "    letter-spacing: 1.5px;\n"
            "    qproperty-alignment: AlignCenter;\n"
            "}"
        )
        self.widget_2 = QWidget(reserva_edit)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setGeometry(QRect(10, 40, 471, 681))
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_oculto = QWidget(self.widget_2)
        self.widget_oculto.setObjectName("widget_oculto")
        self.gridLayout_2 = QGridLayout(self.widget_oculto)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_jornadas = QWidget(self.widget_oculto)
        self.widget_jornadas.setObjectName("widget_jornadas")
        self.gridLayout_7 = QGridLayout(self.widget_jornadas)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.jornadas_spinBox = QSpinBox(self.widget_jornadas)
        self.jornadas_spinBox.setObjectName("jornadas_spinBox")

        self.gridLayout_7.addWidget(self.jornadas_spinBox, 0, 1, 1, 1)

        self.jornadas_label = QLabel(self.widget_jornadas)
        self.jornadas_label.setObjectName("jornadas_label")
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setBold(True)
        self.jornadas_label.setFont(font)

        self.gridLayout_7.addWidget(self.jornadas_label, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget_jornadas, 0, 0, 1, 1)

        self.widget_habitaciones = QWidget(self.widget_oculto)
        self.widget_habitaciones.setObjectName("widget_habitaciones")
        self.gridLayout_8 = QGridLayout(self.widget_habitaciones)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.habitaciones_checkBox = QCheckBox(self.widget_habitaciones)
        self.habitaciones_checkBox.setObjectName("habitaciones_checkBox")

        self.gridLayout_8.addWidget(self.habitaciones_checkBox, 0, 1, 1, 1)

        self.habitaciones_label = QLabel(self.widget_habitaciones)
        self.habitaciones_label.setObjectName("habitaciones_label")
        self.habitaciones_label.setFont(font)

        self.gridLayout_8.addWidget(self.habitaciones_label, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget_habitaciones, 0, 1, 1, 1)

        self.gridLayout_3.addWidget(self.widget_oculto, 1, 0, 1, 1)

        self.widget_botones = QWidget(self.widget_2)
        self.widget_botones.setObjectName("widget_botones")
        self.gridLayout_6 = QGridLayout(self.widget_botones)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.boton_izquierdo_pushButton = QPushButton(self.widget_botones)
        self.boton_izquierdo_pushButton.setObjectName("boton_izquierdo_pushButton")

        self.gridLayout_6.addWidget(self.boton_izquierdo_pushButton, 0, 0, 1, 1)

        self.boton_derecho_pushButton = QPushButton(self.widget_botones)
        self.boton_derecho_pushButton.setObjectName("boton_derecho_pushButton")

        self.gridLayout_6.addWidget(self.boton_derecho_pushButton, 0, 1, 1, 1)

        self.gridLayout_3.addWidget(self.widget_botones, 2, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.tipo_reserva_comboBox = QComboBox(self.widget)
        self.tipo_reserva_comboBox.setObjectName("tipo_reserva_comboBox")

        self.gridLayout.addWidget(self.tipo_reserva_comboBox, 8, 0, 1, 2)

        self.tipo_reserva_label = QLabel(self.widget)
        self.tipo_reserva_label.setObjectName("tipo_reserva_label")
        self.tipo_reserva_label.setFont(font)

        self.gridLayout.addWidget(self.tipo_reserva_label, 7, 0, 1, 2)

        self.cliente_comboBox = QComboBox(self.widget)
        self.cliente_comboBox.setObjectName("cliente_comboBox")

        self.gridLayout.addWidget(self.cliente_comboBox, 2, 0, 1, 2)

        self.asistentes_label = QLabel(self.widget)
        self.asistentes_label.setObjectName("asistentes_label")
        self.asistentes_label.setFont(font)

        self.gridLayout.addWidget(self.asistentes_label, 11, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(
            372, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout.addItem(self.horizontalSpacer, 12, 1, 1, 1)

        self.tipo_cocina_label = QLabel(self.widget)
        self.tipo_cocina_label.setObjectName("tipo_cocina_label")
        self.tipo_cocina_label.setFont(font)

        self.gridLayout.addWidget(self.tipo_cocina_label, 9, 0, 1, 2)

        self.telefono_label = QLabel(self.widget)
        self.telefono_label.setObjectName("telefono_label")
        self.telefono_label.setFont(font)

        self.gridLayout.addWidget(self.telefono_label, 5, 0, 1, 2)

        self.tipo_cocina_comboBox = QComboBox(self.widget)
        self.tipo_cocina_comboBox.setObjectName("tipo_cocina_comboBox")

        self.gridLayout.addWidget(self.tipo_cocina_comboBox, 10, 0, 1, 2)

        self.salon_comboBox = QComboBox(self.widget)
        self.salon_comboBox.setObjectName("salon_comboBox")

        self.gridLayout.addWidget(self.salon_comboBox, 6, 0, 1, 2)

        self.fecha_dateEdit = QDateEdit(self.widget)
        self.fecha_dateEdit.setObjectName("fecha_dateEdit")
        font1 = QFont()
        font1.setFamilies(["Roboto"])
        self.fecha_dateEdit.setFont(font1)

        self.gridLayout.addWidget(self.fecha_dateEdit, 4, 0, 1, 2)

        self.asistentes_spinBox = QSpinBox(self.widget)
        self.asistentes_spinBox.setObjectName("asistentes_spinBox")

        self.gridLayout.addWidget(self.asistentes_spinBox, 12, 0, 1, 1)

        self.fecha_label = QLabel(self.widget)
        self.fecha_label.setObjectName("fecha_label")
        self.fecha_label.setFont(font)

        self.gridLayout.addWidget(self.fecha_label, 3, 0, 1, 2)

        self.nombre_label = QLabel(self.widget)
        self.nombre_label.setObjectName("nombre_label")
        self.nombre_label.setFont(font)

        self.gridLayout.addWidget(self.nombre_label, 1, 0, 1, 1)

        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(reserva_edit)

        QMetaObject.connectSlotsByName(reserva_edit)

    # setupUi

    def retranslateUi(self, reserva_edit):
        reserva_edit.setWindowTitle(
            QCoreApplication.translate("reserva_edit", "Form", None)
        )
        self.title_label.setText(
            QCoreApplication.translate("reserva_edit", "TextLabel", None)
        )
        # if QT_CONFIG(tooltip)
        self.jornadas_label.setToolTip(
            QCoreApplication.translate("reserva_edit", "Fecha del evento", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.jornadas_label.setText(
            QCoreApplication.translate("reserva_edit", "Jornadas:", None)
        )
        self.habitaciones_checkBox.setText("")
        self.habitaciones_label.setText(
            QCoreApplication.translate("reserva_edit", "\u00bfHabitaciones?", None)
        )
        self.boton_izquierdo_pushButton.setText(
            QCoreApplication.translate("reserva_edit", "boton2", None)
        )
        self.boton_derecho_pushButton.setText(
            QCoreApplication.translate("reserva_edit", "boton2", None)
        )
        # if QT_CONFIG(tooltip)
        self.tipo_reserva_label.setToolTip(
            QCoreApplication.translate(
                "reserva_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tipo_reserva_label.setText(
            QCoreApplication.translate("reserva_edit", "Tipo reserva", None)
        )
        # if QT_CONFIG(tooltip)
        self.asistentes_label.setToolTip(
            QCoreApplication.translate(
                "reserva_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.asistentes_label.setText(
            QCoreApplication.translate("reserva_edit", "Asistentes", None)
        )
        # if QT_CONFIG(tooltip)
        self.tipo_cocina_label.setToolTip(
            QCoreApplication.translate(
                "reserva_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.tipo_cocina_label.setText(
            QCoreApplication.translate("reserva_edit", "Tipo cocina", None)
        )
        # if QT_CONFIG(tooltip)
        self.telefono_label.setToolTip(
            QCoreApplication.translate(
                "reserva_edit", "Tel\u00e9fono del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.telefono_label.setText(
            QCoreApplication.translate("reserva_edit", "Salon", None)
        )
        # if QT_CONFIG(tooltip)
        self.fecha_dateEdit.setToolTip(
            QCoreApplication.translate("reserva_edit", "Fecha de nacimiento", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.fecha_label.setToolTip(
            QCoreApplication.translate("reserva_edit", "Fecha del evento", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.fecha_label.setText(
            QCoreApplication.translate("reserva_edit", "Fecha ", None)
        )
        # if QT_CONFIG(tooltip)
        self.nombre_label.setToolTip(
            QCoreApplication.translate(
                "reserva_edit", "Nombre del/la organizador/a", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.nombre_label.setText(
            QCoreApplication.translate("reserva_edit", "Cliente:", None)
        )

    # retranslateUi

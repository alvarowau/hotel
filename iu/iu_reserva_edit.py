# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'iu_reserva_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_reserva_edit(object):
    def setupUi(self, reserva_edit):
        if not reserva_edit.objectName():
            reserva_edit.setObjectName(u"reserva_edit")
        reserva_edit.resize(541, 729)
        reserva_edit.setMinimumSize(QSize(541, 729))
        reserva_edit.setMaximumSize(QSize(541, 729))
        reserva_edit.setStyleSheet(u"QWidget {\n"
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
"}")
        self.widget_2 = QWidget(reserva_edit)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 60, 521, 661))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_principal = QWidget(self.widget_2)
        self.widget_principal.setObjectName(u"widget_principal")
        self.verticalLayout = QVBoxLayout(self.widget_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nombre_label = QLabel(self.widget_principal)
        self.nombre_label.setObjectName(u"nombre_label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setBold(True)
        self.nombre_label.setFont(font)

        self.verticalLayout.addWidget(self.nombre_label)

        self.nombre_lineEdit = QLineEdit(self.widget_principal)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        self.nombre_lineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.nombre_lineEdit)

        self.fecha_label = QLabel(self.widget_principal)
        self.fecha_label.setObjectName(u"fecha_label")
        self.fecha_label.setFont(font)

        self.verticalLayout.addWidget(self.fecha_label)

        self.fecha_dateEdit = QDateEdit(self.widget_principal)
        self.fecha_dateEdit.setObjectName(u"fecha_dateEdit")
        self.fecha_dateEdit.setFont(font1)

        self.verticalLayout.addWidget(self.fecha_dateEdit)

        self.telefono_label = QLabel(self.widget_principal)
        self.telefono_label.setObjectName(u"telefono_label")
        self.telefono_label.setFont(font)

        self.verticalLayout.addWidget(self.telefono_label)

        self.telefono_lineEdit = QLineEdit(self.widget_principal)
        self.telefono_lineEdit.setObjectName(u"telefono_lineEdit")
        self.telefono_lineEdit.setEnabled(True)
        self.telefono_lineEdit.setFont(font1)

        self.verticalLayout.addWidget(self.telefono_lineEdit)

        self.tipo_reserva_label = QLabel(self.widget_principal)
        self.tipo_reserva_label.setObjectName(u"tipo_reserva_label")
        self.tipo_reserva_label.setFont(font)

        self.verticalLayout.addWidget(self.tipo_reserva_label)

        self.tipo_reserva_comboBox = QComboBox(self.widget_principal)
        self.tipo_reserva_comboBox.setObjectName(u"tipo_reserva_comboBox")

        self.verticalLayout.addWidget(self.tipo_reserva_comboBox)

        self.tipo_cocina_label = QLabel(self.widget_principal)
        self.tipo_cocina_label.setObjectName(u"tipo_cocina_label")
        self.tipo_cocina_label.setFont(font)

        self.verticalLayout.addWidget(self.tipo_cocina_label)

        self.tipo_cocina_comboBox = QComboBox(self.widget_principal)
        self.tipo_cocina_comboBox.setObjectName(u"tipo_cocina_comboBox")

        self.verticalLayout.addWidget(self.tipo_cocina_comboBox)

        self.asistentes_label = QLabel(self.widget_principal)
        self.asistentes_label.setObjectName(u"asistentes_label")
        self.asistentes_label.setFont(font)

        self.verticalLayout.addWidget(self.asistentes_label)

        self.asistentes_spinBox = QSpinBox(self.widget_principal)
        self.asistentes_spinBox.setObjectName(u"asistentes_spinBox")

        self.verticalLayout.addWidget(self.asistentes_spinBox)

        self.horizontalSpacer = QSpacerItem(482, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.widget_principal, 0, 0, 1, 1)

        self.widget_botones = QWidget(self.widget_2)
        self.widget_botones.setObjectName(u"widget_botones")
        self.gridLayout_6 = QGridLayout(self.widget_botones)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.boton_izquierdo_pushButton = QPushButton(self.widget_botones)
        self.boton_izquierdo_pushButton.setObjectName(u"boton_izquierdo_pushButton")

        self.gridLayout_6.addWidget(self.boton_izquierdo_pushButton, 0, 0, 1, 1)

        self.boton_derecho_pushButton = QPushButton(self.widget_botones)
        self.boton_derecho_pushButton.setObjectName(u"boton_derecho_pushButton")

        self.gridLayout_6.addWidget(self.boton_derecho_pushButton, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_botones, 2, 0, 1, 1)

        self.widget_secundario = QWidget(self.widget_2)
        self.widget_secundario.setObjectName(u"widget_secundario")
        self.horizontalLayout = QHBoxLayout(self.widget_secundario)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_jornadas = QWidget(self.widget_secundario)
        self.widget_jornadas.setObjectName(u"widget_jornadas")
        self.gridLayout_7 = QGridLayout(self.widget_jornadas)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.jornadas_spinBox = QSpinBox(self.widget_jornadas)
        self.jornadas_spinBox.setObjectName(u"jornadas_spinBox")

        self.gridLayout_7.addWidget(self.jornadas_spinBox, 0, 1, 1, 1)

        self.jornadas_label = QLabel(self.widget_jornadas)
        self.jornadas_label.setObjectName(u"jornadas_label")
        self.jornadas_label.setFont(font)

        self.gridLayout_7.addWidget(self.jornadas_label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_jornadas)

        self.widget_habitaciones = QWidget(self.widget_secundario)
        self.widget_habitaciones.setObjectName(u"widget_habitaciones")
        self.gridLayout_8 = QGridLayout(self.widget_habitaciones)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.habitaciones_label = QLabel(self.widget_habitaciones)
        self.habitaciones_label.setObjectName(u"habitaciones_label")
        self.habitaciones_label.setFont(font)

        self.gridLayout_8.addWidget(self.habitaciones_label, 0, 0, 1, 1)

        self.habitaciones_checkBox = QCheckBox(self.widget_habitaciones)
        self.habitaciones_checkBox.setObjectName(u"habitaciones_checkBox")

        self.gridLayout_8.addWidget(self.habitaciones_checkBox, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_habitaciones)


        self.gridLayout.addWidget(self.widget_secundario, 1, 0, 1, 1)

        self.label = QLabel(reserva_edit)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 521, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #BB86FC;\n"
"    text-transform: uppercase;\n"
"    letter-spacing: 1.5px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}")

        self.retranslateUi(reserva_edit)

        QMetaObject.connectSlotsByName(reserva_edit)
    # setupUi

    def retranslateUi(self, reserva_edit):
        reserva_edit.setWindowTitle(QCoreApplication.translate("reserva_edit", u"Form", None))
#if QT_CONFIG(tooltip)
        self.nombre_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.nombre_label.setText(QCoreApplication.translate("reserva_edit", u"Nombre", None))
#if QT_CONFIG(tooltip)
        self.nombre_lineEdit.setToolTip(QCoreApplication.translate("reserva_edit", u"Nombre del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fecha_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
        self.fecha_label.setText(QCoreApplication.translate("reserva_edit", u"Fecha ", None))
#if QT_CONFIG(tooltip)
        self.fecha_dateEdit.setToolTip(QCoreApplication.translate("reserva_edit", u"Fecha de nacimiento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.telefono_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.telefono_label.setText(QCoreApplication.translate("reserva_edit", u"Telefono", None))
#if QT_CONFIG(tooltip)
        self.telefono_lineEdit.setToolTip(QCoreApplication.translate("reserva_edit", u"Telefono del/la cliente/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tipo_reserva_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.tipo_reserva_label.setText(QCoreApplication.translate("reserva_edit", u"Tipo reserva", None))
#if QT_CONFIG(tooltip)
        self.tipo_cocina_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.tipo_cocina_label.setText(QCoreApplication.translate("reserva_edit", u"Tipo cocina", None))
#if QT_CONFIG(tooltip)
        self.asistentes_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.asistentes_label.setText(QCoreApplication.translate("reserva_edit", u"Asistentes", None))
        self.boton_izquierdo_pushButton.setText(QCoreApplication.translate("reserva_edit", u"boton2", None))
        self.boton_derecho_pushButton.setText(QCoreApplication.translate("reserva_edit", u"boton2", None))
#if QT_CONFIG(tooltip)
        self.jornadas_label.setToolTip(QCoreApplication.translate("reserva_edit", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
        self.jornadas_label.setText(QCoreApplication.translate("reserva_edit", u"Jornadas:", None))
        self.habitaciones_label.setText(QCoreApplication.translate("reserva_edit", u"\u00bfHabitaciones?", None))
        self.habitaciones_checkBox.setText("")
        self.label.setText(QCoreApplication.translate("reserva_edit", u"TextLabel", None))
    # retranslateUi


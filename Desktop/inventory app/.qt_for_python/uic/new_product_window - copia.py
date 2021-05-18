# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_product_window - copia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_newProductWindow(object):
    def setupUi(self, newProductWindow):
        if not newProductWindow.objectName():
            newProductWindow.setObjectName(u"newProductWindow")
        newProductWindow.resize(405, 472)
        self.label = QLabel(newProductWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newProductWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.nameLineEdit = QLineEdit(newProductWindow)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(newProductWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.loteLineEdit = QLineEdit(newProductWindow)
        self.loteLineEdit.setObjectName(u"loteLineEdit")
        self.loteLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(newProductWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 61, 13))
        self.proveedorLineEdit = QLineEdit(newProductWindow)
        self.proveedorLineEdit.setObjectName(u"proveedorLineEdit")
        self.proveedorLineEdit.setGeometry(QRect(30, 180, 271, 20))
        self.activoCheckBox = QCheckBox(newProductWindow)
        self.activoCheckBox.setObjectName(u"activoCheckBox")
        self.activoCheckBox.setGeometry(QRect(30, 220, 67, 18))
        self.activoCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.saborCheckBox = QCheckBox(newProductWindow)
        self.saborCheckBox.setObjectName(u"saborCheckBox")
        self.saborCheckBox.setGeometry(QRect(30, 240, 161, 18))
        self.saborCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.excipienteCheckBox = QCheckBox(newProductWindow)
        self.excipienteCheckBox.setObjectName(u"excipienteCheckBox")
        self.excipienteCheckBox.setGeometry(QRect(30, 260, 81, 18))
        self.excipienteCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.label_5 = QLabel(newProductWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 290, 131, 16))
        self.descriptionTextEdit = QTextEdit(newProductWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(30, 310, 351, 111))
        self.addButton = QPushButton(newProductWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(94, 430, 101, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/69943.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.cancelButton = QPushButton(newProductWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(210, 430, 101, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")

        self.retranslateUi(newProductWindow)

        QMetaObject.connectSlotsByName(newProductWindow)
    # setupUi

    def retranslateUi(self, newProductWindow):
        newProductWindow.setWindowTitle(QCoreApplication.translate("newProductWindow", u"Nuevo Producto", None))
        self.label.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Nuevo Producto</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Producto</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Lote</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Proveedor</span></p></body></html>", None))
        self.activoCheckBox.setText(QCoreApplication.translate("newProductWindow", u"Activo", None))
        self.saborCheckBox.setText(QCoreApplication.translate("newProductWindow", u"Saborizante y Endulcorante", None))
        self.excipienteCheckBox.setText(QCoreApplication.translate("newProductWindow", u"Excipiente", None))
        self.label_5.setText(QCoreApplication.translate("newProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descripcion Producto</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("newProductWindow", u"AGREGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("newProductWindow", u"CANCELAR", None))
    # retranslateUi


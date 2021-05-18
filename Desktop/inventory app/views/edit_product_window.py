# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class editProductForm(object):
    def setupUi(self, editProductWindow):
        if not editProductWindow.objectName():
            editProductWindow.setObjectName(u"editProductWindow")
        editProductWindow.resize(405, 472)
        self.label = QLabel(editProductWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(editProductWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.nameLineEdit = QLineEdit(editProductWindow)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(editProductWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.loteLineEdit = QLineEdit(editProductWindow)
        self.loteLineEdit.setObjectName(u"loteLineEdit")
        self.loteLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(editProductWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 61, 13))
        self.proveedorLineEdit = QLineEdit(editProductWindow)
        self.proveedorLineEdit.setObjectName(u"proveedorLineEdit")
        self.proveedorLineEdit.setGeometry(QRect(30, 180, 271, 20))
        self.activoCheckBox = QCheckBox(editProductWindow)
        self.activoCheckBox.setObjectName(u"activoCheckBox")
        self.activoCheckBox.setGeometry(QRect(30, 220, 67, 18))
        self.activoCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.saborCheckBox = QCheckBox(editProductWindow)
        self.saborCheckBox.setObjectName(u"saborCheckBox")
        self.saborCheckBox.setGeometry(QRect(30, 240, 161, 18))
        self.saborCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.excipienteCheckBox = QCheckBox(editProductWindow)
        self.excipienteCheckBox.setObjectName(u"excipienteCheckBox")
        self.excipienteCheckBox.setGeometry(QRect(30, 260, 81, 18))
        self.excipienteCheckBox.setStyleSheet(u"Activo\n"
"font: 75 11pt \"Arial\";")
        self.label_5 = QLabel(editProductWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 290, 131, 16))
        self.descriptionTextEdit = QTextEdit(editProductWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(30, 310, 351, 111))
        self.addButton = QPushButton(editProductWindow)
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
        icon.addFile(u"../assets/icons/edit-product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(20, 20))
        self.cancelButton = QPushButton(editProductWindow)
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

        self.retranslateUi(editProductWindow)

        QMetaObject.connectSlotsByName(editProductWindow)
    # setupUi

    def retranslateUi(self, editProductWindow):
        editProductWindow.setWindowTitle(QCoreApplication.translate("editProductWindow", u"Editar Producto", None))
        self.label.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDITAR PRODUCTO</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Producto</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Lote</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Proveedor</span></p></body></html>", None))
        self.activoCheckBox.setText(QCoreApplication.translate("editProductWindow", u"Activo", None))
        self.saborCheckBox.setText(QCoreApplication.translate("editProductWindow", u"Saborizante y Endulcorante", None))
        self.excipienteCheckBox.setText(QCoreApplication.translate("editProductWindow", u"Excipiente", None))
        self.label_5.setText(QCoreApplication.translate("editProductWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Descripcion Producto</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("editProductWindow", u"EDITAR", None))
        self.cancelButton.setText(QCoreApplication.translate("editProductWindow", u"CANCELAR", None))
    # retranslateUi


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListProductForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(961, 550)
        self.buttonsFrame = QFrame(Form)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setGeometry(QRect(10, 10, 961, 91))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.open_Product_Button = QPushButton(self.buttonsFrame)
        self.open_Product_Button.setObjectName(u"open_Product_Button")
        self.open_Product_Button.setGeometry(QRect(20, 10, 71, 51))
        self.open_Product_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_Product_Button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../assets/icons/123-512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_Product_Button.setIcon(icon)
        self.open_Product_Button.setIconSize(QSize(50, 50))
        self.open_Product_Button.setFlat(True)
        self.label = QLabel(self.buttonsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 91, 21))
        self.label_2 = QLabel(self.buttonsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 91, 21))
        self.open_new_window = QPushButton(self.buttonsFrame)
        self.open_new_window.setObjectName(u"open_new_window")
        self.open_new_window.setGeometry(QRect(110, 10, 71, 51))
        self.open_new_window.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_window.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/69943.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_window.setIcon(icon1)
        self.open_new_window.setIconSize(QSize(49, 44))
        self.open_new_window.setFlat(True)
        self.label_3 = QLabel(self.buttonsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 60, 91, 21))
        self.open_edit_button = QPushButton(self.buttonsFrame)
        self.open_edit_button.setObjectName(u"open_edit_button")
        self.open_edit_button.setGeometry(QRect(220, 10, 71, 51))
        self.open_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_edit_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/edit-product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_edit_button.setIcon(icon2)
        self.open_edit_button.setIconSize(QSize(60, 48))
        self.open_edit_button.setFlat(True)
        self.label_4 = QLabel(self.buttonsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 60, 111, 21))
        self.open_edit_button_2 = QPushButton(self.buttonsFrame)
        self.open_edit_button_2.setObjectName(u"open_edit_button_2")
        self.open_edit_button_2.setGeometry(QRect(340, 10, 71, 51))
        self.open_edit_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_edit_button_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/57480.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_edit_button_2.setIcon(icon3)
        self.open_edit_button_2.setIconSize(QSize(60, 60))
        self.open_edit_button_2.setFlat(True)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(941, 41, 120, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 941, 120, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 110, 941, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 71, 16))
        self.searchBycomboBox = QComboBox(self.frame_3)
        self.searchBycomboBox.setObjectName(u"searchBycomboBox")
        self.searchBycomboBox.setGeometry(QRect(70, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame_3)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.searchButton = QPushButton(self.frame_3)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/search-512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshButton = QPushButton(self.frame_3)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(800, 10, 131, 25))
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/61444.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon5)
        self.listProductTable = QTableWidget(Form)
        self.listProductTable.setObjectName(u"listProductTable")
        self.listProductTable.setGeometry(QRect(20, 160, 941, 341))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 510, 121, 16))
        self.productQtyLabel = QLabel(Form)
        self.productQtyLabel.setObjectName(u"productQtyLabel")
        self.productQtyLabel.setGeometry(QRect(150, 510, 47, 14))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"ListProduct", None))
        self.open_Product_Button.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Abrir Lista </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Producto</span></p></body></html>", None))
        self.open_new_window.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Editar Producto</span></p></body></html>", None))
        self.open_edit_button.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Producto</span></p></body></html>", None))
        self.open_edit_button_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Buscar por:", None))
        self.searchButton.setText(QCoreApplication.translate("Form", u"BUSCAR", None))
        self.refreshButton.setText(QCoreApplication.translate("Form", u"ACTUALIZAR", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad productos:</span></p></body></html>", None))
        self.productQtyLabel.setText(QCoreApplication.translate("Form", u"#", None))
    # retranslateUi


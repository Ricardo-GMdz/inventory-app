from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from views.edit_product_window import editProductForm

class EditProductWindow(QtWidgets, editProductForm):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def populate_inputs(self):
        pass

    def checks_inputs(self):
        pass

    def edit_product(self):
        pass
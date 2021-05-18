from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from views.new_product_window import newProductForm

class newProductWindow(QtWidgets, newProductForm):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

    def check_inputs(self):
        pass

    def add_product(self):
        pass

    def clean_inputs(self):
        pass

    def undo(self):
        pass
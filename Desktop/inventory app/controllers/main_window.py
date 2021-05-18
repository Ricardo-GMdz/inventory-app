from PySide2.QtWidgets import QWidget
from views.main_window import ListProductForm

class ListProductWindow(QWidget, ListProductForm):
    
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.open_new_window.clicked.connect(self.open_new_product_window)

    def open_new_product_window(self):
        from controllers.new_product_window import newProductWindow
        window = newProductWindow(self)
        window.show()

    def open_edit_new_window(self):
        pass

    def remove_product(self):
        pass

    def populate_table(self):
        pass

    def populate_combobox(self):
        pass

    def search_product_by_title(self):
        pass

    def search_product_by_lote(self):
        pass
    
    def search_product_by_proveedor(self):
        pass

    def search(self):
        pass

    def records_qty(self):
        pass

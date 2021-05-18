from PySide2.QtWidgets import QApplication
from controllers.main_window import ListProductWindow

if __name__ == "__main__":
    app = QApplication()
    window = ListProductWindow()
    window.show()

    app.exec_()
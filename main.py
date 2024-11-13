import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton)


class Roamify(QWidget):
    def __init__(self):
        super().__init__()
        pass

#Show/Run our App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())
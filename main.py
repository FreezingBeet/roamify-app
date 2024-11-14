import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCalendarWidget, QVBoxLayout
from PyQt5.QtCore import QDate


class Roamify(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roamify")
        self.resize(400, 350)  # Adjusted height to fit the new input field
        self.current_theme = "light"  # Start with light theme
        self.initUI()

    def initUI(self):
        self.app_name = QLabel("Roamify", self)
        self.app_name.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Add "From" input
        self.from_location = QLineEdit(self)
        self.from_location.setPlaceholderText("From")

        # Add "To" input
        self.location = QLineEdit(self)
        self.location.setPlaceholderText("To")

        self.date_label = QLabel(QDate.currentDate().toString("dd-MM-yyyy"), self)

        self.calendar = QCalendarWidget(self)
        self.calendar.setMaximumHeight(150)
        self.calendar.selectionChanged.connect(self.update_date_label)

        self.submit_btn = QPushButton("Submit", self)

        self.theme_btn = QPushButton("Switch to Dark Theme", self)
        self.theme_btn.clicked.connect(self.toggle_theme)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.app_name)
        layout.addWidget(self.from_location)
        layout.addWidget(self.location)
        layout.addWidget(self.date_label)
        layout.addWidget(self.calendar)
        layout.addWidget(self.submit_btn)
        layout.addWidget(self.theme_btn)
        self.setLayout(layout)

        self.apply_theme(self.current_theme)

    def update_date_label(self):
        self.date_label.setText(self.calendar.selectedDate().toString("dd-MM-yyyy"))

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.theme_btn.setText("Switch to Light Theme")
        else:
            self.current_theme = "light"
            self.theme_btn.setText("Switch to Dark Theme")
        self.apply_theme(self.current_theme)

    def apply_theme(self, theme):
        if theme == "dark":
            self.setStyleSheet("""
                QWidget { background-color: #121212; color: #FFFFFF; }
                QLineEdit { background-color: #444444; color: #FFFFFF; border: 1px solid #888888; }
                QPushButton { background-color: #007BFF; color: white; border-radius: 5px; }
                QPushButton:hover { background-color: #0056b3; }
                QCalendarWidget { background-color: #222222; color: #FFFFFF; border: none; }
            """)
        else:
            self.setStyleSheet("""
                QWidget { background-color: #F8F8F8; color: #000000; }
                QLineEdit { background-color: #FFFFFF; color: #000000; border: 1px solid #CCCCCC; }
                QPushButton { background-color: #007BFF; color: white; border-radius: 5px; }
                QPushButton:hover { background-color: #0056b3; }
                QCalendarWidget { background-color: #FFFFFF; color: #000000; border: none; }
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())

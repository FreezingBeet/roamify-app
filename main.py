import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCalendarWidget, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QDate, Qt


class Roamify(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roamify")
        self.resize(800, 600)

        self.initUI()

    def initUI(self):
        # Create all App Objects

        self.app_name = QLabel("Roamify")    # Will later add an image with Roamify written on it stylistically and the same bg color as that of the app

        self.location = QLineEdit()
        self.location.setPlaceholderText("Enter Location")

        self.date_label = QLabel()
        self.date_label.setObjectName("date_label")
        self.submit_btn = QPushButton("Submit")

        self.app_name.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(QDate.currentDate())    # Have to add a Minimum and Maximum date range that can be selected
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.date_label.setText(QDate.currentDate().toString("yyyy-MM-dd"))

        #All Design Here

        master_layout = QVBoxLayout()
        master_layout.setContentsMargins(100, 20, 100, 20)
        master_layout.setSpacing(10)

        self.submit_btn.setFixedWidth(400)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.submit_btn)
        button_layout.addStretch()

        master_layout.addWidget(self.app_name)
        master_layout.addSpacing(50)
        master_layout.addWidget(self.location)
        master_layout.addSpacing(40)
        master_layout.addWidget(self.date_label)
        master_layout.addSpacing(5)
        master_layout.addWidget(self.calendar)
        master_layout.addSpacing(30)
        master_layout.addLayout(button_layout)

        self.setLayout(master_layout)
        self.app_name.setFixedHeight(int(self.height() * 0.2))

        self.setStyleSheet("""
                            QLineEdit
                           {
                              background-color: #444444;
                              color: #ffffff;
                              padding: 20px;
                              font-weight: bold;
                              font-size: 30px;
                           }
                           #date_label
                           {
                              background-color: #444444;
                              color: #ffffff;
                              font-size: 20px;
                              font-weight: bold;
                              padding: 20px;
                              border: 1px solid;
                              border-radius: 5px;
                           }
                           QCalendarWidget
                           {
                              font-size: 25px;
                           }
                           QPushButton
                           {
                              background-color: #007BFF;   /* Blue background */
                              color: white;               /* White text */
                              border-radius: 10px;        /* Rounded corners */
                              font-size: 20px;            /* Font size */
                              padding: 15px 10px;         /* Padding for size */
                              font-weight: bold;
                              font-family: Arial Black;
                           }

                            QPushButton:hover{background-color: #0056b3;}
                            QPushButton:pressed{background-color: #003f7f;}
""")

        pass




#Show/Run our App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCalendarWidget, QVBoxLayout)
from PyQt5.QtCore import QDate


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
        self.date_label = QLabel()
        self.submit_btn = QPushButton("Submit")

        # Style the Submit Button
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;   /* Blue background */
                color: white;               /* White text */
                border-radius: 10px;        /* Rounded corners */
                font-size: 16px;            /* Font size */
                padding: 10px 20px;         /* Padding for size */
            }
            QPushButton:hover {
                background-color: #0056b3;  /* Darker blue on hover */
            }
            QPushButton:pressed {
                background-color: #003f7f;  /* Even darker blue on press */
            }
        """)

        self.calendar = QCalendarWidget()

        # Set date range: current date to one year later
        current_date = QDate.currentDate()
        one_year_later = current_date.addYears(1)
        self.calendar.setMinimumDate(current_date)
        self.calendar.setMaximumDate(one_year_later)

        # Set the initial selected date to today's date
        self.calendar.setSelectedDate(current_date)
        self.date_label.setText(current_date.toString("yyyy-MM-dd"))

        # Update label when date is changed
        self.calendar.selectionChanged.connect(self.update_date_label)

        # All Design Here
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.app_name)
        master_layout.addWidget(self.location)
        master_layout.addWidget(self.date_label)
        master_layout.addWidget(self.calendar)
        master_layout.addWidget(self.submit_btn)

        self.setLayout(master_layout)

    def update_date_label(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(selected_date.toString("yyyy-MM-dd"))


# Show/Run our App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())

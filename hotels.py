import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QCalendarWidget, QVBoxLayout, QHBoxLayout, QSpinBox, QMessageBox
)
from PyQt5.QtCore import QDate


class BookingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Booking App")
        self.resize(800, 600)

        self.initUI()

    def initUI(self):
        # Set background color and styles
        self.setStyleSheet(""" 
            QWidget {
                background-color: hsl(10, 47%, 40%);
            }
            QLineEdit, QSpinBox {
                background-color: hsl(35, 90%, 81%);
                color: black;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #000;
                border-radius: 5px;
                text-align: center;
            }
            QLabel {
                color: hsl(35, 90%, 81%);
                font-size: 18px;
                font-weight: bold;
                font-family: "Arial";
                cursor: pointer;
            }
        """)

        # Create widgets for Check In and Check Out
        self.check_in_label = QLabel("Check In", self)
        self.check_in_label.mousePressEvent = lambda event: self.show_calendar("check_in")

        self.check_in_date = QLineEdit(self)
        self.check_in_date.setPlaceholderText("Select Check In Date")
        self.check_in_date.setReadOnly(True)

        self.check_out_label = QLabel("Check Out", self)
        self.check_out_label.mousePressEvent = lambda event: self.show_calendar("check_out")

        self.check_out_date = QLineEdit(self)
        self.check_out_date.setPlaceholderText("Select Check Out Date")
        self.check_out_date.setReadOnly(True)

        # Create widgets for Adults and Children
        self.adults_label = QLabel("Adults", self)
        self.adults_spinbox = QSpinBox(self)
        self.adults_spinbox.setMinimum(1)
        self.adults_spinbox.setMaximum(10)

        self.max_price_label = QLabel("Maximum Price", self)
        self.max_price_spinbox = QSpinBox(self)
        self.max_price_spinbox.setMinimum(0)
        self.max_price_spinbox.setMaximum(100000)

        self.children_label = QLabel("Children", self)
        self.children_spinbox = QSpinBox(self)
        self.children_spinbox.setMinimum(0)
        self.children_spinbox.setMaximum(10)

        self.min_price_label = QLabel("Minimum Price", self)
        self.min_price_spinbox = QSpinBox(self)
        self.min_price_spinbox.setMinimum(0)
        self.min_price_spinbox.setMaximum(100000)

        # Calendar Widget
        self.calendar = QCalendarWidget(self)
        self.calendar.hide()
        self.calendar.clicked.connect(self.set_date)

        # Layouts for Check In and Check Out
        check_in_layout = QVBoxLayout()
        check_in_layout.addWidget(self.check_in_label)
        check_in_layout.addWidget(self.check_in_date)
        check_in_layout.addWidget(self.adults_label)
        check_in_layout.addWidget(self.adults_spinbox)
        check_in_layout.addWidget(self.max_price_label)  # Add Maximum Price below Adults
        check_in_layout.addWidget(self.max_price_spinbox)

        check_out_layout = QVBoxLayout()
        check_out_layout.addWidget(self.check_out_label)
        check_out_layout.addWidget(self.check_out_date)
        check_out_layout.addWidget(self.children_label)
        check_out_layout.addWidget(self.children_spinbox)
        check_out_layout.addWidget(self.min_price_label)  # Add Minimum Price below Children
        check_out_layout.addWidget(self.min_price_spinbox)

        # Top layout for both sections
        top_layout = QHBoxLayout()
        top_layout.addLayout(check_in_layout)
        top_layout.addStretch()  # Add spacing
        top_layout.addLayout(check_out_layout)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addStretch()  # Push other elements down
        main_layout.addWidget(self.calendar)

        self.setLayout(main_layout)

    def show_calendar(self, mode):
        """Display the calendar and store the mode (check-in or check-out)."""
        self.calendar.show()
        self.calendar_mode = mode

    def set_date(self):
        """Set the selected date in the respective field."""
        selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        selected_date_obj = self.calendar.selectedDate()

        if self.calendar_mode == "check_in":
            self.check_in_date.setText(selected_date)
            self.check_out_date.clear()  # Clear check-out date to avoid invalid selection
        elif self.calendar_mode == "check_out":
            if self.check_in_date.text():
                check_in_date_obj = QDate.fromString(self.check_in_date.text(), "yyyy-MM-dd")
                if selected_date_obj <= check_in_date_obj:
                    QMessageBox.warning(
                        self,
                        "Invalid Date",
                        "Check Out date must be after Check In date!",
                        QMessageBox.Ok,
                    )
                    return
            self.check_out_date.setText(selected_date)

        self.calendar.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = BookingApp()
    main_window.show()
    sys.exit(app.exec_())

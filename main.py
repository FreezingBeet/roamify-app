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

        self.app_name = QLabel()    # Will later add an image with Roamify written on it stylistically and the same bg color as that of the app

        self.location = QLineEdit()
        self.location.setPlaceholderText("Enter Location")

        self.date_label = QLabel()
        self.date_label.setObjectName("date_label")
        self.submit_btn = QPushButton("Submit")

        self.app_name.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.calendar = QCalendarWidget()
        current_date = QDate.currentDate()
        one_year_later = current_date.addYears(1)
        self.calendar.setMinimumDate(current_date)
        self.calendar.setMaximumDate(one_year_later)

        self.calendar.setSelectedDate(current_date)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.date_label.setText(QDate.currentDate().toString("yyyy-MM-dd"))

        # Update label when date is changed
        self.calendar.selectionChanged.connect(self.update_date_label)

        # All Design Here
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
                         QWidget{background-color: hsl(94, 10%, 86%);}
                         QLineEdit
                         {
                              background-color: hsl(31, 48%, 84%);
                              color: #ffffff;
                              padding: 20px;
                              font-weight: bold;
                              font-size: 30px;
                              border: 1px solid;
                              border-radius: 5px;
                         }
                         #date_label
                         {
                              background-color: hsl(31, 48%, 84%);
                              color: #ffffff;
                              font-size: 20px;
                              font-weight: bold;
                              padding: 20px;
                              border: 1px solid;
                              border-radius: 5px;
                         }
                         QCalendarWidget 
                         {
                              background-color: #f0f8ff;
                              border: 2px solid #007BFF;
                              border-radius: 10px;
                              font-size: 25px;
                         }

                         QCalendarWidget QToolButton
                         {
                              background-color: hsl(35, 60%, 96%);
                              color: black;
                              border-radius: 5px;
                              margin: 5px;
                         }
                         QCalendarWidget QToolButton:hover
                         {
                              background-color: hsl(35, 60%, 86%);
                         }
                         QCalendarWidget QToolButton:pressed
                         {
                              background-color: hsl(31, 48%, 84%);
                         }
                         QCalendarWidget QTableView QHeaderView::section
                         {
                              background-color: #d3e0ff;
                              color: #333333;
                              font-size: 14px;
                              font-weight: bold;
                              padding: 5px;
                              border: none;
                         }
                         QCalendarWidget QAbstractItemView 
                         {
                              background-color: #ffffff;
                              border: 1px solid #cccccc;
                              color: #000000;
                              selection-background-color: #007BFF;
                              selection-color: white;
                         }
                         QCalendarWidget QAbstractItemView::item
                         {
                              border: 1px solid #007BFF;
                         }
                         QPushButton
                         {
                              background-color: hsl(35, 60%, 96%);   
                              color: black;               
                              border-radius: 10px;        
                              font-size: 20px;            
                              padding: 15px 10px;         
                              font-weight: bold;
                              font-family: Arial Black;
                         }

                         QPushButton:hover{background-color: hsl(35, 60%, 86%);}
                         QPushButton:pressed{background-color: hsl(31, 48%, 84%);}
""")
      

    def update_date_label(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(selected_date.toString("yyyy-MM-dd"))


# Show/Run our App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())

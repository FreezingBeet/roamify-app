import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCalendarWidget, QVBoxLayout, QHBoxLayout,
                             QStackedWidget)
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPixmap
from weather import WeatherPage


class Roamify(QWidget):
     def __init__(self, stack_widget, weather_page):
          super().__init__()

          self.setWindowTitle("Roamify")
          self.stack_widget = stack_widget
          self.weather_page = weather_page
          
          self.initUI()

     def initUI(self):
          # Create all App Objects

          self.app_name = QLabel()    # Will later add an image with Roamify written on it stylistically and the same bg color as that of the app
          self.app_name.setPixmap(QPixmap("Roamify/roamify_logo_temp1.png"))
          self.app_name.setObjectName("app_name")

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
          self.location.setFixedWidth(600)
          self.date_label.setFixedWidth(600)
          self.calendar.setFixedWidth(600)

          button_layout = QHBoxLayout()
          button_layout.addStretch()
          button_layout.addWidget(self.submit_btn)
          button_layout.addStretch()

          location_layout = QHBoxLayout()
          location_layout.addStretch()
          location_layout.addWidget(self.location)
          location_layout.addStretch()

          date_layout = QHBoxLayout()
          date_layout.addStretch()
          date_layout.addWidget(self.date_label)
          date_layout.addStretch()

          calendar_layout = QHBoxLayout()
          calendar_layout.addStretch()
          calendar_layout.addWidget(self.calendar)
          calendar_layout.addStretch()

          master_layout.addWidget(self.app_name)
          master_layout.addSpacing(50)
          master_layout.addLayout(location_layout)
          master_layout.addSpacing(40)
          master_layout.addLayout(date_layout)
          master_layout.addSpacing(5)
          master_layout.addLayout(calendar_layout)
          master_layout.addSpacing(30)
          master_layout.addLayout(button_layout)

          self.setLayout(master_layout)
          self.app_name.setFixedHeight(int(self.height() * 0.6))

          self.setStyleSheet("""
                              QWidget{background-color: hsl(10, 47%, 40%);}
                              QLineEdit
                              {
                                   background-color: hsl(35, 90%, 81%);
                                   color: #ffffff;
                                   padding: 20px;
                                   font-weight: bold;
                                   font-size: 30px;
                                   border: 1px solid;
                                   border-radius: 5px;
                              }
                              #date_label
                              {
                                   background-color: hsl(35, 90%, 81%);
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
          

          self.submit_btn.clicked.connect(self.switch_page)

     def update_date_label(self):
          selected_date = self.calendar.selectedDate()
          self.date_label.setText(selected_date.toString("yyyy-MM-dd"))

     def switch_page(self):
          selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
          location = self.location.text().title()

          self.weather_page.update_weather_info(location, selected_date)
          self.stack_widget.setCurrentIndex(1)



class MainWindow(QWidget):
     def __init__(self):
          super().__init__()

          self.setWindowTitle("Roamify App")

          self.stack_widget = QStackedWidget()
          self.weather_page = WeatherPage()
          self.roamify_page = Roamify(self.stack_widget, self.weather_page)

          self.stack_widget.addWidget(self.roamify_page)
          self.stack_widget.addWidget(self.weather_page)

          layout = QVBoxLayout()
          layout.addWidget(self.stack_widget)
          self.setLayout(layout)

          self.setStyleSheet("""QWidget{background-color: hsl(10, 47%, 40%);}""")



# Show/Run our App
if __name__ == "__main__":
     app = QApplication(sys.argv)
     main_window = MainWindow()
     main_window.showMaximized()
     sys.exit(app.exec_())

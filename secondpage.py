import sys
import requests
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QTabWidget, QGridLayout, 
                             QSpinBox, QLineEdit, QCalendarWidget, QPushButton)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QDate

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roamify")

        self.initUI()

    def initUI(self):
        #Tab 1
        tab_layout = QGridLayout()

        self.tab1 = QWidget()
        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab1, "Weather")

        # Set background color
        self.tab1.setStyleSheet(""" 
            QWidget {
                background-color: hsl(10, 47%, 40%);
            }
            #box-label {
                background-color: hsl(35, 90%, 81%);
                color: white;
                padding: 6px;
                font-size: 16px;
                font-weight: bold;
                border: 1px solid #000;
                border-radius: 5px;
            }
            #label {
                color: hsl(35, 90%, 81%);
                font-size: 18px;
                font-weight: bold;
            }
            #app-name
            {
                color: hsl(35, 90%, 81%);
                font-size: 50px;
                font-weight: bold;
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
            QPushButton:pressed{background-color: hsl(31, 48%, 60%);}
        """)
        
        # Create all App Objects
        self.app_name = QLabel("WEATHER")
        self.app_name.setObjectName("app-name")
        self.date_label = QLabel("19-11-2024")
        self.date_label.setObjectName("box-label")

        self.temp_label = QLabel("TEMPERATURE")
        self.temp_label.setObjectName("label")

        self.morning_label = QLabel("MORNING")
        self.morning_label.setObjectName("label")
        self.morning_temp = QLabel("0.0")
        self.morning_temp.setObjectName("box-label")

        self.afternoon_label = QLabel("AFTERNOON")
        self.afternoon_label.setObjectName("label")
        self.afternoon_temp = QLabel("0.0")
        self.afternoon_temp.setObjectName("box-label")

        self.evening_label = QLabel("EVENING")
        self.evening_label.setObjectName("label")
        self.evening_temp = QLabel("0.0")
        self.evening_temp.setObjectName("box-label")

        self.max_label = QLabel("MAXIMUM")
        self.max_label.setObjectName("label")
        self.max_temp = QLabel("0.0")
        self.max_temp.setObjectName("box-label")

        self.min_label = QLabel("MINIMUM")
        self.min_label.setObjectName("label")
        self.min_temp = QLabel("0.0")
        self.min_temp.setObjectName("box-label")

        self.cloud_label = QLabel("CLOUD COVER")
        self.cloud_label.setObjectName("label")
        self.cloud_cover = QLabel("0.0")
        self.cloud_cover.setObjectName("box-label")

        self.humidity_label = QLabel("HUMIDITY")
        self.humidity_label.setObjectName("label")
        self.humidity_lvl = QLabel("0.0")
        self.humidity_lvl.setObjectName("box-label")

        self.wind_label = QLabel("WIND SPEED")
        self.wind_label.setObjectName("label")
        self.wind_speed = QLabel("0.0")
        self.wind_speed.setObjectName("box-label")

        self.ppt_label = QLabel("PRECIPITATION")
        self.ppt_label.setObjectName("label")
        self.ppt_lvl = QLabel("0.0")
        self.ppt_lvl.setObjectName("box-label")

        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.back_to_home)

        # All Design Here

        self.tab1.master_layout = QVBoxLayout()
        self.tab1.master_layout.setContentsMargins(400, 20, 400, 20)

        self.date_label.setFixedWidth(120)
        self.morning_temp.setFixedWidth(120)
        self.afternoon_temp.setFixedWidth(120)
        self.evening_temp.setFixedWidth(120)
        self.max_temp.setFixedWidth(120)
        self.min_temp.setFixedWidth(120)
        self.cloud_cover.setFixedWidth(120)
        self.wind_speed.setFixedWidth(120)
        self.humidity_lvl.setFixedWidth(120)
        self.ppt_lvl.setFixedWidth(120)

        self.date_label.setFixedHeight(60)
        self.morning_temp.setFixedHeight(50)
        self.afternoon_temp.setFixedHeight(50)
        self.evening_temp.setFixedHeight(50)
        self.max_temp.setFixedHeight(50)
        self.min_temp.setFixedHeight(50)
        self.cloud_cover.setFixedHeight(50)
        self.wind_speed.setFixedHeight(50)
        self.humidity_lvl.setFixedHeight(50)
        self.ppt_lvl.setFixedHeight(50)

        row1 = QHBoxLayout()
        row1.addWidget(self.date_label)
        row1.addStretch()
        row1.addWidget(self.app_name)

        row2 = QHBoxLayout()
        row2.addStretch()
        row2.addWidget(self.temp_label)
        row2.addStretch()

        row3 = QHBoxLayout()
        row3.addStretch()
        row3.addWidget(self.morning_label)
        row3.addStretch()
        row3.addWidget(self.afternoon_label)
        row3.addStretch()
        row3.addWidget(self.evening_label)
        row3.addStretch()

        row4 = QHBoxLayout()
        row4.addStretch()
        row4.addWidget(self.morning_temp)
        row4.addStretch()
        row4.addWidget(self.afternoon_temp)
        row4.addStretch()
        row4.addWidget(self.evening_temp)
        row4.addStretch()

        row5 = QHBoxLayout()
        row5.addStretch()
        row5.addWidget(self.min_label)
        row5.addStretch()
        row5.addWidget(self.max_label)
        row5.addStretch()

        row6 = QHBoxLayout()
        row6.addStretch()
        row6.addWidget(self.min_temp)
        row6.addStretch()
        row6.addWidget(self.max_temp)
        row6.addStretch()

        row7 = QHBoxLayout()
        row7.addStretch()
        row7.addWidget(self.cloud_label)
        row7.addStretch()
        row7.addWidget(self.wind_label)
        row7.addStretch()

        row8 = QHBoxLayout()
        row8.addStretch()
        row8.addWidget(self.cloud_cover)
        row8.addStretch()
        row8.addWidget(self.wind_speed)
        row8.addStretch()

        row9 = QHBoxLayout()
        row9.addStretch()
        row9.addWidget(self.humidity_label)
        row9.addStretch()
        row9.addWidget(self.ppt_label)
        row9.addStretch()

        row10 = QHBoxLayout()
        row10.addStretch()
        row10.addWidget(self.humidity_lvl)
        row10.addStretch()
        row10.addWidget(self.ppt_lvl)
        row10.addStretch()

        row11 = QHBoxLayout()
        row11.addStretch()
        row11.addWidget(self.back_btn)
        row11.addStretch()

        self.tab1.master_layout.addLayout(row1)
        self.tab1.master_layout.addLayout(row2)
        self.tab1.master_layout.addSpacing(-40)
        self.tab1.master_layout.addLayout(row3)
        self.tab1.master_layout.addSpacing(-30)
        self.tab1.master_layout.addLayout(row4)
        self.tab1.master_layout.addLayout(row5)
        self.tab1.master_layout.addSpacing(-30)
        self.tab1.master_layout.addLayout(row6)
        self.tab1.master_layout.addLayout(row7)
        self.tab1.master_layout.addSpacing(-30)
        self.tab1.master_layout.addLayout(row8)
        self.tab1.master_layout.addLayout(row9)
        self.tab1.master_layout.addSpacing(-30)
        self.tab1.master_layout.addLayout(row10)
        self.tab1.master_layout.addSpacing(-40)
        self.tab1.master_layout.addLayout(row11)
        
        self.tab1.setLayout(self.tab1.master_layout)
        tab_layout.addWidget(self.tabs1, 0, 0)

        #Tab 2
        self.tab2 = QWidget()
        self.tabs1.addTab(self.tab2, "Hotels")

        self.tab2.setStyleSheet(""" 
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
            }
            QCalendarWidget {
                background-color: white;
                border: 1px solid #000;
                border-radius: 5px;
                font-size: 16px;
            }
            QCalendarWidget QAbstractItemView {
                selection-background-color: hsl(10, 47%, 40%);
                selection-color: white;
                background-color: white;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: hsl(10, 47%, 40%);
            }
             QCalendarWidget QToolButton {
                color: white;
                background-color: hsl(10, 47%, 40%);
                border-radius: 3px;
                margin: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: hsl(10, 47%, 30%);
            }
            QCalendarWidget QAbstractItemView {
                selection-background-color: hsl(10, 47%, 40%);
                selection-color: white;
                background-color: white;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: hsl(10, 47%, 40%);
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: hsl(10, 47%, 40%);
                border-radius: 3px;
                margin: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: hsl(10, 47%, 30%);
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
            QPushButton:pressed{background-color: hsl(31, 48%, 60%);}
        """)

        # Create widgets for Check In and Check Out
        self.check_in_label = QLabel("Check In", self)
        self.check_in_label.mousePressEvent = lambda event: self.show_calendar("check_in")

        self.check_in_date = QLineEdit(self)
        self.check_in_date.setPlaceholderText("Select Check In Date")
        self.check_in_date.mousePressEvent = lambda event: self.show_calendar("check_in")
        self.check_in_date.setReadOnly(True)

        self.check_out_label = QLabel("Check Out", self)

        self.check_out_date = QLineEdit(self)
        self.check_out_date.setPlaceholderText("Select Check Out Date")
        self.check_out_date.mousePressEvent = lambda event: self.show_calendar("check_out")
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

        self.children_label = QLabel("Children (0 - 17)", self)
        self.children_spinbox = QSpinBox(self)
        self.children_spinbox.setMinimum(0)
        self.children_spinbox.setMaximum(10)

        self.min_price_label = QLabel("Minimum Price", self)
        self.min_price_spinbox = QSpinBox(self)
        self.min_price_spinbox.setMinimum(0)
        self.min_price_spinbox.setMaximum(100000)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setFixedWidth(200)
        self.submit_btn.clicked.connect(self.validate_inputs)

        # Calendar Widget
        self.calendar = QCalendarWidget(self)
        current_date = QDate.currentDate()
        one_year_later = current_date.addYears(1)
        self.calendar.setMinimumDate(current_date)
        self.calendar.setMaximumDate(one_year_later)
        self.calendar.hide()
        self.calendar.clicked.connect(self.set_date)

        # All Design Here
        
        self.tab2.master_layout = QVBoxLayout()
        self.tab2.master_layout.setContentsMargins(400, 20, 400, 20)

        check_in_layout = QVBoxLayout()
        check_in_layout.addWidget(self.check_in_label)
        check_in_layout.addWidget(self.check_in_date)
        check_in_layout.addWidget(self.adults_label)
        check_in_layout.addWidget(self.adults_spinbox)
        check_in_layout.addWidget(self.min_price_label)  # Add Maximum Price below Adults
        check_in_layout.addWidget(self.min_price_spinbox)

        check_out_layout = QVBoxLayout()
        check_out_layout.addWidget(self.check_out_label)
        check_out_layout.addWidget(self.check_out_date)
        check_out_layout.addWidget(self.children_label)
        check_out_layout.addWidget(self.children_spinbox)
        check_out_layout.addWidget(self.max_price_label)  # Add Minimum Price below Children
        check_out_layout.addWidget(self.max_price_spinbox)

        # Top layout for both sections
        top_layout = QHBoxLayout()
        top_layout.addLayout(check_in_layout)
        top_layout.addStretch()  # Add spacing
        top_layout.addLayout(check_out_layout)

        submit_btn_layout = QHBoxLayout()
        submit_btn_layout.addStretch()
        submit_btn_layout.addWidget(self.submit_btn)
        submit_btn_layout.addStretch()

        self.hotel_grid_layout = QGridLayout()
        self.hotel_grid_layout.setSpacing(20)

        self.tab2.master_layout.addLayout(top_layout)
        self.tab2.master_layout.addLayout(submit_btn_layout)
        self.tab2.master_layout.addLayout(self.hotel_grid_layout)
        self.tab2.master_layout.addStretch()  # Push other elements down
        self.tab2.master_layout.addWidget(self.calendar)

        self.setLayout(self.tab2.master_layout)
        self.tab2.setLayout(self.tab2.master_layout)




        self.setLayout(tab_layout)

    def set_location(self, location):
        self.location = location

    def update_weather_info(self, location, date, stack_widget):
        self.date_label.setText(date)
        self.stack_widget = stack_widget
        self.get_geocode_data(location, date)

        self.check_in_date.setText(date)
        self.check_out_date.clear()
        self.adults_spinbox.setValue(1)
        self.children_spinbox.setValue(0)
        self.min_price_spinbox.setValue(0)
        self.max_price_spinbox.setValue(0)

        while self.hotel_grid_layout.count():
            child = self.hotel_grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def get_geocode_data(self, location, date):
        appid = os.getenv("API_KEY")

        geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={appid}"
        geocode_response = requests.get(geocode_url)
        lat = 0
        lon = 0

        if geocode_response.status_code == 200:
            try:
                coord_data = geocode_response.json()
                lat = str(coord_data[0]['lat'])
                lon = str(coord_data[0]['lon'])
                self.get_weather_data(lat, lon, date)
            except:
                QMessageBox.warning(self, "Wrong city", "Sorry! City not found")
        else:
            QMessageBox.warning(self, "Wrong city", "Sorry! City not found")

    def get_weather_data(self, lat, lon, date):
        appid = os.getenv("API_KEY")

        weather_url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&appid={appid}&units=metric"
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            try:
                weather_data = weather_response.json()

                self.min_temp.setText(str(weather_data['temperature']['min']) + " C")
                self.max_temp.setText(str(weather_data['temperature']['max']) + " C")
                self.morning_temp.setText(str(weather_data['temperature']['morning']) + " C")
                self.afternoon_temp.setText(str(weather_data['temperature']['afternoon']) + " C")
                self.evening_temp.setText(str(weather_data['temperature']['evening']) + "C")
                self.cloud_cover.setText(str(weather_data['cloud_cover']['afternoon']) + "%")
                self.wind_speed.setText(str(weather_data['wind']['max']['speed']) + "Km/h")
                self.humidity_lvl.setText(str(weather_data['humidity']['afternoon']) + "%")
                self.ppt_lvl.setText(str(weather_data['precipitation']['total']) + "%")
            except:
                QMessageBox.warning(self, "Error" + str(weather_response.status_code), "Couldn't recieve city's data")
        else:
            QMessageBox.warning(self, "Error" + str(weather_response.status_code), "Couldn't recieve city's data")

    def show_calendar(self, mode):
        """Display the calendar and store the mode (check-in or check-out)."""

        while self.hotel_grid_layout.count():
            child = self.hotel_grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        
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

    def validate_inputs(self):
        """Validate user inputs before displaying hotels."""

        if not self.check_in_date.text():
            QMessageBox.warning(self, "Input Error", "Please select a Check In date.", QMessageBox.Ok)
            return
        if not self.check_out_date.text():
            QMessageBox.warning(self, "Input Error", "Please select a Check Out date.", QMessageBox.Ok)
            return
        if self.adults_spinbox.value() <= 0:
            QMessageBox.warning(self, "Input Error", "Number of Adults must be greater than 0.", QMessageBox.Ok)
            return
        if self.min_price_spinbox.value() <= 0:
            QMessageBox.warning(self, "Input Error", "Minimum Price must be greater than 0.", QMessageBox.Ok)
            return
        if self.min_price_spinbox.value() > self.max_price_spinbox.value():
            QMessageBox.warning(self, "Input Error", "Maximum Price must be greater than the Minimum price.", QMessageBox.Ok)
            return

        # If all validations pass, display hotels
        self.display_hotels()

    def display_hotels(self):
        """Display hotel details in the grid."""

        # Clear the grid before adding new items
        while self.hotel_grid_layout.count():
            child = self.hotel_grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Hotel data
        hotels = self.get_hotels()

        # Add hotel widgets to the grid (2 per row)
        for i, hotel in enumerate(hotels):
            # Image
            try:
                image = QImage()
                image.loadFromData(requests.get(hotel["image"]).content)
                pixmap = QPixmap(image).scaled(220, 220, aspectRatioMode=True)
            except:
                pixmap = pixmap = QPixmap("Roamify/roamify_logo_temp1.png").scaled(220, 220, aspectRatioMode=True)

            image_label = QLabel(self)
            image_label.setPixmap(pixmap)
            image_label.setFixedSize(220, 220)

            # Details
            details_label = QLabel(f"{hotel['name']}\nPrice: {hotel['price']}\nRating: {hotel['rating']}\nReviews: {hotel['reviews']}")
            details_label.setStyleSheet("color: white; font-size: 14px; font-weight: bold; text-align: center;")

            # Calculate row and column for grid layout
            row = i // 2
            col = i % 2

            # Add to grid
            self.hotel_grid_layout.addWidget(image_label, row, col * 2)  # Image in the first column
            self.hotel_grid_layout.addWidget(details_label, row, col * 2 + 1)  # Details in the second column

    def get_hotels(self):
        location = self.location
        check_in_date = self.check_in_date.text()
        check_out_date = self.check_out_date.text()
        adults = self.adults_spinbox.value()
        children = self.children_spinbox.value()
        min_price = self.min_price_spinbox.value()
        max_price = self.max_price_spinbox.value()
        api_key = "182fb0151f12ec02cb3610e6321c6a917487537962b92f2fa8e2e9e719f72fa7"


        url = f"https://serpapi.com/search.json?engine=google_hotels&q={location}+Hotels&check_in_date={check_in_date}&check_out_date={check_out_date}&adults={adults}&children={children}&min_price={min_price}&max_price={max_price}&currency=INR&gl=us&hl=en&api_key={api_key}"
        response = requests.get(url)

        list_hotels = []

        if response.status_code == 200:
            try:
                data = response.json()
                hotels = data['properties']
            except:
                QMessageBox.warning(self, "Error", "Some error occurred")
                return list_hotels

            for i in range(min(4, len(hotels))):
                hotel = hotels[i]
                hotel_data = {}

                try:
                    hotel_data['name'] = hotel['name']
                except:
                    hotel_data['name'] = "NaN"
                try:
                    hotel_data['price'] = hotel['rate_per_night']['lowest']
                except:
                    hotel_data['price'] = "NaN"
                try:
                    hotel_data['rating'] = hotel['overall_rating']
                except:
                    hotel_data['rating'] = "NaN"
                try:
                    hotel_data['reviews'] = hotel['reviews']
                except:
                    hotel_data['reviews'] = "NaN"
                try:
                    hotel_data['image'] = hotel['images'][0]['original_image']
                except:
                    hotel_data['image'] = "NaN"
                
                list_hotels.append(hotel_data)
            
            return list_hotels
        else:
            QMessageBox.warning(self, "Error", "Sorry! Can't recieve hotel data")
            return list_hotels

    def back_to_home(self):
        self.stack_widget.setCurrentIndex(0)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SecondPage()
    main_window.showMaximized()
    sys.exit(app.exec_())

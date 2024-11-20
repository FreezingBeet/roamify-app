import sys
import requests
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class WeatherPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roamify")

        self.initUI()

    def initUI(self):
        # Set background color
        self.setStyleSheet(""" 
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
                font-family: "Arial";
            }
            #app-name
            {
                color: hsl(35, 90%, 81%);
                font-size: 50px;
                font-weight: bold;
                font-family: "Arial";
            }
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

        # All Design Here

        master_layout = QVBoxLayout()
        master_layout.setContentsMargins(400, 20, 400, 100)

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

        master_layout.addLayout(row1)
        master_layout.addLayout(row2)
        master_layout.addSpacing(-40)
        master_layout.addLayout(row3)
        master_layout.addSpacing(-30)
        master_layout.addLayout(row4)
        master_layout.addLayout(row5)
        master_layout.addSpacing(-30)
        master_layout.addLayout(row6)
        master_layout.addLayout(row7)
        master_layout.addSpacing(-30)
        master_layout.addLayout(row8)
        master_layout.addLayout(row9)
        master_layout.addSpacing(-30)
        master_layout.addLayout(row10)
        
        self.setLayout(master_layout)



    def update_weather_info(self, location, date):
        self.date_label.setText(date)
        self.get_geocode_data(location, date)
    
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = WeatherPage()
    main_window.showMaximized()
    sys.exit(app.exec_())

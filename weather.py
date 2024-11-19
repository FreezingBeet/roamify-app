import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class Roamify(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Roamify")
        self.resize(800, 600)  

        self.initUI()

    def initUI(self):
        # Set background color
        self.setStyleSheet(""" 
            QWidget {
                background-color: hsl(10, 47%, 40%);
            }
            QLineEdit {
                background-color: hsl(35, 90%, 81%);
                color: black;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #000;
                border-radius: 5px;
            }
            QLabel {
                color: hsl(35, 90%, 81%);
                font-size: 18px;
                font-weight: bold;
                font-family: "Arial";
            }
        """)
        
        self.temp_label = QLabel("TEMPERATURE", self)
        self.temp_label.setGeometry(313, 10,180, 40)

        # Label for "DATE"
        self.date_label = QLineEdit("19-11-2024", self)
        self.date_label.setGeometry(10, 20, 180, 40)  # Positioned as the first item, just like the date picker

        # Label for "MORNING"
        self.morning_label = QLabel("MORNING", self)
        self.morning_label.setGeometry(90, 70, 180, 30)  # Shifted slightly down by adjusting y-coordinate

        # Morning Temperature input box
        self.morning_temp = QLineEdit(self)
        self.morning_temp.setPlaceholderText("Morning Temperature")
        self.morning_temp.setGeometry(50, 100, 180, 40)  # Position remains the same

        # Label for "AFTERNOON"
        self.afternoon_label = QLabel("AFTERNOON", self)
        self.afternoon_label.setGeometry(328, 70, 180, 30)  # Positioned next to "MORNING" label

        # Afternoon Temperature input box
        self.afternoon_temp = QLineEdit(self)
        self.afternoon_temp.setPlaceholderText("Afternoon Temperature")
        self.afternoon_temp.setGeometry(300, 100, 180, 40)  # Correctly positioned

        # Label for "EVENING"
        self.evening_label = QLabel("EVENING", self)
        self.evening_label.setGeometry(600, 70, 180, 30)  # Positioned next to "AFTERNOON" label

        # Evening Temperature input box
        self.evening_temp = QLineEdit(self)
        self.evening_temp.setPlaceholderText("Evening Temperature")
        self.evening_temp.setGeometry(560, 100, 180, 40)  # Positioned next to "EVENING" label

        # Label for "MAXIMUM" (below existing boxes)
        self.max_label = QLabel("MAXIMUM", self)
        self.max_label.setGeometry(220, 160, 180, 30)  # Positioned below the "MORNING" label

        # Max Temperature input box (below the others)
        self.max_temp = QLineEdit(self)
        self.max_temp.setPlaceholderText("Max Temperature")
        self.max_temp.setGeometry(180, 190, 180, 40)  # Positioned below the "MORNING" temperature box

        # Label for "MINIMUM" (below the "AFTERNOON" label)
        self.min_label = QLabel("MINIMUM", self)
        self.min_label.setGeometry(470, 160, 180, 30)  # Positioned below the "AFTERNOON" label

        self.min_temp = QLineEdit(self)
        self.min_temp.setPlaceholderText("Min Temperature")
        self.min_temp.setGeometry(430, 190, 180, 40)  # Positioned below the "AFTERNOON" temperature box

        # Add a new block below the "MAXIMUM" and "MINIMUM" section
        # Label for "MAXIMUM" (second block)
        self.cloud_label = QLabel("CLOUD COVER", self)
        self.cloud_label.setGeometry(156, 315, 180, 30)  # Positioned below the first "MAXIMUM"

        # Max Temperature input box (second block)
        self.cloud_cover = QLineEdit(self)
        self.cloud_cover.setPlaceholderText("CLOUD COVER")
        self.cloud_cover.setGeometry(140, 345, 180, 40)  # Positioned below the first "Max Temperature" box

        # Label for "MINIMUM" (second block)
        self.humidity_label = QLabel("HUMIDITY", self)
        self.humidity_label.setGeometry(530, 315, 180, 30)  # Positioned below the first "MINIMUM" label

        # Min Temperature input box (second block)
        self.humidity_lvl = QLineEdit(self)
        self.humidity_lvl.setPlaceholderText("HUMIDITY")
        self.humidity_lvl.setGeometry(480, 345, 180, 40)  # Positioned below the first "Min Temperature" box

        self.wind_label = QLabel("WIND SPEED", self)
        self.wind_label.setGeometry(165, 470, 180, 30)  # Positioned below the second "MAXIMUM"

        # Max Temperature input box (third block)
        self.wind_speed = QLineEdit(self)
        self.wind_speed.setPlaceholderText("WIND SPEED")
        self.wind_speed.setGeometry(140, 500, 180, 40)  # Positioned below the second "Max Temperature" box

        # Label for "MINIMUM" (third block)
        self.ppt_label = QLabel("PRECIPITATION", self)
        self.ppt_label.setGeometry(500, 470, 180, 30)  # Positioned below the second "MINIMUM" label

        # Min Temperature input box (third block)
        self.ppt_lvl = QLineEdit(self)
        self.ppt_lvl.setPlaceholderText("PRECIPITATION")
        self.ppt_lvl.setGeometry(480, 500, 180, 40)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Roamify()
    main_window.show()
    sys.exit(app.exec_())

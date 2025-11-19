import datetime
import os
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from hijri_converter import Gregorian
os.system('cls')


class PrayerSchApp(QWidget):

    def __init__(self):
        super().__init__()
        self.title_label = QLabel('Prayer time in: ', self)
        self.location_label = QLabel(self)

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Write your city")

        self.country_input = QLineEdit(self)
        self.country_input.setPlaceholderText("Write your country")

        self.get_button = QPushButton("Find", self)
        self.get_button.setCursor(Qt.PointingHandCursor)

        self.date_label = QLabel(self)

        self.error_label = QLabel(self)

        self.time_labels = []
        self.initUi()
        self.date()

    def initUi(self):
        self.setWindowTitle("Player Schdule App")

        # Main Layout
        main_vbox = QVBoxLayout()
        main_vbox.setSpacing(5)
        main_vbox.setContentsMargins(10, 0, 10, 15)

        # Date and Title
        top_hbox = QHBoxLayout()
        self.title_label.setAlignment(Qt.AlignLeft)
        top_hbox.addWidget(self.title_label)
        top_hbox.addStretch()
        top_hbox.addWidget(self.date_label)
        main_vbox.addLayout(top_hbox)

        # City
        self.location_label.setAlignment(Qt.AlignLeft)
        main_vbox.addWidget(self.location_label)

        # Input and Button
        srch_layout = QHBoxLayout()
        srch_layout.setSpacing(20)
        srch_layout.setContentsMargins(0, 0, 350, 140)

        srch_layout.addWidget(self.city_input)
        srch_layout.addWidget(self.country_input)
        srch_layout.addWidget(self.get_button)
        self.country_input.hide()

        main_vbox.addLayout(srch_layout)

        # Error
        self.error_label.setAlignment(Qt.AlignCenter)
        main_vbox.addWidget(self.error_label)

        # Name and Time
        main_hbox = QHBoxLayout()
        main_hbox.setSpacing(20)

        data = [
            ('Fajr', self),
            ('Dhuhr', self),
            ('Asr', self),
            ('Maghrib', self),
            ('Isha', self)
        ]

        for name, time in data:

            box_frame = QFrame(self)
            
            if name == "Fajr":
                box_frame.setObjectName("ActivePrayerBox")
            else:
                box_frame.setObjectName("prayerBox")
                
            box_vlayout = QVBoxLayout()
            box_vlayout.setSpacing(20)
            box_vlayout.setContentsMargins(0, 10, 0, 50)
            # left, top, right, bottom

            pray_label = QLabel(name)
            time_label = QLabel(time)

            pray_label.setObjectName("pray_label")
            time_label.setObjectName("time_label")

            pray_label.setAlignment(Qt.AlignCenter)
            time_label.setAlignment(Qt.AlignCenter)

            self.time_labels.append(time_label)

            box_vlayout.addWidget(pray_label)
            box_vlayout.addWidget(time_label)

            box_frame.setLayout(box_vlayout)
            main_hbox.addWidget(box_frame)

        main_vbox.addLayout(main_hbox)
        self.get_button.clicked.connect(self.button_click)

        self.setLayout(main_vbox)

        self.title_label.setObjectName("title_label")
        self.location_label.setObjectName("location_label")
        self.error_label.setObjectName("error_label")
        self.date_label.setObjectName("date_label")
        self.city_input.setObjectName("city_input")
        self.country_input.setObjectName("country_input")
        self.get_button.setObjectName("get_button")

        self.setStyleSheet("""
            
            QLabel{
                font-family: "Plus Jakarta Sans";
                font-size: 14px;
                font-weight: 450;
            }
            
            QLabel#pray_label{
                font-family: "Plus Jakarta Sans";
                font-size: 16px;
                font-weight:500;
            }
            
            QLabel#time_label{
                font-family: "Plus Jakarta Sans";
                font-size: 20px;
                font-weight:700;
                qproperty-alignment: 'AlignHCenter';
            } 
            
             
            QLabel#location_label{
                font-family: "Plus Jakarta Sans";
                font-size: 21px;
                font-weight: 600;
            }
            
            QLabel#error_label{
                font-family: "Plus Jakarta Sans";
                font-size: 21px;
                font-weight: 600;
                padding-bottom: 15px;
                padding-top: 0px;
            }
            
            QFrame#prayerBox{
                background-color: #ffffff;
                border: 2px solid transparent;
                border-radius: 12px;
            }
            
            QFrame#ActivePrayerBox{
                font-family: "Plus Jakarta Sans";
                background-color: #ffffff;
                border: 3px solid #1DB954;
                border-radius: 12px;
            }
            
            
            QLineEdit#city_input{
                font-family: "Plus Jakarta Sans";
                font-size: 16px;
                border-radius: 20px;
                padding: 12px 15px;
                border: 1px solid #ced4da;
                max-width: 300px;
            }
            
            QLineEdit#country_input{
                font-family: "Plus Jakarta Sans";
                font-size: 16px;
                border-radius: 20px;
                padding: 12px 15px;
                border: 1px solid #ced4da;
                max-width: 300px;
            }
            
            QPushButton#get_button{
                font-size: 16px;
                color: white;
                background-color: #1DB954;
                border-radius: 20px;
                border: none;
                padding: 12px 15px;
                border: 1px solid #ced4da;
                font-weight: bold;
                max-width: 100px;
            }
            QPushButton#get_button:hover{
                background-color: #1ED760;
            }
            
                           """)

        self.setFixedSize(800, 500)
        self.date_label.setAlignment(Qt.AlignRight)

    def button_click(self):
        if self.country_input.isHidden():

            self.country_input.show()
            self.city_input.hide()

        else:
            self.get_schedule()

    def get_schedule(self):

        city = self.city_input.text()
        country = self.country_input.text()

        if not city or not country:

            self.location_label.setText("Please fill in the text.")
            return

        url = f"http://api.aladhan.com/v1/timingsByCity/11-11-2025?city={city}&country={country}&method=20"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["code"] == 200:
                self.display_schedule(data)

                location_label = f"{city}, {country}"
                self.location_label.setText(location_label)
            else:
                self.location_label.setText(
                    f"Location of {city} City and {country}  Country not found")

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error(
                        'Bad Requests:\nPlease Check Your Input')

                case 403:
                    self.display_error("Forbidden:\nAcces is denied")

                case 500:
                    self.display_error(
                        "Internal Server Error:\nPlease Try Again Later")

                case 502:
                    self.display_error(
                        "Bad Gateway:\nInvalid response from the server")

                case 503:
                    self.display_error("Service Unavailable:\nServer id down")

                case 504:
                    self.display_error(
                        "Gateway Timeout:\nNo response from the server")

                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection Error:\n Check your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe requests timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\n Check the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

        self.city_input.show()
        self.country_input.hide()
        self.city_input.clear()
        self.country_input.clear()

    def date(self):
        now = datetime.datetime.now()
        gregorian_var = Gregorian(now.year, now.month, now.day)

        hijri_date = gregorian_var.to_hijri()

        day = hijri_date.day
        month_name = hijri_date.month_name()
        year = hijri_date.year

        gregorian = now.strftime("%d %B,  %Y")

        hijri = f"{day} {month_name},  {year}"

        final_date = f"{gregorian} | {hijri}"

        self.date_label.setText(final_date)

    def display_error(self, message):
        self.error_label.setText(message)

    def display_schedule(self, data):

        fajr = data["data"]["timings"]["Fajr"]
        dhuhr = data["data"]["timings"]["Dhuhr"]
        asr = data["data"]["timings"]["Asr"]
        maghrib = data["data"]["timings"]["Maghrib"]
        isha = data["data"]["timings"]["Isha"]

        self.time_labels[0].setText(f"{fajr} am")
        self.time_labels[1].setText(f"{dhuhr} am")
        self.time_labels[2].setText(f"{asr} am")
        self.time_labels[3].setText(f"{maghrib} am")
        self.time_labels[4].setText(f"{isha} am")

        print('Complete')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prayer_schaapp = PrayerSchApp()
    prayer_schaapp.show()
    sys.exit(app.exec_())

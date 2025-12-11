import os
import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from hijri_converter import Gregorian
from PyQt5.QtGui import QFontDatabase

from .api_service import get_schedule

STYLESHEET = """

            QLabel{
                font-family: "Plus Jakarta Sans";
                font-size: 14px;
                font-weight: 450;
            }

            QLabel#name_label{
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

            """


class PrayerSchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.prayer_frames = []
        self.time_labels = []

        self.get_font()
        self.initUi()
        self.get_date()

    def get_font(self):

        current_file_path = os.path.abspath(__file__)
        current_folder = os.path.dirname(current_file_path)
        project_root = os.path.dirname(current_folder)

        font_files = ["PlusJakartaSans-Regular.ttf",
                      "PlusJakartaSans-SemiBold.ttf", "PlusJakartaSans-Bold.ttf"]

        for filename in font_files:
            font_path = os.path.join(project_root, "fonts", filename)
            font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id < 0:
            print("Gagal dimuat")
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            print(f"Font berhasil dimuat: {font_families[0]}")

    def initUi(self):

        self.setWindowTitle("Player Schdule App")
        self.setFixedSize(800, 550)
        self.title_label = QLabel('Prayer time in: ', self)
        self.date_label = QLabel(self)
        self.location_label = QLabel(self)
        self.error_label = QLabel(self)

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Write your city")
        self.country_input = QLineEdit(self)
        self.country_input.setPlaceholderText("Write your country")
        self.country_input.hide()

        self.get_button = QPushButton("Find", self)
        self.get_button.setCursor(Qt.PointingHandCursor)
        self.get_button.clicked.connect(self.button_click)

        # Layouting
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

        # City Label
        self.location_label.setAlignment(Qt.AlignLeft)
        main_vbox.addWidget(self.location_label)

        # Search Area
        srch_layout = QHBoxLayout()
        srch_layout.setSpacing(20)
        srch_layout.setContentsMargins(0, 0, 350, 140)

        srch_layout.addWidget(self.city_input)
        srch_layout.addWidget(self.country_input)
        srch_layout.addWidget(self.get_button)
        self.country_input.hide()

        main_vbox.addLayout(srch_layout)

        # Error Message
        self.error_label.setAlignment(Qt.AlignCenter)
        main_vbox.addWidget(self.error_label)

        # Prayer Boxes
        self.create_prayer_boxes(main_vbox)

        self.setLayout(main_vbox)
        self.set_object_names()
        self.setStyleSheet(STYLESHEET)

    def create_prayer_boxes(self, parent_layout):
        main_hbox = QHBoxLayout()
        main_hbox.setSpacing(20)
        prayer_names = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

        for name in prayer_names:
            box = QFrame(self)
            box.setObjectName("prayerBox")
            box.setFixedSize(140, 160)
            vbox = QVBoxLayout(box)
            vbox.setContentsMargins(0, 30, 0, 30)

            name_label = QLabel(name)
            name_label.setObjectName("name_label")
            name_label.setAlignment(Qt.AlignCenter)

            time_label = QLabel("")
            time_label.setObjectName("time_label")
            time_label.setAlignment(Qt.AlignCenter)

            vbox.addWidget(name_label)
            vbox.addWidget(time_label)

            self.time_labels.append(time_label)
            self.prayer_frames.append(box)
            main_hbox.addWidget(box)

        parent_layout.addLayout(main_hbox)

    def set_object_names(self):
        self.title_label.setObjectName("title_label")
        self.location_label.setObjectName("location_label")
        self.error_label.setObjectName("error_label")
        self.date_label.setObjectName("date_label")
        self.city_input.setObjectName("city_input")
        self.country_input.setObjectName("country_input")
        self.get_button.setObjectName("get_button")

    def button_click(self):
        if self.country_input.isHidden():
            self.country_input.show()
            self.city_input.hide()
        else:
            get_schedule(self)

    def get_date(self):
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

    def get_active_prayer(self, timings):

        now = datetime.datetime.now().strftime("%H:%M")

        fajr = timings['Fajr']
        dhuhr = timings['Dhuhr']
        asr = timings['Asr']
        maghrib = timings['Maghrib']
        isha = timings['Isha']

        index = -1

        if now >= fajr and now < dhuhr:
            index = 0
        elif now >= dhuhr and now < asr:
            index = 1
        elif now >= asr and now < maghrib:
            index = 2
        elif now >= maghrib and now < isha:
            index = 3
        elif now >= isha or now < fajr:
            index = 4

        for i, frame in enumerate(self.prayer_frames):
            if i == index:
                frame.setObjectName("ActivePrayerBox")
            else:
                frame.setObjectName("prayerBox")

            frame.style().unpolish(frame)
            frame.style().polish(frame)

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

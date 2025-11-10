import datetime
import os
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
os.system('cls')


class PrayerSchApp(QWidget):

    def __init__(self):
        super().__init__()
        self.title_label = QLabel('Prayer time in: ', self)
        self.city_label = QLabel('Bandung, Indonesia', self)

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Write your location")

        self.get_button = QPushButton("Find", self)
        self.get_button.setCursor(Qt.PointingHandCursor)

        self.date_label = QLabel(
            'Monday, 10 November 2025 | 19 Jumada al-Ula 1447', self)
        self.time_labels = []
        self.initUi()

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
        self.city_label.setAlignment(Qt.AlignLeft)
        main_vbox.addWidget(self.city_label)

        # Input and Button
        srch_layout = QHBoxLayout()
        srch_layout.setSpacing(20)
        srch_layout.setContentsMargins(0, 10, 350, 150)

        srch_layout.addWidget(self.city_input)
        srch_layout.addWidget(self.get_button)
        main_vbox.addLayout(srch_layout)

        # Name and Time
        main_hbox = QHBoxLayout()
        main_hbox.setSpacing(20)

        data = [
            ('Fajr', '....'),
            ('Zuhur', '....'),
            ('Ashar', '....'),
            ('Maghrib', '....'),
            ('Isya', '....')
        ]

        for name, time in data:

            box_frame = QFrame(self)
            if name == "Isya":
                box_frame.setObjectName("ActivePrayerBox")
            else:
                box_frame.setObjectName("prayerBox")
            box_vlayout = QVBoxLayout()
            box_vlayout.setSpacing(20)
            box_vlayout.setContentsMargins(0, 10, 0, 120)
            # left, top, right, bottom

            pray_label = QLabel(name)
            time_label = QLabel(time)

            pray_label.setAlignment(Qt.AlignCenter)
            time_label.setAlignment(Qt.AlignCenter)

            self.time_labels.append(time_label)

            box_vlayout.addWidget(pray_label)
            box_vlayout.addWidget(time_label)

            box_frame.setLayout(box_vlayout)
            main_hbox.addWidget(box_frame)

        main_vbox.addLayout(main_hbox)

        self.setLayout(main_vbox)

        self.title_label.setObjectName("title_label")
        self.date_label.setObjectName("date_label")
        self.city_input.setObjectName("city_input")
        self.get_button.setObjectName("get_button")
        pray_label.setObjectName("pray_label")
        time_label.setObjectName("time_label")

        self.setStyleSheet(""" 
            QWidget{}
            
            QFrame#prayerBox{
                background-color: #ffffff;
                border: 2px solid transparent;
                border-radius: 12px;
            }
            
            QFrame#ActivePrayerBox{
                background-color: #ffffff;
                border: 3px solid #1DB954;
                border-radius: 12px;
            }
            
            Qlabel, QPushButton{
                font-family: calibri;
            }
            QLineEdit#city_input{
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

        self.setFixedSize(800, 450)
        self.date_label.setAlignment(Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prayer_schaapp = PrayerSchApp()
    prayer_schaapp.show()
    sys.exit(app.exec_())

    # now = datetime.datetime.now()
    # print(now.strftime("%d %B %Y"))

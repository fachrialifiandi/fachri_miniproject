import sys
from PyQt5.QtWidgets import QApplication
from sch_utils.gui_design import PrayerSchApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrayerSchApp()
    window.show()
    sys.exit(app.exec_())

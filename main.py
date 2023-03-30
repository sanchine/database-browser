from PyQt5.QtWidgets import QApplication
from windows.Main import Main
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

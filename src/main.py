import sys
from PyQt5.QtWidgets import QApplication
from gui import App

if __name__ == "__main__":
    # launches the gui and application
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
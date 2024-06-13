from PyQt5.QtWidgets import QPushButton, QSizePolicy


class ToggleSwitch(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setMinimumSize(50, 25)
        self.setMaximumSize(50, 25)
        self.setChecked(False)
        self.update_style()

    def update_style(self):
        if self.isChecked():
            self.setStyleSheet("""
                QPushButton {
                    background-color: #66bb6a;
                    border-radius: 12px;
                }
                QPushButton::before {
                    content: "";
                    position: absolute;
                    left: 25px;
                    top: 2px;
                    width: 21px;
                    height: 21px;
                    background-color: white;
                    border-radius: 10px;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #ccc;
                    border-radius: 12px;
                }
                QPushButton::before {
                    content: "";
                    position: absolute;
                    left: 2px;
                    top: 2px;
                    width: 21px;
                    height: 21px;
                    background-color: white;
                    border-radius: 10px;
                }
            """)
            
    def paintEvent(self, event):
        super().paintEvent(event)
        self.update_style()
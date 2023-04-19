import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget

class Screen1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel("Screen 1")
        layout.addWidget(self.label)
        self.button = QPushButton("Go to Screen 2")
        layout.addWidget(self.button)

class Screen2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel("Screen 2")
        layout.addWidget(self.label)
        self.button = QPushButton("Go back to Screen 1")
        layout.addWidget(self.button)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QStackedWidget to manage multiple screens
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create the screens and add them to the QStackedWidget
        self.screen1 = Screen1()
        self.screen2 = Screen2()
        self.stacked_widget.addWidget(self.screen1)
        self.stacked_widget.addWidget(self.screen2)

        # Connect the button signals to the slot that changes the current widget
        self.screen1.button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.screen2))
        self.screen2.button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.screen1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QColorDialog, QLabel

class ColorPickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window's Details
        self.setWindowTitle("Color Picker")
        self.main_layout = QVBoxLayout()
        self.setFixedSize(220, 100)

        # UI things
        self.color_label = QLabel()
        self.copied_label = QLabel()
        self.color_label.setText("Click the button to pick color")
        self.main_layout.addWidget(self.color_label)
        
        self.pick_color_button = QPushButton("Pick Color")
        self.pick_color_button.clicked.connect(self.openColorDialog)
        self.main_layout.addWidget(self.pick_color_button)

        # Set layout
        self.setLayout(self.main_layout)

    # Colorbox dialog
    def openColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_label.setText("Selected Color: " + color.name())
            self.color_label.setStyleSheet("Background-color: " + color.name())
            self.copyToClipboard(color.name())

    # Copy to clipboard
    def copyToClipboard(self, text: str):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        self.copied_label.setText("Selected color copied to clipboard")
        self.main_layout.addWidget(self.copied_label)

# no need to do __name__ == '__main__' as this is just a single file
app = QApplication(sys.argv)
window = ColorPickerApp()
window.show()
sys.exit(app.exec())

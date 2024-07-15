# ch 4.2.1 main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget
class Calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Calcualtor')
        self.resize(256, 256)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())
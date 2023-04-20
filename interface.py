from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
    
from greetings import GreetingsWindow

class TInterface:
    
    #def create_input_table()

    def __init__(self):
        self.window = QMainWindow()
        self.ui = GreetingsWindow()
        self.ui.setupUi(self.window)

    def show(self):
        self.window.show()
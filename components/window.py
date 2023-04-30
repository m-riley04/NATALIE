from PyQt6.QtWidgets import *
from PyQt6.QtCore import QSize
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QAction, QPixmap
from threading import Thread
from .app import App

class Window(QMainWindow):
    '''GUI of the application'''
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("components/layout.ui", self)
        
        # Initialize Icons
        #self._appIcon           = QIcon("components/icons/icon.ico")
        
        # Window Attributes
        self.setWindowTitle("NATALIE")
        #self.setWindowIcon(self._appIcon)
        self.setFixedSize(800, 603)
        
        # Import Stylesheet
        with open("components/stylesheet.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        
        # Set app
        self.app = App()
        
        # Initialize Widgets
        self._initialize_widgets()
        self._initialize_settings()
        
        # Show Window
        self.show()
        
    def _initialize_widgets(self):
        self.btn_main.clicked.connect(lambda: self.navigate(self.stack_pages, self.page_main))
        self.btn_settings.clicked.connect(lambda: self.navigate(self.stack_pages, self.page_settings))
        self.btn_speak.clicked.connect(lambda: self.click_speak())
        #self.field_prompt.returnPressed.connect(lambda: self.submit_prompt())
        
    def _initialize_settings(self):
        self.dropdown_devices.addItems(self.app.get_devices())
        self.dropdown_devices.currentIndexChanged.connect(lambda: self.app.set_device(self.dropdown_devices.currentIndex()))
        self.slider_threshold.valueChanged.connect(lambda: self.app.set_threshold(self.slider_threshold.value()))
    
    def _initialize_pages(self):
        pass
    
    def navigate(self, stack, page):
        stack.setCurrentWidget(page)
        
    def click_speak(self):
        self.checkbox_listen.setChecked(True)
        _input = self.app.listen()
        self.textbox_input.setText(_input)
        _output = self.app.respond(_input)
        self.textbox_output.setText(_output)
    
    def submit_prompt(self):
        pass
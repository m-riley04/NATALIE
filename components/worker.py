from PyQt6 import QtCore
from time import sleep


class Worker(QtCore.QObject):
    def __init__(self, func, *args):
        self.working = QtCore.pyqtSignal(bool)
        self.value = QtCore.pyqtSignal(str)
        self.finished = QtCore.pyqtSignal()
        self.func = func
        self.args = args

    def run(self):
        self.working.emit(True)
        value = self.func(self.args)
        
        self.value.emit(str(value))
        self.working.emit(False)

        self.finished.emit()
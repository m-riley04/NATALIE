from .natalie import Natalie
import threading as th
from PyQt6.QtCore import QThread, pyqtSignal
from .worker import Worker
from .transcriber import Transcriber

class App:
    def __init__(self) -> None:
        self.transcriber = Transcriber()
        self.natalie = Natalie(transcriber=self.transcriber)
    
    def respond(self, message: str):
        #worker = Worker(self.natalie.respond, message)
        #worker.run()
        return self.natalie.respond(message)
    
    def listen(self):
        #worker = Worker(self.natalie.listen)
        #worker.run()
        return self.natalie.listen()
    
    def set_threshold(self, threshold: int):
        self.transcriber.set_threshold(threshold)
    
    def test_microphone(self):
        pass
    
    def set_device(self, index: int):
        self.transcriber.set_device(index)
    
    def get_devices(self):
        return self.transcriber.get_devices()
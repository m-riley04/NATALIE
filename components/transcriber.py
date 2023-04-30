import speech_recognition as sr
import openai, os, whisper

# OpenAI INIT
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "whisper-1"
openai.organization = "org-zy5w1ha0zbdZ975DOWCHpfVP"
openai.api_key = API_KEY
openai.Model.list()

class Transcriber:
    def __init__(self, device_index=0):
        self.microphone = sr.Microphone(device_index)
        self.recognizer = sr.Recognizer()
        self.threshold = 300
        
    def get_devices(self) -> list:
        '''Returns a list of the names of the available microphone devices.'''
        return self.microphone.list_microphone_names()
        
    def set_device(self, device_index:int):
        '''Sets the microphone device to be used for speech recognition based on an index.'''
        self.microphone.device_index = device_index
        
    def set_threshold(self, threshold:float=300):
        self.threshold = threshold
        
    def set_dynamic_thresholding(self, active:bool=True):
        self.recognizer.dynamic_energy_threshold = active
        
    def set_pause_threshold(self, threshold:float=0.8):
        self.recognizer.pause_threshold = threshold
        
    def set_background_listener(self, active:bool=True):
        return self.recognizer.listen_in_background()
        
    def listen(self):
        '''Returns the recognized text from the microphone.'''
        with self.microphone as microphone:
            #print("Adjusting for ambient noise...")
            #self.recognizer.adjust_for_ambient_noise(source=microphone, duration=2)
            self.recognizer.energy_threshold = self.threshold
            
            print("---- Listening... ----")
            return self.__transcribe(data=self.recognizer.listen(source=microphone))
    
    def record(self, duration=None):
        return self.recognizer.record(source=self.microphone, duration=duration)
       
    def print_devices(self):
        for i, device in enumerate(self.get_devices()):
            print(f"{i}) {device}")
        
    def __transcribe(self, data):
        '''Translates the AudioData using the OpenAI Whisper API'''
        print("Transcribing...")
        return self.recognizer.recognize_whisper(data, show_dict=True, model="tiny")['text']
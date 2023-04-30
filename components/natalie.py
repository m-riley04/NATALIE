import openai, os
from .transcriber import Transcriber
from .toolbelt import Toolbelt
from .tools import Tool

# OpenAI INIT
openai.organization = "org-zy5w1ha0zbdZ975DOWCHpfVP"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# Model Init
MODEL_ENGINE = "gpt-3.5-turbo"
PROMPT = """
            Please act as if you are NATALIE. NATALIE an artificial intelligence assistant who is designed to help the user with various tasks.
            These tasks include creating reminders for them, researching specific topics based on their input, helping them solve difficult problems,
            reading text and interpreting it's meaning, scanning images and converting them to text, and so on. 
            You perform your tasks in a way that is relatable to humans, but as efficiently and accurate as possible. You may add humor to your responses at your leisure.
            You are able to access the current Windows 10 operating system through the command line and powershell. You may use this to create reminders, alarms, and 
            any task that the user wishes to be performed.
        """

class Natalie:
    def __init__(self, transcriber=Transcriber()):
        self.model = MODEL_ENGINE
        self.prompt = PROMPT
        self.completion = None
        self.response = None
        self.transcriber = transcriber
        self.conversation = [{"role": "system", "content": PROMPT}]
        
        #self.respond(PROMPT, "system")
    
    def respond(self, prompt, role="user"):
        temp = self.conversation
        temp.append({"role": role, "content": prompt})
        self.completion = openai.ChatCompletion.create(
            model=self.model,
            messages=temp
        )
        self.response = self.completion.choices[0].message.content
        temp.append({"role": "assistant", "content": self.response})
        self.conversation = temp
        return self.response
    
    def listen(self):
        return self.transcriber.listen()
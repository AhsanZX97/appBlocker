from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial



class FirstKivy(App): 
    def runScript(self,instance,*args):
        instance.text = "test button"
    def build(self):
        runBtn = Button(text="Start Pomodore Timer!")
        runBtn.bind(on_press = partial(self.runScript,runBtn))
        return runBtn
    

FirstKivy().run()
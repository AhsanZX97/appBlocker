from kivy.app import App
from kivy.uix.label import Label

class FirstKivy(App): 
    def build(self):
        return Button(text="Start Pomodore Timer!")

FirstKivy().run()
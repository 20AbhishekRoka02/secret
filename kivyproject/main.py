import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        
        return Label(text='Hello world ' + chr(2764), font_size='20sp')
class BtnApp(App):
    pass

if __name__=="__main__":
    # BtnApp().run()
    MyApp().run()
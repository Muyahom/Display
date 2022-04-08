import kivy 
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.config import Config
 
Config.set('graphics', 'resizable', 1)
## Config.set('graphics', 'width', '400')
## Config.set('graphics', 'height', '400')
 
 
# Creating Layout class
class CalcGridLayout(GridLayout):
  
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
  
 # Creating App class
class CalculatorApp(App):
  
    def build(self):
        return CalcGridLayout()
  
# creating object and running it
calcApp = CalculatorApp()
calcApp.run()
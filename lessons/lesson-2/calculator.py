from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import toolkit

class Calculator(BoxLayout):
	def operation(self):
		x = float(self.form.text)
		y = float(self.buf)
		self.form.text = str(toolkit.func[self.action](x,y))
		
class CalculatorApp(App):
	def build(self):
		return Calculator()

CalculatorApp().run()

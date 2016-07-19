import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Test(BoxLayout):
	pass
	
class TestApp(App):
	def build(self):
		return Test()
		
TestApp().run()


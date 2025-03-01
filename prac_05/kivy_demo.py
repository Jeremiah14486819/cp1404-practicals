from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # This will load the layout from the kivy_layout.kv file automatically
        return BoxLayout(orientation='vertical')

if __name__ == "__main__":
    MyApp().run()

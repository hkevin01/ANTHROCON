from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MapScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Map and Transportation Info'))
        # Here you would integrate a mapping library
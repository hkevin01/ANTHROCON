from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Button(text='View Event Schedule', on_press=self.show_event_schedule))
        self.add_widget(Button(text='Transportation Info', on_press=self.show_transportation_info))

    def show_event_schedule(self, instance):
        self.manager.current = 'event_schedule'

    def show_transportation_info(self, instance):
        self.manager.current = 'transport_info'
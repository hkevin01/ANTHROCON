from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from utils.wait_times import get_wait_time

class EventSchedule(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Event Schedule'))
        
        # Example event data
        events = [
            {"name": "Opening Ceremony", "time": "10:00 AM"},
            {"name": "Keynote Speech", "time": "11:00 AM"},
        ]
        
        for event in events:
            event_label = Label(text=f"{event['name']} at {event['time']} - Wait time: {get_wait_time(event['name'])} mins")
            self.add_widget(event_label)
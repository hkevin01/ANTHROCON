from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from utils.authentication import login_user

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

    def login(self, email, password):
        try:
            user_data = login_user(email, password)
            self.manager.current = 'home'
        except ValueError as e:
            print(e)  # Handle invalid login
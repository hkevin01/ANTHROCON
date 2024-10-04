from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.email = TextInput(hint_text='Email')
        self.password = TextInput(hint_text='Password', password=True)
        self.login_btn = Button(text='Login')
        self.login_btn.bind(on_press=self.login)
        self.add_widget(self.email)
        self.add_widget(self.password)
        self.add_widget(self.login_btn)
    
    def login(self, instance):
        email = self.email.text
        password = self.password.text
        # Replace with your backend URL
        response = requests.post('https://yourbackend.com/api/login', data={'email': email, 'password': password})
        if response.status_code == 200:
            # Handle successful login
            pass
        else:
            # Handle login failure
            pass

class ConventionApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    ConventionApp().run()
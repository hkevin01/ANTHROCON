from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class ConventionApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    ConventionApp().run()
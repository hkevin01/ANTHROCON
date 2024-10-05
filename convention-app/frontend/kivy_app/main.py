from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen

class MyScreenManager(ScreenManager):
    pass

class ConventionApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    ConventionApp().run()
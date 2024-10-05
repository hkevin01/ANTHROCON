from kivy.uix.button import Button

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.1, 0.5, 0.8, 1)  # Example color
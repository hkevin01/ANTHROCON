from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class QRCodeWidget(Image):
    def __init__(self, qr_code_path, **kwargs):
        super().__init__(**kwargs)
        self.source = qr_code_path
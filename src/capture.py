from plyer import camera

def capture_image():
    camera.capture('path_to_save_image/image.png')
    # Process the captured image to decode QR
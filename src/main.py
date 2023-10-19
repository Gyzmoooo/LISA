from PIL import Image
from pyzbar import pyzbar
from time import sleep
import vlc
from picamera import PiCamera
import RPi.GPIO as GPIO

class LISA():
    def __init__(self):
        # GPIO setup
        self.qr_button, self.model_button, self.pause_button, self.backward_button = 4, 17, 27, 22
        GPIOlist = [self.qr_button, self.model_button, self.pause_button, self.backward_button]
        GPIO.setmode (GPIO.BCM)
        for i in range(4):
            GPIO.setup(GPIOlist[i], GPIO.IN, pull_up_down = GPIO.PUD_UP )
        start_state_qr = GPIO.input(self.qr_button)
        current_state_qr = GPIO.input(self.qr_button)

        # PiCamera setup
        self.cam = PiCamera()
        self.cam.start_preview()

        while start_state_qr == current_state_qr:
            sleep(0.01)
            current_state_qr = GPIO.input(self.qr_button)
            current_state_model = GPIO.input(self.model_button)
            if start_state_qr != current_state_qr:
                sleep(0.7)
                self.capture()
                self.play(self.decode())

    def capture(self):
        self.cam.capture('image.png')
        self.cam.stop_preview()
        self.cam.close()
        
    def decode(self):
        # QR decoding
        img = Image.open('image.png')
        self.output = pyzbar.decode(img)

        if not self.output: 
            print('error')
            return
        
        name = self.output[0][0].decode("utf-8") + '.mp4'
        return name

    def play(self, name):
        media = vlc.MediaPlayer(name)
        media.toggle_fullscreen()
        media.play()
        sleep(2)
        while media.is_playing():
            sleep(1)

l = LISA()

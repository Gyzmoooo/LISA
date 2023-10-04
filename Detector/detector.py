from PIL import Image
from pyzbar import pyzbar
from time import sleep
import vlc
from picamera import PiCamera
import RPi.GPIO as GPIO

class LISA():
    def __init__(self):
        # GPIO setup
        self.capture_button, self.forward_button, self.pause_button, self.backward_button = 4, 17, 27, 22
        GPIOlist = [self.capture_button, self.forward_button, self.pause_button, self.backward_button]
        GPIO.setmode (GPIO.BCM)
        for i in range(4):
            GPIO.setup(GPIOlist[i], GPIO.IN, pull_up_down = GPIO.PUD_UP )
        state = GPIO.input(self.capture_button)
        state1 = GPIO.input(self.capture_button)

        # PiCamera setup
        self.cam = PiCamera()
        self.cam.start_preview()

        while state == state1:
            sleep(0.01)
            state1 = GPIO.input(self.capture_button)
            if state != state1:
                sleep(0.7)
                self.capture()
                self.play()

    def capture(self):
        self.cam.capture('qr1.png')
        self.cam.stop_preview()
        self.cam.close()
        
    def play(self):
        # QR decoding
        img = Image.open('qr1.png')
        self.output = pyzbar.decode(img)

        if not self.output: 
            print('error')
            return
        
        name = self.output[0][0].decode("utf-8") + '.mp4'
        media = vlc.MediaPlayer(name)
        media.toggle_fullscreen()
        media.play()
        sleep(2)
        while media.is_playing():
            sleep(1)

if __name__ == '__main__':
  l = LISA()

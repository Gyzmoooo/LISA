from PIL import Image
from pyzbar import pyzbar
from time import sleep
import vlc
from picamera import PiCamera
import RPi.GPIO as GPIO

# Camera setup
cam = PiCamera()
cam.start_preview()
cam.rotation = 180

# GPIO setup
qr_button = 17

GPIO.setmode (GPIO.BCM)
GPIO.setup (qr_button, GPIO.IN, pull_up_down = GPIO.PUD_UP)

start_state_qr = GPIO.input(qr_button)

def play():
    # QR decoding
    img = Image.open('image.png')
    output = pyzbar.decode(img)

    if not output: 
        print('error')
        return
    
    name = output[0][0].decode("utf-8") + '.mp4'
    media = vlc.MediaPlayer(name)
    media.toggle_fullscreen()
    media.play()
    sleep(2)
    while media.is_playing():
        sleep(1)

def capture(cam):
    cam.capture("image.png")
    cam.stop_preview()

def get_start_state_qr(self):
    return self.start_state_qr

while True:
    try:
        current_state_qr = GPIO.input(qr_button)
        sleep(0.5)
        if start_state_qr != current_state_qr:
            sleep(0.7)
            capture(cam)
            play()
            cam.start_preview()
    except KeyboardInterrupt:
        print("cam closed")
        cam.stop_preview()
        cam.close()
    else:
        pass

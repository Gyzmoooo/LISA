from operator import truediv
from pathlib import Path
from pickle import TRUE
from PIL import Image
from pycoral.utils.edgetpu import make_interpreter
from pycoral.adapters import common
from pycoral.adapters import classify
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import cv2
from rembg import remove
import os

# define pin GPIO + setup
capturebutton = 4
forwardbutton = 17
pausebutton = 27
backwardbutton = 22
GPIO.setmode (GPIO.BCM)
GPIO.setup (capturebutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup (forwardbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup (pausebutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup (backwardbutton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
state = GPIO.input(capturebutton) # stato iniziale del bottone

# define base_folder
base_folder = Path(__file__).parent.resolve()

# camera setting
cam = PiCamera()
cam.resolution = (1920, 1080) # da modificare per la risoluzione della picam

# image classifier setting
label_file = base_folder/'model/labels.txt'
model_file = base_folder/'model/model_edgetpu.tflite'
interpreter = make_interpreter(f"{model_file}")
interpreter.allocate_tensors()
size = common.input_size(interpreter)

def classifier(): # returns the video to play
    # takes a photo
    cam.capture(Path(f"{base_folder}/{'foto'}/{'foto.png'}"))   
    
    # process filtering
    input_path = 'foto.png' # input image name
    filtered = 'foto_cropped.png'  # output image name
    input = Image.open(input_path) # load image
    output = remove(input) # remove background
    output.save(filtered) # save image
    os.remove(Path(f"{base_folder}/{'foto'}/{'foto.png'}"))

    # classifies the filtered photo
    image = Image.open('foto_cropped.png').convert('RGB').resize(size, Image.Resampling.LANCZOS)
    common.set_input(interpreter, image)
    interpreter.invoke()
    classes = classify.get_classes(interpreter, top_k=1)
    os.remove(Path(f"{base_folder}/{'foto'}/foto_cropped.png"))
    for c in classes:
        return(str((c.id)) + '.mp4') #returns the name of the video

# skip forward (10s)
def skip_forward(cap):
    current_pos = cap.get(cv2.CAP_PROP_POS_MSEC)
    new_pos = current_pos + 5000
    cap.set(cv2.CAP_PROP_POS_MSEC, new_pos)

# play/pause
def playpause(cap):
    while True:
        state1 = GPIO.input(capturebutton)        
        state2 = GPIO.input(forwardbutton)
        state3 = GPIO.input(pausebutton)
        state4 = GPIO.input(backwardbutton)
        if state1 != state or state3 != state:
            sleep(0.7)
            break
        if state2 != state:
            sleep(0.7)
            skip_forward(cap)
        if state4 != state:
            sleep(0.7)
            skip_backward(cap)  

# skip backward (10s)
def skip_backward(cap):
    current_pos = cap.get(cv2.CAP_PROP_POS_MSEC)
    new_pos = current_pos - 5000
    cap.set(cv2.CAP_PROP_POS_MSEC, new_pos)
    
# reproduce video
def start_video(path):
    # video setup
    cap = cv2.VideoCapture(path)
    window_name = 'video'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while (cap.isOpened()):
        # start video
        ret, img = cap.read()
        if ret == True:
            cv2.imshow(window_name, img)
            # read button
            state1 = GPIO.input(capturebutton)        
            state2 = GPIO.input(forwardbutton)
            state3 = GPIO.input(pausebutton)
            state4 = GPIO.input(backwardbutton)
            if state1 != state:  # capture button now interrupts video
                sleep(0.7)
                break
            if state2 != state:
                sleep(0.7)
                skip_forward(cap)
            if state3 != state:
                sleep(0.7)
                playpause(cap)
            if state4 != state:
                sleep(0.7)
                skip_backward(cap)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

nImg = 0
try: 
    while True:
        # read button data
        sleep(0.01)
        state1 = GPIO.input(capturebutton)
        
        if state1 != state:
            sleep(0.7)
            start_video(classifier())

except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyAllWindows()

from rembg import remove    
from PIL import Image
import os
from pathlib import Path

def removebg(input_path, output_path):
    input = Image.open(input_path) # load image
    output = remove(input) # remove background
    output.save(output_path) # save image

# define base_folder
base_folder = Path(__file__).parent.resolve()

counter = 1
for i in os.listdir(Path(f"{base_folder}/{'foto'}")):
    n = "image" + str(counter) + ".png"
    input_photo = "foto/" + i
    output_photo = "foto/" + n 
    removebg(input_photo, output_photo)
    os.remove(input_photo)
    counter += 1

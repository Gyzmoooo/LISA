from PIL import Image, ImageDraw
from pycoral.adapters import common
from pycoral.adapters import detect
from pycoral.utils.edgetpu import make_interpreter

def draw_objects(draw, objs):
  for obj in objs:
    bbox = obj.bbox
    draw.rectangle([(bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax)],
                   outline='red')
    draw.text((bbox.xmin + 10, bbox.ymin + 10),
              '%s\n%.2f' % ( obj.score),
              fill='red')


def detection(model, input, output, threshold=0.5, count=1):
  interpreter = make_interpreter(model)
  interpreter.allocate_tensors()

  image = Image.open(input)
  tensor, scale = common.set_resized_input(
      interpreter, image.size, lambda size: image.resize(size, Image.ANTIALIAS))

  for tensor in range(count):
    interpreter.invoke()
    objs = detect.get_objects(interpreter, threshold, scale)
    
  if output:
    image = image.convert('RGB')
    draw_objects(ImageDraw.Draw(image), objs)
    image.save(output)

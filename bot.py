import pytesseract
import time
from PIL import Image
from pymouse import PyMouse
import quickgrab

m = PyMouse()

while True:
    try:
        quickgrab.screengrab()
        operation = pytesseract.image_to_string(Image.open("./screen.png"))
        operation = operation.replace(":", "=").replace(" ", "").replace("(", "1").replace("S", "5").replace("B", "8").replace("O", "0")
        print(operation)
        operation = operation.split("=")
        left = operation[0]
        right = operation[1]
        left = (eval(left.replace("x", "*").replace("X", "*").replace("l", "/")))
        right = eval(right)
        if left == right:
            m.click(873, 934)
        else:
            m.click(1039, 934)
        time.sleep(0.4)
    except NameError:
        m.click(873, 934)
        time.sleep(0.4)

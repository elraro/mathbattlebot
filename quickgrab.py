import pyscreenshot as imagegrab


def screengrab():
    box = (688,382,1232,606)
    im = imagegrab.grab(box)
    im.save("screen.png", 'PNG')
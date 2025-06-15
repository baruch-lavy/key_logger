from pynput.mouse import Controller

def controlMouse():
    mouse = Controller
    mouse.position = (10,20)

controlMouse()
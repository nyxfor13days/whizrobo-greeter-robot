import gpiozero
from lib.motion import Motion
from lib.speak import Speak


class Main:
    def __init__(self):
        if Motion():
            Speak("Hello")


if __name__ == '__main__':
    Main()

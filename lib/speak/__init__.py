import pyttsx3


class Speak(object):
    def __init__(self, text, rate=125, volume=1.0, voice='english-us'):
        self.engine = pyttsx3.init()

        self.setRate(rate)
        self.setVolume(volume)
        self.setVoice(voice)

        self.engine.say(text)
        self.engine.runAndWait()

    def setRate(self, rate):
        self.engine.setProperty('rate', rate)

    def setVolume(self, volume):
        self.engine.setProperty('volume', volume)

    def setVoice(self, voice):
        self.engine.setProperty('voice', voice)

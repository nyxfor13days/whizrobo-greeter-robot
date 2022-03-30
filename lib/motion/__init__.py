import json
from gpiozero import MotionSensor

with open('data/pins.json') as file:
    pins = json.load(file)


def Motion(threshold=0.5):
    sensor = MotionSensor(pins["motion_sensor"], threshold=threshold)
    sensor.wait_for_motion()

    if sensor.motion_detected:
        print("Motion detected")
        return True

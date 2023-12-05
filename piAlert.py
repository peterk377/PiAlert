from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (1920, 1080)
filename = "{0:%X}  {0:%d}-{0:%m}-{0:%Y}".format(datetime.now()) + ".h264"
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
    print("Stopped recording")
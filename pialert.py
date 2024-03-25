from gpiozero import MotionSensor
from gpiozero import PiCamera
from dateTime import dateTime
from encode import encode

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (1920, 1080)
filename = "{0:%X}-{0:%d}-{0:%y}".format(dateTime.now()) + ".h264"

while True:
  pir.wait_for_motion()
  print("Motion Detected")
  camera.start_recording(filename)
  pir.wait_for_no_motion()
  encode(filename)
  camera.stop_recording()
  print("Stopped Recording")
import subprocess
import time
from picamera import PiCamera
from datetime import datetime
from database import newAlert, login
from gpiozero import MotionSensor

def convert_to_mp4(input_file):
    output_file = input_file.replace('.h264', '.mp4')
    cmd = f'MP4Box -add {input_file} {output_file}'
    subprocess.call(cmd, shell=True)
    return output_file

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (1920, 1080)

userID = ''
email = ''
whatsapp = ''

print("Please enter your username.")
username = input()
print("Please enter your password.")
password = input()

userID, email, whatsapp = login(username, password, whatsapp)
print(userID)
print(whatsapp)

while True:
    pir.wait_for_motion()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"video_{timestamp}"    
    print("Motion Detected")
    camera.start_recording(filename + ".h264")
    time.sleep(3)
    print("Motion Stopped")
    camera.stop_recording()
    mp4 = convert_to_mp4(f"{filename}.h264")
    newAlert(userID, email, whatsapp, mp4)
    time.sleep(20)
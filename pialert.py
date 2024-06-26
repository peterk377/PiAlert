import subprocess
import time
from picamera import PiCamera
from datetime import datetime
from database import newAlert, login
from gpiozero import MotionSensor
from ledLight2 import lightOn, lightOff, lightLoggedIn, lightProgramOn, flash

lightOff()

def convert_to_mp4(input_file):
    output_file = input_file.replace('.h264', '.mp4')
    cmd = f'MP4Box -add {input_file} {output_file}'
    subprocess.call(cmd, shell=True)
    return output_file

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (640, 480)

userID = ''
email = ''
whatsapp = ''

x = 1
while(x == 1):

    flash(5)
    print("Please enter your username.")
    username = input()
    print("Please enter your password.")
    password = input()

    userID, email, whatsapp, x = login(username, password, whatsapp)
    print(userID)
    print(email)
    whatsapp = "+353" + whatsapp[1:]
    print(whatsapp)

flash(3)

while True:
    pir.wait_for_motion()
    flash(1)
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
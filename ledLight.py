import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time
import threading

# Function to simulate LED turning on
def led_on(pin):
    print(f"Turning on LED on pin {pin}")

# Function to simulate LED turning off
def led_off(pin):
    print(f"Turning off LED on pin {pin}")

# Define GPIO pins
ledChannel4 = 5
ledChannel20 = 20
ledChannel21 = 21
pirChannel = 4

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledChannel4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledChannel20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ledChannel21, GPIO.OUT, initial=GPIO.LOW)

# Initialize Motion Sensor
pir = MotionSensor(pirChannel)

# Function to start and stop LED pattern
isStarted = False
def startLEDs():
    global isStarted
    isStarted = True
    while isStarted:
        led_on(ledChannel4)
        led_off(ledChannel20)
        led_off(ledChannel21)
        time.sleep(0.3)
        led_off(ledChannel4)
        led_on(ledChannel20)
        led_off(ledChannel21)
        time.sleep(0.3)
        led_off(ledChannel4)
        led_off(ledChannel20)
        led_off(ledChannel21)
        time.sleep(0.3)

def stopLEDs():
    global isStarted
    isStarted = False
    led_off(ledChannel4)
    led_off(ledChannel20)
    led_off(ledChannel21)

try:
    while True:
        print("Waiting for motion..")
        pir.wait_for_motion()
        thread = threading.Thread(target=startLEDs)
        thread.start()
        print("Motion Detected..")
        pir.wait_for_no_motion()
        print("No motion detected")
        stopLEDs()
        thread.join()
except KeyboardInterrupt:
    stopLEDs()
finally:
    GPIO.cleanup()  # Ensure GPIO cleanup

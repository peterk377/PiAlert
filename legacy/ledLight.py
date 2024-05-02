import RPi.GPIO as GPIO
from gpiozero import MotionSensor
import time
import threading

# Define LED states
LED_STATE_OFF = 0
LED_STATE_GREEN_FLASH = 1
LED_STATE_GREEN_CONSTANT = 2
LED_STATE_RED = 3

# Initialize LED state
led_state = LED_STATE_OFF

# Function to simulate LED turning on
def led_on(pin):
    GPIO.output(pin, GPIO.HIGH)

# Function to simulate LED turning off
def led_off(pin):
    GPIO.output(pin, GPIO.LOW)

# Define GPIO pins
ledChannel4 = 4
pirChannel = 26

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledChannel4, GPIO.OUT, initial=GPIO.LOW)

# Initialize Motion Sensor
pir = MotionSensor(pirChannel)

# Function to control LED based on state
def control_led():
    if led_state == LED_STATE_OFF:
        led_off(ledChannel4)
    elif led_state == LED_STATE_GREEN_FLASH:
        led_on(ledChannel4)
        time.sleep(0.5)  # Flash interval
        led_off(ledChannel4)
        time.sleep(0.5)
    elif led_state == LED_STATE_GREEN_CONSTANT:
        led_on(ledChannel4)
    elif led_state == LED_STATE_RED:
        led_on(ledChannel4)

# Function to check login status
def login(username, password):
    import os
    import pymongo
    from dotenv import load_dotenv

    load_dotenv()

    url = os.getenv('DATABASE_URL')
    myclient = pymongo.MongoClient(url)
    db = myclient["pialert"]

    user_collection = db["user"]

    query = {"username": username, "password": password}

    x = user_collection.find(query)

    for result in x:
        userID = result['userID']
        email = result['email']
        whatsapp_number = result['whatsapp']

    if x.count() > 0:
        return True, userID, email, whatsapp_number
    else:
        return False, None, None, None

# Function to start and stop LED pattern
isStarted = False
def startLEDs():
    global isStarted
    isStarted = True
    while isStarted:
        control_led()

def stopLEDs():
    global isStarted
    isStarted = False
    led_off(ledChannel4)

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
        # Determine LED state based on login status
        logged_in, userID, email, whatsapp_number = login("your_username", "your_password")
        if logged_in:
            led_state = LED_STATE_GREEN_CONSTANT
        else:
            led_state = LED_STATE_GREEN_FLASH
        thread.join()
except KeyboardInterrupt:
    stopLEDs()
finally:
    GPIO.cleanup()  # Ensure GPIO cleanup

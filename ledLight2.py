import RPi.GPIO as GPIO
import time

# Set up GPIO outside functions
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)

def lightOn(): #light powered on
    GPIO.output(2, GPIO.HIGH)

def lightOff(): # light powered off
    GPIO.output(2, GPIO.LOW)

def lightProgramOn(): #program started
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)


def lightLoggedIn(): #logged into an account
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(2, GPIO.LOW)

def flash(x):
    y=0
    while(x > y):
        GPIO.output(2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(2, GPIO.LOW)
        time.sleep(0.5)
        y=y+1
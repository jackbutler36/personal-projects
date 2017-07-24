import RPi.GPIO as GPIO
import time

redLight = 18
greenLight = 16
button = 36

GPIO.setmode(GPIO.BCM) # GPIO.BOARD

# Declare I/O with GPIO.OUT or GPIO.IN
GPIO.setup(redLight, GPIO.OUT)
GPIO.setup(greenLight, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize light state either GPIO.HIGH or GPIO.LOW
GPIO.output(redLight, GPIO.HIGH)
GPIO.output(greenLight, GPIO.LOW)

try:
    while 1:
        time.sleep(1)
        # Check if button is pressed
        if GPIO.input(button):
            GPIO.output(greenLight, GPIO.HIGH)
            GPIO.output(redLight, GPIO.LOW)
        else:
            GPIO.output(redLight, GPIO.HIGH)
            GPIO.output(greenLight, GPIO.LOW)
        
        
except KeyboardInterrupt:
    GPIO.cleanup()
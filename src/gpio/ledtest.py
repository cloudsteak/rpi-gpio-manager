import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

print("\n***********************************\n")
# Get Pin for LED
LED = os.getenv('LED_PIN')
LED = int(LED[1:])
print("Get LED PIN:", LED)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)

try:
    print("Start blinking in every 0.5 second. (Terminate script running to stop it. CTRL + c)")
    while True:
        GPIO.output(LED,GPIO.HIGH) # Turn on
        time.sleep(0.5) # Wait for a second
        GPIO.output(LED,GPIO.LOW) # Turn Off
        time.sleep(0.5) # Wait for a second
except KeyboardInterrupt:
    GPIO.output(LED,GPIO.HIGH) # Turn Off
    print("\nStopped by the user")
    print("\n***********************************\n")
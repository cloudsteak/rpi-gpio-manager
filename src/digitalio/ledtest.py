import digitalio
import board
import time
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

print("\n***********************************\n")
# Get Pin for LED
LED = os.getenv('LED_PIN')
print("Get LED:", LED)
led_pin = digitalio.DigitalInOut(getattr(board, LED))
led_pin.direction = digitalio.Direction.OUTPUT
led_pin.value = True


try:
    print("Start blinking in every 0.5 second. (Terminate script running to stop it. CTRL + c)")
    while True:
        led_pin.value = False # Turn on
        time.sleep(0.5) # Wait for a second
        led_pin.value = True # Turn Off
        time.sleep(0.5) # Wait for a second
except KeyboardInterrupt:
    led_pin.value = True # Turn Off
    print("\nStopped by the user")
    print("\n***********************************\n")
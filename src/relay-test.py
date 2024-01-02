import board
import digitalio
import os
from dotenv import load_dotenv

# Get environment variables
load_dotenv()

RELAY_CHANNEL_COUNT=os.getenv('RELAY_CHANNEL_COUNT')

print("\n***********************************\n")
# Get Pin for relay 1
PIN1 = os.getenv('RELAY_PIN_1')
print("Get PIN1:", PIN1)
relay_pin_1 = digitalio.DigitalInOut(getattr(board, PIN1))



# On/Off Pin1
relay_pin_1.direction = digitalio.Direction.OUTPUT
print("PIN1 (",PIN1, ") value:",relay_pin_1.value)
relay_pin_1.value = True
print("PIN1 (",PIN1, ") value:",relay_pin_1.value)

if int(RELAY_CHANNEL_COUNT) > 1: 
    # Get Pin for relay 2
    print("\n***********************************\n")
    PIN2 = os.getenv('RELAY_PIN_2')
    print("Get PIN2:", PIN2)
    relay_pin_2 = digitalio.DigitalInOut(getattr(board, PIN2))

    # On/Off Pin2
    relay_pin_2.direction = digitalio.Direction.OUTPUT
    print("PIN1 (",PIN2, ") value:",relay_pin_2.value)
    relay_pin_2.value = True
    print("PIN1 (",PIN2, ") value:",relay_pin_2.value)
    print("\n***********************************\n")
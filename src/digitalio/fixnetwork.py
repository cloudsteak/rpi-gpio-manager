import board
import digitalio



def switch_relay(direction, pin1, pin2, pin_count):
    relay_pin_1 = digitalio.DigitalInOut(getattr(board, pin1))  # Get Pin1
    relay_pin_1.direction = digitalio.Direction.OUTPUT
    if direction == "ON":
        relay_pin_1.value = False

    if direction == "OF":
        relay_pin_1.value = True

    if int(pin_count) > 1:
        relay_pin_2 = digitalio.DigitalInOut(getattr(board, pin2))  # Get Pin2
        relay_pin_2.direction = digitalio.Direction.OUTPUT

        if direction == "ON":
            relay_pin_2.value = False

        if direction == "OF":
            relay_pin_2.value = True

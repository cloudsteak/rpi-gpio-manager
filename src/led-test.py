import digitalio
import board

pin = digitalio.DigitalInOut(board.LED)
print(pin.value)
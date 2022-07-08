import time
import board
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.GP21)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    print(switch.value)
    time.sleep(1)  # debounce delay
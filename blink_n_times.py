import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1 = 11

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid input for 'n'. Please provide an integer.")
        sys.exit(1)
else:
    n = 5

ITER_COUNT = n * 2  # Two iterations per blink

while ITER_COUNT > 0:
    ITER_COUNT -= 1
    GPIO.output(pin1, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin1, GPIO.LOW)
    sleep(1)

GPIO.cleanup()


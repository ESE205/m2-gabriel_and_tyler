import RPi.GPIO as GPIO
import time
import argparse
import sys

# Set up command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="print debug info")
parser.add_argument("-r", "--rate", type=int, default=1, help="blink rate in seconds")
parser.add_argument("-t", "--time", type=int, default=10, help="program run time in seconds")
args = parser.parse_args()

# Set up GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 16
SWITCH_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize variables
start_time = time.time()
iterations = 0
state = False

# Main loop
while time.time() - start_time < args.time:
    # Check switch state
    if GPIO.input(SWITCH_PIN) == GPIO.HIGH:
        # Toggle state
        state = not state
        GPIO.output(LED_PIN, state)
        # Debug info
        if args.debug:
            print(f"{time.ctime()}\t{iterations}\t{'on' if state else 'off'}")
        # Write to file
        with open("output.txt", "a") as f:
            f.write(f"{time.ctime()}\t{'on' if state else 'off'}\n")
        # Wait for the next cycle
        time.sleep(args.rate)
        iterations += 1
    else:
        GPIO.output(LED_PIN, False)

# Clean up
GPIO.cleanup()








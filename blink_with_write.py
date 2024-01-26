import time
import argparse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED_PIN = 17 
GPIO.setup(LED_PIN, GPIO.OUT)

parser = argparse.ArgumentParser(description="LED Blinking")
parser.add_argument("switch_state", type=int, help="Switch state (0 for off, 1 for on)")
parser.add_argument("blink_rate", type=int, help="Blink rate in seconds")
parser.add_argument("program_duration", type=int, help="Program duration in seconds")
parser.add_argument("-debug", action="store_true", help="Enable debug mode")

args = parser.parse_args()

start_time = time.time()
iterations = 0

try:
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        
        if elapsed_time >= args.program_duration:
            break

        if args.switch_state == 1:
            led_state = GPIO.HIGH if int(elapsed_time) % args.blink_rate == 0 else GPIO.LOW
        else:
            led_state = GPIO.LOW

        if args.debug:
            print(f"{time.ctime()}\t{iterations}\t{led_state}")

        GPIO.output(LED_PIN, led_state)

        time.sleep(1)
        iterations += 1

finally:
    GPIO.cleanup()

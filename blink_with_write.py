import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_PIN = 16
LED_IS_ON = False
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

DEBUG = '-debug' in sys.argv
BLINK_RATE = int(sys.argv[sys.argv.index('-blink_rate')+1]) if '-blink_rate' in sys.argv else 1
RUN_TIME = int(sys.argv[sys.argv.index('-run_time')+1]) if '-run_time' in sys.argv else 60

start_time = time.time()

with open('data.txt', 'w') as data:
    i = 0
    while time.time() - start_time < RUN_TIME:
        GPIO.output(LED_PIN, LED_IS_ON)
        data.write(f'{time.time():1.0f}\t{LED_IS_ON}\n')
        if DEBUG:
            print(f'{time.asctime()}\t{i}\tLED is {"on" if LED_IS_ON else "off"}')
        LED_IS_ON = not LED_IS_ON
        time.sleep(BLINK_RATE)
        i += 1

GPIO.cleanup()

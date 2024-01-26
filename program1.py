import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

switch_pin = 11  # Change this to the actual pin number connected to the switch
led_pin = 13  # Change this to the actual pin number connected to the LED

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        if GPIO.input(switch_pin) == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        sleep(0.1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

switch_pin = 24 
led_pin = 16  

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        if GPIO.input(switch_pin) == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        sleep(0.1)  

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

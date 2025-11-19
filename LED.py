import RPi.GPIO as GPIO
import time

LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


try:
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED is ON")
    time.sleep(5)
except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleanup complete")
    
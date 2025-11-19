import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)

if GPIO.input(22)--GPIO.HIGH:
    print("Motion detected!")
    else:
        print("no motion,")
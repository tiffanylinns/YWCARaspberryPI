from gpiozero import LED
from threading import Thread #Multi-threading, multi-tasking
import time

led1 = LED(27)
led2 = LED(17)

def blink_led1():
    while True:
        led1.on()
        time.sleep(0.5)
        led1.off()
        time.sleep(0.5)
        
def blink_led2():
    while True:
        led2.on()
        time.sleep(1)
        led2.off()
        time.sleep(1)

#Create threads
t1 = Thread(target=blink_led1)
t2 = Thread(target=blink_led2)

#Start threads
t1.start()
t2.start()


from gpiozero import InputDevice, LED
from time import sleep

light_sensor =  InputDevice(25)
led = LED(27)
    
while True:
    if light_sensor.is_active:
        led.off()
    else:
        led.on()
    sleep(1)
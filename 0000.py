from gpiozero import LED
from time import sleep
lg=LED(1)
lr=LED(17)
while True:
    lg.on(10)
    sleep(1)
    lg.off(10)
    sleep(1)
    lr.on()
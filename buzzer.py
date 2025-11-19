from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(25)

for i in range(5):
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)
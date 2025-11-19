from gpiozero import LED, Button
from time import sleep

green = LED(17)
button = Button(12)
red = LED(27)

while True:
    #green.on()
    #sleep(1)
    #green.off()
    #
    sleep(1)
    button.wait_for_press()
    green.toggle()
    sleep(0.5)

    #red.on()
    #sleep(1)
    #red.off()
    #sleep(1)
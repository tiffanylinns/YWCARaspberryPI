from gpiozero import LED,Button,MotionSensor
from time import sleep

pir = MotionSensor(22)
led1 = LED(17)                                                                                                                                17)
led2 = LED(27)
button = Button(12)

try:
    while True:
        if pir.motion_detected:
            print("Motion detected! Turning on LED 1.")
            led1.on()
            else:
                led1.off()
                
        if button.is_active:
            print("Button pressed! Turning on LED 2.")
             led2.on()
          else:
              led2.off()
              sleep(0.1)
            
except KeyboardInterrupt:
    print("Script interrupted. Cleaning up GPIO pins.")
    led1.close()
    led2.close()
       
                                                                                                                                                                                                                                                                                      
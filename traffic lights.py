from gpiozero import Tona1Buzzer, Button, TrafficLights
from time import sleep

buzzer=Tona1Buzzer(25)
button= Button( 23)
traffic_lights=Trafficlights(17,27,22)

try:
	while True:
		if button.is_pressed:
			print("Pedestrian crossing activated!")
			buzzer.play(440)
			traffic_lights.red.on
			traffic_lights.yellow.off
		    traffic_lights.green.off
		    sleep(5)
		    buzzer.stop()
		    traffic_lights.red.off()
		else:
			traffic_lights.green.on()
			traffic_lights.yellow.off()
			traffic_lights.red.off()
		    sleep(10)
		    
		    traffic_lights.green.off()
		    traffic_lights.yellow.on()
		    sleep(8)
		    
		    traffic_lights.yellow.off()
		    traffic_lights.red.off()
		    
except KeyboardInterrupt:
	print("Program interrupted")
	
finally:
	traffic light.close()
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    
		    

++++++++++

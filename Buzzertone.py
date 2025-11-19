from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep


buzzer = TonalBuzzer(25)


buzzer.play(Tone("F4"))
sleep(1)
buzzer.stop()
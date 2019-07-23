from gpiozero import LED, Button, Buzzer
from time import sleep
import time
import datetime

buzzer = Buzzer(15)
button = Button(21)
light = LED(25)

global people
global counter

button.when_pressed =light.on
button.when_released = light.off
counter = 0
people = 0
def countdown(n):
    while n > 0:
        i="a"
        button.wait_for_press()
        buzzer.on()
        sleep(1)
        buzzer.off()
        print("Pressed")
        print("current date and time: ", datetime.datetime.now())
        if i =="a":
            print(n)
            n = n + 1
#            people.save_value({'value':n})
        
            

        
while True:
    
    countdown(1)
from gpiozero import LED, Button, Buzzer
from time import sleep
import time
import datetime

buzzer = Buzzer(15)
button = Button(21)
light = LED(25)


button.when_pressed = light.on
button.when_released = light.off

def countdown(no_of_students):
    print ("connected")
    #while no_of_students > 0:
    button.wait_for_press()
    buzzer.on()
    sleep(1)
    buzzer.off()
    
#    print("Pressed")
#    print("Current date and time: ",datetime.datetime.now())
#    print(no_of_students)
    no_of_students = no_of_students + 1
    
    return no_of_students 
    
countdown(0)
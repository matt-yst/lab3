#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors
#The configuration for sensor 1
SOUND = sound.Sound(duration=0.5, pitch="A5", volume=100)
TOUCH_SENSOR = TouchSensor(1)

#The configuration for sensor 2
SOUND2 = sound.Sound(duration=0.1, pitch="A4", volume=100)
TOUCH_SENSOR2 = TouchSensor(3)

#The sound produced by the combination of both sensors
SOUND3 = sound.Sound(duration=0.1, pitch="B4", volume=80)

wait_ready_sensors() # Note: Touch sensors actually have no initialization time


def play_sound():
    "Play a single note for the first sensor."
    SOUND.play()
    SOUND.wait_done()

def play_sound2():
    "Play another note for the second sensor"
    SOUND2.play()
    SOUND2.wait_done()

def play_sound3():
    "Play a different note when both sensors are pressed together"
    SOUND3.play()
    SOUND3.wait_done()
    
def play_sound_on_button_press():
    "In an infinite loop, play a single note when one touch sensor is pressed or both."
    try:
        
        while True:
            if (TOUCH_SENSOR.is_pressed() and TOUCH_SENSOR2.is_pressed()):
                print('test')
                play_sound3()
                
                
            elif TOUCH_SENSOR2.is_pressed():
                play_sound2()
                print('sensor2')
            elif TOUCH_SENSOR.is_pressed():
                play_sound()
                print('sensor1')
                
        
        
    except BaseException:
        print("exit")# capture all exceptions including KeyboardInterrupt (Ctrl-C)
        exit()


if __name__=='__main__':
    
    play_sound()

    # TODO Implement this function
    play_sound_on_button_press()

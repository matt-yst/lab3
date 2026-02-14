from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time

# -------------------- SENSORS AND MOTORS --------------------

# Sensors
TS1 = TouchSensor(1)
TS2 = TouchSensor(2)
US = EV3UltrasonicSensor(3)
MOTOR = Motor("D")

# Make sure that all of our sensors are ready
# wait_ready_sensors()
# ^ Absolutely do not put the piece of code above lol

MOTOR.set_limits(power=70)


# -------------------- CONSTANTS AND VARIABLES --------------------

# Notes
NOTE1 = sound.Sound(duration=0.2, pitch="C6", volume=70)
NOTE2 = sound.Sound(duration=0.2, pitch="A6", volume=70)
NOTE3 = sound.Sound(duration=0.2, pitch="E6", volume=70)
NOTE4 = sound.Sound(duration=0.2, pitch="G6", volume=70)

ts1_on = False
ts2_on = False
us_on = False
drum_on = False

# -------------------- FUNCTIONS --------------------

def playDrum():
    if drum_on:
        MOTOR.set_position(0)
        #print(motor.get_position())
        time.sleep(0.25)
        MOTOR.set_position(-110)
        #print(motor.get_position())
        time.sleep(0.25)


# -------------------- MAIN LOOP --------------------
while (True):
    # Finding all the sensor startes
    ts2_on = TS2.is_pressed()
    time.sleep(0.07)
    ts1_on = TS1.is_pressed()
    time.sleep(0.05)

    playDrum()
    
    if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
        us_on = True
    else:
        us_on = False

    if (not ts1_on and ts2_on and not us_on):
        # Note 1 plays
        NOTE1.play()
        NOTE1.wait_done()

    elif (not ts1_on and ts2_on and us_on):
        # Note 2 plays
        NOTE2.play()
        NOTE2.wait_done()   

    elif (ts1_on and not ts2_on and not us_on):
        # Note 3 plays
        print("Note 3")
        NOTE3.play()
        NOTE3.wait_done()  
   
    elif (ts1_on and not ts2_on and us_on):
        # Note 4 plays
        print("Note 4")
        NOTE4.play()
        NOTE4.wait_done()    
   
    elif (ts1_on and ts2_on and not us_on):
        # Emergency Stop
        print("Emergency Stop")
        drum_on = False

    elif (ts1_on and ts2_on and us_on):
        # Drum toggle
        print("Drum Toggle")
        drum_on = True
    
    time.sleep(0.07)
        

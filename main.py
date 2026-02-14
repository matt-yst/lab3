from utils import sound
from utils.brick import TouchSensor, Motor, EV3UltrasonicSensor, wait_ready_sensors
import time
import threading

# -------------------- SENSORS AND MOTORS --------------------

# Sensors
TS1 = TouchSensor(1)
TS2 = TouchSensor(2)
US = EV3UltrasonicSensor(3)
MOTOR = Motor("D")

MOTOR.set_limits(power=70)


# -------------------- CONSTANTS AND VARIABLES --------------------

# Notes
NOTE1 = sound.Sound(duration=0.1, pitch="C6", volume=70)
NOTE2 = sound.Sound(duration=0.1, pitch="A6", volume=70)
NOTE3 = sound.Sound(duration=0.1, pitch="E6", volume=70)
NOTE4 = sound.Sound(duration=0.1, pitch="G6", volume=70)

is_ts1_on = False
is_ts2_on = False
is_us_on = False
is_drum_on = False
is_emergency = False

# -------------------- FUNCTIONS --------------------

def playDrum():
    if is_drum_on:
        MOTOR.set_position(0)
        time.sleep(0.25)
        MOTOR.set_position(-110)
        time.sleep(0.25)
        
def checkSensors():
    # Finding all the sensor startes
    ts2_on = TS2.is_pressed()
    time.sleep(0.07)
    ts1_on = TS1.is_pressed()
    time.sleep(0.05)
    
    if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
        us_on = True
    else:
        us_on = False

def drum():
    while (True):
        
        is_ts2_on = TS2.is_pressed()
        time.sleep(0.07)
        is_ts1_on = TS1.is_pressed()
        time.sleep(0.05)

        if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
            is_us_on = True
        else:
            is_us_on = False

        # Check if sensor conditions are met for drumming
        if (is_ts1_on and is_ts2_on and is_us_on):
            # Drum toggle
            print("Drum Toggle")
            is_drum_on = True
            print("isDrum on?: ", is_drum_on)


def notes():
    while (True):
        # Check the status of the sensors
        is_ts2_on = TS2.is_pressed()
        time.sleep(0.07)
        is_ts1_on = TS1.is_pressed()
        time.sleep(0.05)

        if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
            is_us_on = True
        else:
            is_us_on = False

        if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
            is_us_on = True
        else:
            is_us_on = False
            
        
        if (not is_ts1_on and not is_ts2_on and is_us_on):
            # Note 1 plays
            print("Note 1")
            NOTE1.play()
            NOTE1.wait_done()
        
        if (not is_ts1_on and is_ts2_on and not is_us_on):
            # Emergency stop
            print("Emergency Stop")
            is_drum_on = False
            isEmergency = not isEmergency
            

        elif (not is_ts1_on and is_ts2_on and is_us_on):
            # Note 2 plays
            print("Note 2")
            NOTE2.play()
            NOTE2.wait_done()   

        elif (is_ts1_on and not is_ts2_on and not is_us_on):
            # Note 3 plays
            print("Note 3")
            NOTE3.play()
            NOTE3.wait_done()  
    
        elif (is_ts1_on and not is_ts2_on and is_us_on):
            # Note 4 plays
            print("Note 4")
            NOTE4.play()
            NOTE4.wait_done()    

        


# -------------------- MAIN --------------------

t1 = threading.Thread(target=drum, args=())
t2 = threading.Thread(target=notes, args=())

t1.start()
t2.start()
t1.join()
t2.join()


# while (True):
#     is_ts2_on = TS2.is_pressed()
#     time.sleep(0.07)
#     is_ts1_on = TS1.is_pressed()
#     time.sleep(0.05)
    
#     if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
#         is_us_on = True
#     else:
#         is_us_on = False


#     if (is_ts1_on and is_ts2_on and not is_us_on):
#             # Emergency Stop
#             print("Emergency Stop")
#             isEmergency = not isEmergency


#     while (not isEmergency):
#         is_ts2_on = TS2.is_pressed()
#         time.sleep(0.07)
#         is_ts1_on = TS1.is_pressed()
#         time.sleep(0.05)

        
        
#         if (US.get_value() != None and 5.0 < US.get_value() < 20.0):
#             is_us_on = True
#         else:
#             is_us_on = False
            
        
#         if (not is_ts1_on and not is_ts2_on and is_us_on):
#             # Note 1 plays
#             NOTE1.play()
#             NOTE1.wait_done()
        
#         if (not is_ts1_on and is_ts2_on and not is_us_on):
#             # Note 1 plays
#             # NOTE1.play()
#             # NOTE1.wait_done()
            
#             print("Emergency Stop")
#             is_drum_on = False
#             isEmergency = not isEmergency
            

#         elif (not is_ts1_on and is_ts2_on and is_us_on):
#             # Note 2 plays
#             NOTE2.play()
#             NOTE2.wait_done()   

#         elif (is_ts1_on and not is_ts2_on and not is_us_on):
#             # Note 3 plays
#             print("Note 3")
#             NOTE3.play()
#             NOTE3.wait_done()  
    
#         elif (is_ts1_on and not is_ts2_on and is_us_on):
#             # Note 4 plays
#             print("Note 4")
#             NOTE4.play()
#             NOTE4.wait_done()    
    
#         #elif (ts1_on and ts2_on and not us_on):
#             # Emergency Stop
#             # print("Emergency Stop")
#             # isEmergency = not isEmergency

#         elif (is_ts1_on and is_ts2_on and is_us_on):
#             # Drum toggle
#             print("Drum Toggle")
#             is_drum_on = True
#             print("isDrum on?: ", is_drum_on)
            
#         playDrum()
            
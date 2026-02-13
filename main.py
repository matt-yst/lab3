# import collect_color_sensor_data
# import collect_us_sensor_data
# import touch_sensor
from utils import sound
from utils.brick import TouchSensor, EV3UltrasonicSensor, wait_ready_sensors, reset_brick

# -------------------- CONSTANTS --------------------
US_LOWER_BOUND = 3
US_UPPER_BOUND = 15

NOTE1 = sound.Sound(duration=0.2, pitch="C6", volume=100)
NOTE2 = sound.Sound(duration=0.2, pitch="A6", volume=100)
NOTE3 = sound.Sound(duration=0.2, pitch="E6", volume=100)
NOTE4 = sound.Sound(duration=0.2, pitch="G6", volume=100)
flip_counter = 0

TS1 = TouchSensor(1)
TS2 = TouchSensor(2)

US = EV3UltrasonicSensor(4)

NOTES = [NOTE1, NOTE2, NOTE3, NOTE4]


## -------------------- FUNCTIONS --------------------

def us_in_range(data):
    data = 4
    if data < US_UPPER_BOUND and data > US_LOWER_BOUND:
        return True
    else:
        return False
    
# Reads all sensor input data, output string
def read():
    us_data = US.get_value()

    if us_data==None:
        global flip_counter
        print("US sensor reading failed. Defaulting to flip between in and out of range every 20 loops.")
        if flip_counter % 20 == 0:
            if us_data == 4:
                us_data = 16
            else:
                us_data = 4
        flip_counter += 1

    # if us_in_range(us_data) and not TS1.is_pressed() and TS2.is_pressed():
    #     output = "ES"
    # elif not us_in_range(us_data) and not TS1.is_pressed() and TS2.is_pressed():
    #     output = "DT"
    # elif us_in_range(us_data) and not TS1.is_pressed() and TS2.is_pressed():
    #     output = "N1"
    # elif not us_in_range(us_data) and TS1.is_pressed() and not TS2.is_pressed():
    #     output = "N2"
    # elif us_in_range(us_data) and TS1.is_pressed() and not TS2.is_pressed():
    #     output = "N3"
    # elif not us_in_range(us_data) and TS1.is_pressed() and TS2.is_pressed():
    #     output = "N4"
    # else:
    #     output = "None"

    if us_in_range(us_data): # XX1
        #US->TS1->TS2
        if TS1.is_pressed(): # 1X1
            if TS2.is_pressed(): #111
                return ""
            else: #101
                return "N3"
        elif not TS1.is_pressed(): #0X1
            if TS2.is_pressed(): #011
                return "N1"
            else: #001
                return "ES"
        #US->TS2->TS1
        elif TS2.is_pressed(): #X11
            if TS1.is_pressed(): #111
                return ""
            else: #011
                return "N1"
        elif not TS2.is_pressed(): #X01
            if TS1.is_pressed(): #101
                return "N3"
            else: #001
                return "ES"
    elif TS1.is_pressed(): #1XX
        #TS1->TS2->US
        if TS2.is_pressed(): #11X
            if us_in_range(us_data): #111
                return ""
            else: #110
                return "N4"
        elif not TS2.is_pressed(): #10X
            if us_in_range(us_data): #101
                return "N3"
            else: #100
                return "N2"
        #TS1->US->TS2
        elif us_in_range(us_data): #1X1
            if TS2.is_pressed(): #111
                return ""
            else: #101
                return "N3"
    elif TS2.is_pressed(): #X1X
        # TS2->TS1->US
        if TS1.is_pressed(): #11X
            if us_in_range(us_data): #111
                return ""
            else: #110
                return "N4"
        elif not TS1.is_pressed(): #01X
            if us_in_range(us_data): #011
                return "N1"
            else: #010
                return "DT"
        #TS2->US->TS1
        elif us_in_range(us_data): #X11
            if TS1.is_pressed(): #111
                return ""
            else: #011
                return "N1"
        elif not us_in_range(us_data): #X10
            if TS1.is_pressed(): #110
                return "N4"
            else: #010
                return "DT"
    else:
        return ""

# -------------------- MAIN LOOP --------------------

def main() :
    i = 1
    while True:
        out = read()
        if (out == "ES"):
                for note in NOTES:
                    note.stop()
                # if drumPlaying = true:
                #     stopDrum()
                # sleep(5)
                print("emergency stop omg")
                # emergency stop

        elif(out == "ES"):
                print("drum toggle omg")
                # drum toggle
        elif(out == "N1"):
                NOTE1.play()
                NOTE1.wait_done()
                # note 1, C6
        elif(out == "N2"):
                NOTE2.play()
                NOTE2.wait_done()
                # note 2, A6
        elif(out == "N2"):
                NOTE3.play()
                NOTE3.wait_done()
                # note 3, E6
        elif(out == "N4"):
                NOTE4.play()
                NOTE4.wait_done()
                # note 4, G6
        else:
                # don't cares :P
                pass

if __name__ == "__main__":
    main()
    

import collect_color_sensor_data
import collect_us_sensor_data
import touch_sensor
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors

NOTE1 = sound.Sound(duration=1, pitch="C6", volume=100)
NOTE2 = sound.Sound(duration=1, pitch="A6", volume=100)
NOTE3 = sound.Sound(duration=1, pitch="E6", volume=100)
NOTE4 = sound.Sound(duration=1, pitch="G6", volume=100)

NOTES = [NOTE1, NOTE2, NOTE3, NOTE4]

def read():
    output = None
    # Reads all sensor input data, output string
    return output

if __name__ == "__main__":
    while True:
        out = read()
        match out:
            case "ES":
                for note in NOTES:
                    note.stop()
                # if drumPlaying = true:
                #     stopDrum()
                # sleep(5)
                print("emergency stop omg")
                # emergency stop

            case "DT":
                print("drum toggle omg")
                # drum toggle
            case "N1":
                NOTE1.play()
                NOTE1.wait_done()
                # note 1, C6
            case "N2":
                NOTE2.play()
                NOTE2.wait_done()
                # note 2, A6
            case "N3":
                NOTE3.play()
                NOTE3.wait_done()
                # note 3, E6
            case "N4":
                NOTE4.play()
                NOTE4.wait_done()
                # note 4, G6
            case _:
                print("DONNNNNN'T CAREEEEE, WHERE'S RICK?!?")
                # don't cares :P
                pass

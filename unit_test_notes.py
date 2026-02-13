from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors

TS1 = TouchSensor(1)
TS2 = TouchSensor(2)

N1= sound.Sound(duration=0.1, pitch="A5", volume=50)
N2 = sound.Sound(duration=0.1, pitch="B4", volume=50)

wait_ready_sensors()

while (True):
    if (TS1.is_pressed()):
        print("1 Registered")
        N1.play()
        N1.wait_done()
        
    if (TS2.is_pressed()):
        print("2 Registered")
        N2.play()
        N2.wait_done()

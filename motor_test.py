from utils.brick import Motor, wait_ready_sensors
import time

motor = Motor("B")
wait_ready_sensors(True)

# motor.reset_encoder();

motor.set_limits(power=70)

print(motor.get_status())

while True:
    motor.set_position(0)
    print(motor.get_position())
    time.sleep(0.25)
    motor.set_position(-90)
    print(motor.get_position())
    time.sleep(0.25)
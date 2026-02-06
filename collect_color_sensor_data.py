#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor, reset_brick
from time import sleep

COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(3)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        # Appending new data to file, since each execution collects data once only
        output_file = open(COLOR_SENSOR_DATA_FILE, "a")
        print("Press to read")
        while not TOUCH_SENSOR.is_pressed():
            pass
        print("Touch sensor pressed")
        sleep(1)
        print("Starting to collect color sample")
        while True: #continuous reading
            if not TOUCH_SENSOR.is_pressed():
                color_data = COLOR_SENSOR.get_value()
                print(color_data)
                if color_data is not None:
                    # [:3] to exclude the light intensity from max checks, to determine color group
                    # First value is red
                    if max(color_data[:3]) == color_data[0]:
                        print("Color contains mostly red")
                    # Second value is green
                    elif max(color_data[:3]) == color_data[1]:
                        print("Color contains mostly green")
                    # Third value is blue
                    else:
                        print("Color contains mostly blue")
                    output_file.write(f"{color_data}\n")
                else:
                    print("failed to read")
                sleep(0.01)
    except BaseException:
        print("baseexception reached")
        pass
    finally:
        #print("Done collecting Color samples")
        output_file.close()
        reset_brick()
        exit()


if __name__ == "__main__":
    collect_color_sensor_data()

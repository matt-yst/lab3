#!/usr/bin/env python3
from utils.brick import wait_ready_sensors, EV3UltrasonicSensor

ultra = EV3UltrasonicSensor(2)

wait_ready_sensors()

ultra.get_raw_value() # => starts with centimeter reading

ultra.detects_other_us_sensor() # switch mode, False or True
ultra.get_cm() # switch mode, centimeter distance
ultra.get_inches() # switch mode, inches distance
ultra.get_inches() # no mode switch, it's unnecessary

while (True):
    print (ultra.get_value()) # => starts with centimeter reading
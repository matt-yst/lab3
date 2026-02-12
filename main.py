import collect_color_sensor_data
import collect_us_sensor_data
import touch_sensor

def read():
    # Reads all sensor input data, output string
    return output

motor = Motor("A")
motor.set_power(100) # 100% power
motor.set_dps(90) # 90 deg/sec

if __name__ == "__main__":
    while True:
        out = read()
        match out:
            case "ES":
                #emergency stop
                
            case "DT":
                #drum toggle
                motor.set_position(180) # Rotate 180 degrees
                motor.set_position(0)   # Rotate back to 0 degrees
            case "N1":
                #note 1
            case "N2":
                #note 2
            case "N3":
                #note 3 
            case "N4":
                #note 4
            case _:
                pass
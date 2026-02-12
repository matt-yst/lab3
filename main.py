import collect_color_sensor_data
import collect_us_sensor_data
import touch_sensor

def read():
    # Reads all sensor input data, output string
    return output

if __name__ == "__main__":
    while True:
        out = read()
        match out:
            case "ES":
                #emergency stop
                
            case "DT":
                #drum toggle
                #test push 
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
import collect_color_sensor_data
import collect_us_sensor_data
import touch_sensor

US_LOWER_BOUND = 3
US_UPPER_BOUND = 3

def us_in_range(data):
    if data < US_UPPER_BOUND and data > US_LOWER_BOUND:
        return True
    else:
        return False
    
def read():
    # Reads all sensor input data, output string
    us_data = US_SENSOR.get_value()

    if us_in_range(us_data) and not touch1.is_pressed() and touch2.is_pressed():
        output = "ES"
    elif not us_in_range(us_data) and not touch1.is_pressed() and touch2.is_pressed():
        output = "DT"
    elif us_in_range(us_data) and not touch1.is_pressed() and touch2.is_pressed():
        output = "N1"
    elif not us_in_range(us_data) and touch1.is_pressed() and not touch2.is pressed():
        output = "N2"
    elif us_in_range(us_data) and touch1.is_pressed() and not touch2.is_pressed():
        output = "N3"  
    elif not us_in_range(us_data) and touch1.is_pressed() and touch2.is_pressed():
        output = "N4"
    else:
        output = "None"
    return output

if __name__ == "__main__":
    while True:
        out = read()
        match out:
            case "ES":
                #emergency stop
                
            case "DT":
                #drum toggle
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
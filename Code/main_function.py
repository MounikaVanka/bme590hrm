from Input_csv_file import *
from calc_avg_hr import *
from calc_inst_hr import *
from Checking_threshold import *
from Write_output_file import *


def main():

    """main function will print the following to file
    1. The avg heart rate
    2. The instantaneous heart rate
    3. Indication and time of bradycardia or tachycardia
    """
    
    # Gets the input file named ecg_data.csv
    output = read_in()
    time = output[0]
    voltage = output[1]
    print(time)

    # Calculates the Instantaneous Heart Rate
    bpm_inst_hr = calc_inst_hr(time, voltage)

    # Calculates the Average Heart Rate
    bpm_avg_hr = calc_avg_hr(time, voltage, window=input("Enter the window time in seconds"))

    a = input("Enter the Bradycardia threshold")
    b = input("Enter the Tachycardia threshold")

    a = int(a)
    b = int(b)
    
    # Checks the Threshold
    threshold = checking_threshold(a, b, bpm_avg_hr)

    # Writes to output file
    write_to_file(bpm_inst_hr, bpm_avg_hr[0], threshold)


if __name__ == '__main__':
    main()

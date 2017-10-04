from Input_csv_file import *
from calc_avg_hr import *
from calc_inst_hr import *
from Checking_threshold import *
from Write_output_file import *
import numpy as np


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

    # Calculates the Instantaneous Heart Rate
    bpm_inst_hr = calc_inst_hr(time, voltage)

    # Calculates the Average Heart Rate
    window = input("Enter the window time in minutes: ")
    window = int(window) * 60  # convert to seconds for calc
    bpm_avg_hr = calc_avg_hr(time, voltage, window)

    a = input("Enter the Bradycardia threshold: ")
    b = input("Enter the Tachycardia threshold: ")

    a = int(a)
    b = int(b)

    # loop here

    # Checks the Threshold

    threshold1 = np.array([])
    for row in bpm_avg_hr:
        threshold = checking_threshold(a, b, row)
        threshold1 = np.append(threshold1, threshold)

    # Writes to output file
    write_to_file(bpm_inst_hr, bpm_avg_hr[0], threshold1)
    print('Instantaneous Heart Rate is:', bpm_inst_hr, '\n',
          'Average Heart Rate is:', bpm_avg_hr[0], '\n',
          'The condition for each window is', threshold1)


if __name__ == '__main__':
    main()

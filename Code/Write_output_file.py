import sys
# from cal_inst_hr import *
#from Code_1_2 import *


global output


def write_to_file(a, b, c):
    """ Writes the output to a separate file

    :param a: The instantaneous heart rate is displayed
    :param b: The avg_heart_rate is displayed
    :param c: The output string is displayed
    """
    prev = sys.stdout
    sys.stdout = open("test.txt", "w")
    instantaneous_heart_rate = a
    avg_heart_rate = b
    Threshold = c
    print(instantaneous_heart_rate, '\n', avg_heart_rate, '\n', Threshold)
    sys.stdout.close()
    sys.stdout = prev

#print(output)
#write_to_file(60, 72, output)
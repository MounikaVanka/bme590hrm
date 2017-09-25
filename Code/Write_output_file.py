import sys


def write_to_file(a, b, c):
    """
    Writes the output to a separate file
    :param a: instantaneous heart rate
    :param b: avg_heart_rate
    :param c: output string
    """
    prev = sys.stdout
    sys.stdout = open("test.txt", "w")
    instantaneous_heart_rate = a
    avg_heart_rate = b
    threshold = c
    print('Instantaneous Heart Rate is:',instantaneous_heart_rate,'\n','Average Heart Rate is:',avg_heart_rate, '\n','The ouput heart condition is"',threshold)
    sys.stdout.close()
    sys.stdout = prev


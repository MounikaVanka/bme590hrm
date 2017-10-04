
def write_to_file(a, b, c):
    import sys
    """
    Writes the output to a separate file
    :param a: instantaneous heart rate
    :param b: avg_heart_rate
    :param c: output string
    """
    prev = sys.stdout
    sys.stdout = open("output.txt", "w")
    instantaneous_heart_rate = a
    avg_heart_rate = b
    threshold = c
    print('Instantaneous Heart Rate is:', instantaneous_heart_rate)
    print('Average Heart Rate is:', avg_heart_rate)
    print('The condition for each window is', threshold)
    sys.stdout.close()
    sys.stdout = prev


def write_to_file(inst_hr, avg_hr, output):
    """Writes the output to a separate file

    :param inst_hr: int instantaneous heart rate
    :param avg_hr: int avg_heart_rate
    :param output: string output
    """
    import sys
    prev = sys.stdout
    sys.stdout = open("output.txt", "w")
    print('Instantaneous Heart Rate is:', inst_hr)
    print('Average Heart Rate is:', avg_hr)
    print('The condition for each window is', output)
    sys.stdout.close()
    sys.stdout = prev

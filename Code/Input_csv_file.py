
def read_in(b):
    import csv
    import numpy
    """
     Opens the ecg CSV file
     :param readCSV: pointer to the file
     :param times: the time from the signal
     :param Voltage: the voltage from the signal
     """
    # with open('ecg_data.csv') as csvfile:
    #     read_csv = csv.reader(csvfile, delimiter=',')
    #     header_line = next(read_csv)
    #
    #     time = numpy.array([])
    #     voltage = numpy.array([])
    #
    #
    #     for row in read_csv:
    #         time1 = row[0]
    #         voltage1 = row[1]
    #
    #         # time = numpy.append(time, time1)
    #         # voltage = numpy.append(voltage, voltage1)
    a = b
    dat = numpy.genfromtxt(a, delimiter=',', skip_header=1, )
    time = dat[:, 0]
    voltage = dat[:, 1]
    # for element in time:
    #     #parts=element.split(',')
    # time = tim.astype('Float64')
    # time.astype()
    #
    # #for element in voltage:
    #     #parts1=element.split(',')
    # voltage = voltage.astype('Float64')
    return time, voltage

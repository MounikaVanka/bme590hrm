
def read_in():
    import csv
    import numpy

    # with open('ecg_data.csv') as csvfile:
    #     """
    #     Opens the ecg CSV file
    #     :param readCSV: pointer to the file
    #     :param times: the time from the signal
    #     :param Voltage: the voltage from the signal
    #     """
    #
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

    dat = numpy.genfromtxt('ecg_data1.csv', delimiter=',', skip_header= 2, )

    time = dat[:,0]
    voltage = dat[:,1]
    #for element in time:
    #     #parts=element.split(',')
    # time = tim.astype('Float64')
    # time.astype()
    #
    # #for element in voltage:
    #     #parts1=element.split(',')
    # voltage = voltage.astyoe('Float64')
    
    return time, voltage
    




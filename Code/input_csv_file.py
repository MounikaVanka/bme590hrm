def read_in(filename):
    """Opens the ecg CSV file

     :param filename: file string
     :return: the time from the signal
     :return: the voltage from the signal
     """
    import csv
    import numpy
    import warnings

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
    dat = numpy.genfromtxt(filename, delimiter=',', skip_header=1)
    length = len(dat)
    ekg_max = 10  # mV

    # check data for bad values, reversed indexing for accurate removal
    for count, reading in enumerate(reversed(dat)):
        if numpy.isnan(reading[0]) or numpy.isnan(reading[1]):
            dat = numpy.delete(dat, length-count-1, 0)
    if max(abs(dat[:, 1])) >= ekg_max:
        print('Warning: data in {0} out of expected range'.format(filename))

    # dat = filtered;

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


def read_in():
    import csv
    import numpy

    with open('ecg_data.csv') as csvfile:
        """
        Opens the ecg CSV file
        :param readCSV: pointer to the file
        :param times: the time from the signal
        :param Voltage: the voltage from the signal
        """

        read_csv = csv.reader(csvfile, delimiter=',')
        header_line = next(read_csv)
        time = numpy.array([])
        voltage = numpy.array([])

        for row in read_csv:
            time1 = row[0]
            voltage1 = row[1]

            time=numpy.append(time,time1)
            voltage=numpy.append(voltage,voltage1)



    #for element in time:
        #parts=element.split(',')
    Time=numpy.asarray(time,'Float64')
    
    #for element in voltage:
        #parts1=element.split(',')
    Voltage=numpy.asarray(voltage,'Float64')
    print(Time)
    return Time,Voltage

read_in()



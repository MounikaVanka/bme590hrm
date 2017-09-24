
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
        time = []
        voltage = []

        for row in read_csv:
            time1 = row[0]
            voltage1 = row[1]

            time.append(time1)
            voltage.append(voltage1)



    for element in time:
        parts=element.split(',')
    Time=numpy.asarray(parts,'Float64')
    
    for element in voltage:
        parts1=element.split(',')
    Voltage=numpy.asarray(parts1,'Float64')
    return Time,Voltage
'''
read_in()

'''

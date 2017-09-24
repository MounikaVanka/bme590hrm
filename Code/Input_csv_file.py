
def read_in():
    import csv

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

    return time, voltage

'''
read_in()
for element in time:
    parts=element.split(',')
    print(parts)


Time=numpy.asarray(parts,'Float64')
print(Time)
for element in voltage:
    parts1=element.split(',')
    print(parts1)
Voltage=numpy.asarray(parts1,'Float64')
print(Voltage)
print(numpy.ndarray.size(Voltage))
abc=numpy.asarray(parts)
print(abc)
'''

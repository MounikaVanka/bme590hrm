import csv

with open('ecg_data.csv') as csvfile:
    """checking for available ecg file

    :param input file
    :param readCSV: variable for storing the file pointer
    """

    readCSV = csv.reader(csvfile,delimiter=',')
    header_line = next(readCSV)

    times = []
    Voltages = []

    for row in readCSV:
        time = row[0]
        Voltage = row[1]

        times.append(time)
        Voltages.append(Voltage)


print(times)
print(Voltages)
print(header_line)



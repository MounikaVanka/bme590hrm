import csv

with open('ecg_data.csv') as csvfile:

    """Opens the ecg CSV file
    
    
    :param readCSV: pointer to the file
    :param times: the time from the signal
    :param Voltage: the voltage from the signal

    """

    readCSV = csv.reader(csvfile, delimiter=',')
    header_line = next(readCSV)

    time = []
    Voltage = []




    for row in readCSV:
        time1 = row[0]
        Voltage1 = row[1]


        times.append(time1)
        Voltages.append(Voltage1)


print(time)
print(Voltage)


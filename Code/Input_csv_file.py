
import numpy

def read_in():
    import csv
    

    with open('ecg_data.csv') as csvfile:

        """Opens the ecg CSV file
        
        
        :param readCSV: pointer to the file
        :param times: the time from the signal
        :param Voltage: the voltage from the signal
    
        """

        readCSV = csv.reader(csvfile, delimiter=',')
        header_line = next(readCSV)
        global time
        global voltage
        time = []
        voltage = []




        for row in readCSV:
            time1 = row[0]
            voltage1 = row[1]


            time.append(time1)
            voltage.append(voltage1)

    return (time,voltage)

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

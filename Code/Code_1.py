import csv

with open('ecg_data.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    header_line=next(readCSV)

    times=[]
    Voltages=[]



    for row in readCSV:
        time=row[0]
        Voltage=row[1]


        times.append(time)
        Voltages.append(Voltage)


print(times)
print(Voltages)
print(header_line)

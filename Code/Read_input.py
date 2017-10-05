def read_in():

    import numpy as np
    a = input('Enter the file name')
    file = numpy.genfromtxt('ecg_data.csv',
                            dtype=['fltvar', 'fltvar'],
                            ... names=['Time', 'Voltage'],
                            delimiter=" , ")

read_in()

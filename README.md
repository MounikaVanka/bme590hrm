# bme590hrm 
Calculates the instantaneous heart rate, average heart rate and also indicates conditions like Bradycardia and Tachycardia. 


The Software License for the file is:
=========
LICENSE.md ( MIT License)

The Travis Badge is:
=========
[![Build Status](https://travis-ci.org/MounikaVanka/bme590hrm.svg?branch=master)](https://travis-ci.org/MounikaVanka/bme590hrm)

Starting the Program
=========
The program may be started by running main_function.py in the Code folder. 

Requirements:
=========
Python 3.6

The inputs required from the user are:
1. ECG data file in .csv format in a file named 'ecg_data.csv' in the Code folder with the time and Voltage in numerical format
2. The HR threshold in bpm for bradycardia and tachycardia
3. The sample window in minutes for which the average heart rate is to be estimated

Output
=========
The output is printed to output.txt with the instantaneous HR on the first line, average HR on the second line, and ECG condition on the third line.

The output instantaneous HR will be reported from the first RR interval in the input data.

The output average HR will be reported from the first user specified window in the input data. If the window is longer than the amount of data in ecg_data.csv, the output will be the average over all the available data.

The ECG condition will be either Bradycardia, Tachycardia, or Normal Heart Rate. The condition will be indicated for every average heart rate window.


Unit Testing
=========
Unit testing is performed using py.test by running test_hrm.py.

Team Members:
======
+ Caleb Willis
+ Tim Hoer
+ Mounika Vanka


Credits
=======
* Mark Palmeri
* Suyash Kumar
* Arjun Desai



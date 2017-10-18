# bme590hrm 
Calculates the instantaneous heart rate, average heart rate and also indicates conditions like Bradycardia and Tachycardia. 


The Software License for the file is:
=========
LICENSE.md ( MIT License)

The Travis Badge is:
=========
[![Build Status](https://travis-ci.org/MounikaVanka/bme590hrm.svg?branch=master)](https://travis-ci.org/MounikaVanka/bme590hrm)

Read the Docs Badge:
=========
<a href='http://bmehrmproject.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/bmehrmproject/badge/?version=latest' alt='Documentation Status' />
</a>   


Starting the Program
=========
The program may be started by running classy_hrm.py in the Code folder or by importing the classy_hrm() function.

Requirements:
=========
Python 3.6

Input parameters:
1. Filename for ECG data .csv file with time and voltage in numerical format
2. Sample window in seconds for which the average heart rate is to be estimated
3. HR threshold in bpm for bradycardia
4. HR threshold in bpm for and tachycardia

Output
=========
The output is printed to (filename)_out.txt with the instantaneous HR on the first line, average HR on the second line, and ECG condition on the third line.

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



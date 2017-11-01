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
1. file = filename for ECG data .csv file with time and voltage in numerical format
2. window = Sample window in seconds for which the average heart rate is to be estimated
3. brady_max = HR threshold in bpm for bradycardia
4. tachy_min = HR threshold in bpm for and tachycardia

Output
=========
The output is printed to (filename)_out.txt with the instantaneous HR on the first line, average HR on the second line, and ECG condition on the third line, with the latter two data sets calculated over the specified window.


The output average heart rate data will be output in vectors equal to the length of the input time and voltage data vectors. If the specified window is longer than the amount of data in the input file, the output will be the average over all the available data.

The ECG conditions bradycardia and tachycardia are each indicated using a boolean vector.


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



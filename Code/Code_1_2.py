import numpy as np
# from cal_inst_hr import *


<<<<<<< HEAD
def Checking_Threshold(a,b,avg_heart_rate):
=======
def Checking_Threshold(a=60, b=100):
>>>>>>> cc4cd40e29e0a9aa7d97f52662dcd159df7aafd0
    """checking for Tachycardia or Bradycardia



    :param Threshold: int variable, bmp
    :param avg_heart_rate: int, bmp
    :return: The condition string
    """
<<<<<<< HEAD
    
    global output
    
    # Checks if the the heart rate is lesser or greater than the threshold
    if (avg_heart_rate <= a):
        output="Bradycardia"
        print(output)
        return output


    elif(avg_heart_rate >= b):
=======

# Just a place holder, will import the value from cal_inst_hr

    avg_heart_rate = 72    
    global output
    
# Checks if the the heart rate is lesser or greater than the threshold
    if(avg_heart_rate < a): 
        output="Bradycardia"
        print(output)
        return output
    elif(avg_heart_rate > b):
>>>>>>> cc4cd40e29e0a9aa7d97f52662dcd159df7aafd0
        output="Tachycardia"
        print(output)
        return output 
    elif(avg_heart_rate > a and avg_heart_rate < b):
        output="Normal Heart Rate"
        print (output)
        return output

a = int(input("Enter the Bradycardia Threshold"))
b = int(input("Enter the Tachycardia Threshold"))
Checking_Threshold(a, b)

# if _name_ == '_main_':

<<<<<<< HEAD

#a=int(input("Enter the Bradycardia Threshold"))
#b=int(input("Enter the Tachycardia Threshold"))
#avg_heart_rate=72
#Checking_Threshold(a,b,avg_heart_rate)


#if _name_ == '_main_':
=======
>>>>>>> cc4cd40e29e0a9aa7d97f52662dcd159df7aafd0

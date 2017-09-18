import numpy as np
# from cal_inst_hr import *


def Checking_Threshold(a=60,b=100):
    """checking for Tachycardia or Bradycardia



    :param Threshold: int variable, bmp
    :param avg_heart_rate: int, bmp
    :return: The condition string
    """

    #Just a place holder, will import the value from cal_inst_hr

    avg_heart_rate=72
    
    global output
    
    # Checks if the the heart rate is lesser or greater than the threshold
    if (avg_heart_rate < a): 
        output="Bradycardia"
        print(output)
        return output


    elif(avg_heart_rate > b):
        output="Tachycardia"
        print(output)
        return output
    
    
    elif(avg_heart_rate > a and avg_heart_rate < b):
        output="Normal Heart Rate"
        print (output)
        return output




a=int(input("Enter the Bradycardia Threshold"))
b=int(input("Enter the Tachycardia Threshold"))
Checking_Threshold(a,b)


#if _name_ == '_main_':

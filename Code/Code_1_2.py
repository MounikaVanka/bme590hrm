import numpy as np
# from cal_inst_hr import *


def Checking_Threshold(a,b,avg_heart_rate):
    """checking for Tachycardia or Bradycardia



    :param Threshold: int variable, bmp
    :param avg_heart_rate: int, bmp
    :return: The condition string
    """
    
    global output
    
    # Checks if the the heart rate is lesser or greater than the threshold
    if (avg_heart_rate <= a):
        output="Bradycardia"
        print(output)
        return output


    elif(avg_heart_rate >= b):
        output="Tachycardia"
        print(output)
        return output
    
    
    elif(avg_heart_rate > a and avg_heart_rate < b):
        output="Normal Heart Rate"
        print (output)
        return output




#a=int(input("Enter the Bradycardia Threshold"))
#b=int(input("Enter the Tachycardia Threshold"))
#avg_heart_rate=72
#Checking_Threshold(a,b,avg_heart_rate)


#if _name_ == '_main_':

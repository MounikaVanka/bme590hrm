from Input_csv_file import *
from calc_avg_hr import *
from calc_inst_hr import *
from Checking_threshold import *


def main():

    """main funcion return the following output
    1. The avg heart rate
    2. The instantaneous heart rate
    3. The trace with Tachcardia
    """
    
    #Gets the input file named ecg_data.csv
    [time,voltage]=read_in()
    

    #Calculates the Instantaneous Heart Rate
    bpm_inst_hr=calc_inst_hr(time,voltage)
    
    
    #Calculates the Avegare Heart Rate
    bpm_avg_hr=calc_avg_hr(time,voltage,window=input("Enter the window time in seconds"))


    a=input("Enter the Bradycarida range")
    b=input("Enter the Tachycarida range")
    
    #Checks the Threshold
    threshold=checking_threshold(a,b,bmp_avg_hr)

    # Writes to ouput file
    write_to_file(bmp_inst_hr,bmp_avg_hr,threshold)



main()

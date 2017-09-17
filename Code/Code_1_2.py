def Checking_Threshold(a=60,b=100):
    avg_heart_rate=72
    if (avg_heart_rate < a): 
        output=print("Bradycardia")
        return output
    elif(avg_heart_rate > b):
        output=print("Tachycardia")
        return output
    elif(avg_heart_rate > a and avg_heart_rate < b):
        output=print("Normal Heart Rate")
        return output

a=int(input("Enter the Bradycardia Threshold"))
b=int(input("Enter the Tachycardia Threshold"))
Checking_Threshold(a,b)


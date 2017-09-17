import sys

def write_to_file(a,b,c):
    sys.stdout=open("test.txt","w") 
    instantaneous_heart_rate=a
    avg_heart_rate=b
    Threshold=c
    print(instantaneous_heart_rate,' ',avg_heart_rate,' ',Threshold)
    sys.stdout.close()
    


write_to_file(60,72,input("enter the output"))

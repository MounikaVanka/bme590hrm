
def checking_threshold(a, b, avg_heart_rate):
    """checking for Tachycardia or Bradycardia
    :param a: int variable, lower bound bpm
    :param b: int variable, upper bound bpm
    :param avg_heart_rate: int, bmp
    :return: The condition string
    """

    # Checks if the the heart rate is lesser or greater than the threshold
    if avg_heart_rate <= a:
        output = "Bradycardia"
        print(output)
        return output

    elif avg_heart_rate >= b:
        output = "Tachycardia"
        print(output)
        return output

    else:
        output = "Normal Heart Rate"
        print (output)
        return output

# a=int(input("Enter the Bradycardia Threshold"))
# b=int(input("Enter the Tachycardia Threshold"))
# avg_heart_rate=72
# Checking_Threshold(a,b,avg_heart_rate)



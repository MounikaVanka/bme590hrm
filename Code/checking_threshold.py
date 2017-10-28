def checking_threshold(a, b, avg_heart_rate):
    """checking for Tachycardia or Bradycardia

    :param a: int, lower bound bpm
    :param b: int, upper bound bpm
    :param avg_heart_rate: array, bpm
    :return: The condition string
    """

    # Checks if the the heart rate is lesser or greater than the threshold
    if avg_heart_rate <= a:
        brady_state = True
        tachy_state = False
        return brady_state, tachy_state

    elif avg_heart_rate >= b:
        brady_state = False
        tachy_state = True
        return brady_state, tachy_state

    else:
        brady_state = False
        tachy_state = False
        return brady_state, tachy_state

# a=int(input("Enter the Bradycardia Threshold"))
# b=int(input("Enter the Tachycardia Threshold"))
# avg_heart_rate=72
# Checking_Threshold(a,b,avg_heart_rate)

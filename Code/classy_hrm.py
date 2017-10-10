def classy_hrm(file='ecg_data.csv', window=20, brady_max=40, tachy_min=100):
    """Main function to be used with class-based approach

    :param file: str, name of input csv file
    :param window: int, window size in sec to divide signal into for diagnosis
    :param brady_max: int, upper threshold for bradycardia
    :param tachy_min: int, lower threshold for tachycardia
    :return: none
    """
    from ecg import ECG

    data = ECG(file, window, brady_max, tachy_min)
    data.write_file()
    data.print_results()


if __name__ == '__main__':
    # if running standalone, just use default parameters
    classy_hrm()
def classy_hrm(file='ecg_data1.csv', window=20, brady_max=40, tachy_min=100):
    """Creates ECG class given input parameters and performs analysis
        on data in file to find heart condition, as well as instantaneous
        and average heart rate in BPM. These results are printed to
        <file>_out.txt and are printed to the console.

    :param file: str, name of input csv file
    :param window: int,window size in seconds to divide signal for diagnosis
    :param brady_max: int, upper threshold for bradycardia in BPM
    :param tachy_min: int, lower threshold for tachycardia in BPM
    :return: none
    """
    from ecg import ECG

    data = ECG(file=file, window=window, brady_max=brady_max,
               tachy_min=tachy_min)
    data.write_file()
    data.print_results()


if __name__ == '__main__':
    # if running standalone, just use default parameters
    classy_hrm()

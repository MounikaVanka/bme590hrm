def test_initialization():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures ECG class initializes inputs correctly.
    """
    from ecg import ECG
    test = ECG(file='ecg_data1.csv', window=20, brady_max=40, tachy_min=100)
    assert(test.window == 20)
    assert(test.threshold == (40, 100))


def test_class_write():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures ECG class writes output file in correct output.
    """
    from ecg import ECG
    import os
    test = ECG(file='ecg_data1.csv', window=20, brady_max=40, tachy_min=100)
    test.write_file()
    assert(os.path.isfile('ecg_data1_out.txt'))
    os.remove('ecg_data1_out.txt')


def test_read_in():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures input file is read correctly.
    """
    # import script that reads
    import numpy
    from input_csv_file import read_in
    (time, voltage) = read_in('ecg_data.csv')
    # check that lists are created
    assert(isinstance(time, numpy.ndarray) is True)
    assert (isinstance(voltage, numpy.ndarray) is True)


def test_write_to_file():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures output file is formatted correctly.
    """
    # assert output file is 3 lines and lines are as expected
    from write_output_file import write_to_file
    write_to_file('test_output.txt', 60, 75, "False", "False" )
    with open('test_output.txt') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    assert(len(lines) == 4)
    assert (lines[0] == "Instantaneous Heart Rate: 60")
    assert (lines[1] == "Average Heart Rate: 75")
    assert (lines[2] == "Bradycardia Annotations: False")
    assert (lines[3] == "Tachycardia Annotations: False")




def test_checking_threshold():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for proper heart rate classification.
    """
    from checking_threshold import checking_threshold
    assert(checking_threshold(60, 100, 72)[0] == False)
    assert (checking_threshold(60, 100, 55)[0] == True)
    assert (checking_threshold(60, 100, 110)[1] == True)


def test_calc_inst_hr():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for instantaneous HR calculation within 10% of accepted.
    """
    from calc_inst_hr import calc_inst_hr
    import numpy as np
    time = np.loadtxt('time10.txt', delimiter=',')
    voltage = np.loadtxt('voltage10.txt', delimiter=',')
    output = calc_inst_hr(time, voltage)
    assert(len(output) == len(time))
    assert(.9*62 < output[0] < 1.1*62)


def test_calc_avg_hr():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for average HR calculation within 10% of accepted.
    """
    from calc_avg_hr import calc_avg_hr
    import numpy as np
    time = np.loadtxt('time60.txt', delimiter=',')
    voltage = np.loadtxt('voltage60.txt', delimiter=',')
    output = calc_avg_hr(time, voltage, 60)
    assert(len(output) == len(time))
    assert(.9*62 < output[0] < 1.1*62)


def test_all_cases():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tries all test cases.
    """
    import glob
    from ecg import ECG
    path = "../test_data/*.csv"
    for fname in glob.glob(path):
        print('Testing...', fname)
        test = ECG(file=fname, window=20, brady_max=40, tachy_min=100)


def test_web_methods():
    """
    :Author: Tim Hoer
    :Date: November 2, 2017
    :Notes: Tests ECG class methods used for web services.
    """
    from ecg import ECG
    test = ECG(file='ecg_data1.csv', window=20, brady_max=40, tachy_min=100)
    average_out = test.get_average()
    summary_out = test.get_summary()
    assert (len(summary_out) == 4)
    assert(len(average_out) == 5)

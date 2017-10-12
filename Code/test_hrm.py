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


def test_read_in():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures input file is read correctly.
    """
    # import script that reads
    import numpy
    from Input_csv_file import read_in
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
    from Write_output_file import write_to_file
    write_to_file(60, 75, "normal")
    with open('output.txt') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    assert(len(lines) == 3)
    assert (lines[0] == "Instantaneous Heart Rate is: 60")
    assert (lines[1] == "Average Heart Rate is: 75")
    assert (lines[2] == "The condition for each window is normal")


def test_checking_threshold():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for proper heart rate classification.
    """
    from Checking_threshold import checking_threshold
    assert(checking_threshold(60, 100, 72) == "Normal Heart Rate")
    assert (checking_threshold(60, 100, 55) == "Bradycardia")
    assert (checking_threshold(60, 100, 110) == "Tachycardia")


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
    assert(.9*62 < output < 1.1*62)


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
    assert(.9*62 < output[0] < 1.1*62)

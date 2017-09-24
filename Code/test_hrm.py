
def test_read_in():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures input file is read correctly.
    """
    # import script that reads
    from Input_csv_file import read_in
    (time, voltage) = read_in()
    # check imported list is the right length
    assert(len(time) == 3114)


def test_write_to_file():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Ensures output file is formatted correctly.
    """
    # assert output file is 3 lines and lines are as expected
    from Write_output_file import write_to_file
    write_to_file(60, 75, "All good.")
    with open('test.txt') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    assert(len(lines) == 3)
    assert (lines[0] == "60")
    assert (lines[1] == "75")
    assert (lines[2] == "All good.")


def test_checking_threshold():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    "Notes: Tests for proper heart rate classfication.
    """
    from Checking_threshold import checking_threshold
    assert(checking_threshold(60, 100, 72) == "Normal Heart Rate")
    assert (checking_threshold(60, 100, 55) == "Bradycardia")
    assert (checking_threshold(60, 100, 110) == "Tachycardia")


def test_calc_inst_hr():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for proper heart rate classfication.
    """
    from calc_inst_hr import calc_inst_hr
    import numpy as np
    time = np.loadtxt('time.txt', delimiter=',')
    voltage = np.loadtxt('voltage.txt', delimiter=',')
    assert(calc_inst_hr(time, voltage) == 62)


def test_calc_avg_hr():
    """
    :Author: Tim Hoer
    :Date: September 16, 2017
    :Notes: Tests for proper heart rate classfication.
    """
    from calc_avg_hr import calc_avg_hr
    import numpy as np
    time = np.loadtxt('time.txt', delimiter=',')
    voltage = np.loadtxt('voltage.txt', delimiter=',')
    assert(calc_avg_hr(time, voltage) == 62)


'''
    def test_case():
        """
        :Author: Tim Hoer
        :Date: September 16, 2017
        :Notes: Asserts that the output given a known input is as expected.
        """
        # import relevant scripts/functions
        import wrapper.py
        # call relevant function with test case
        wrapper(test_case.txt)
        # assert heart rate is reported accurately in output file for known case
        file = open(“output.txt”,“r”)
        assert(file.readline(1)=="60")
        assert(file.readline(2)=="60")
        assert(file.readline(3)=="N")

    def test_handling():
        """
        @author: Tim Hoer
        @date: September 16, 2017
        @notes: Tests error handling
        """
        # assert program raises exception if input file is not "ecg_data.csv"
        with pytest.raises(ZeroDivisionError):
                wrapper.py('not_ecg_data.csv')
'''

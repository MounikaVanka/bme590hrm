
def test_hrm():
    """
    @author: Tim Hoer
    @date: September 16, 2017
    @notes: Runs all tests of heart rate monitor project
    """


def test_read_in():
    """
    @author: Tim Hoer
    @date: September 16, 2017
    @notes: Ensures input file is read correctly.
    """
    # import script that reads
    from Code_1 import read_in
    (time, voltage) = read_in()
    # check imported list is the right length
    assert(len(time) == 3114)


def test_write_to_file():
    """
    @author: Tim Hoer
    @date: September 16, 2017
    @notes: Ensures output file is formatted correctly.
    """
    # assert output file is 3 lines and lines are as expected
    from Code_1_3 import write_to_file
    write_to_file(60, 75, "All good.")
    with open('test.txt') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    assert(len(lines) == 3)
    assert (lines[0] == "60")
    assert (lines[1] == "75")
    assert (lines[2] == "All good.")


def test_Checking_Threshold():
    """
    @author: Tim Hoer
    @date: September 16, 2017
    @notes: Tests for proper heart rate classfication.
    """
    from Code_1_2 import Checking_Threshold
    assert(Checking_Threshold(60, 100, 72)== "Normal Heart Rate")
    assert (Checking_Threshold(60, 100, 55) == "Bradycardia")
    assert (Checking_Threshold(60, 100, 110) == "Tachycardia")


def test_calc_inst_hr():
    """
    @author: Tim Hoer
    @date: September 16, 2017
    @notes: Tests for proper heart rate classfication.
    """
    """
    from calc_inst_hr import calc_inst_hr
    import numpy as np
    time = np.array([0.0100, 0.0200, 0.0300, 0.0400, 0.0500, 0.0600, 0.0700, 0.0800, 0.0900, 0.100,
                     0.110, 0.120, 0.130, 0.140, 0.150, 0.160, 0.170, 0.180, 0.190, 0.200, 0.210,
                     0.220, 0.230, 0.240, 0.250, 0.260, 0.270, 0.280, 0.290, 0.300, 0.310, 0.320,
                     0.330, 0.340, 0.350, 0.360, 0.370, 0.380, 0.390, 0.400, 0.410, 0.420, 0.430,
                     0.440, 0.450, 0.460, 0.470, 0.480, 0.490, 0.500, 0.510, 0.520, 0.530, 0.540,
                     0.550, 0.560, 0.570, 0.580, 0.590, 0.600, 0.610, 0.620, 0.630, 0.640, 0.650,
                     0.660, 0.670, 0.680, 0.690, 0.700, 0.710, 0.720, 0.730, 0.740, 0.750, 0.760,
                     0.770, 0.780, 0.790, 0.800, 0.810, 0.820, 0.830, 0.840, 0.850, 0.860, 0.870,
                     0.880, 0.890, 0.900, 0.910, 0.920, 0.930, 0.940, 0.950, 0.960, 0.970, 0.980,
                     0.990, 1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11,
                     1.12, 1.13, 1.14, 1.15, 1.16, 1.17, 1.18, 1.19, 1.20, 1.21, 1.22, 1.23, 1.24,
                     1.25, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32, 1.33, 1.34, 1.35, 1.36, 1.37,
                     1.38, 1.39, 1.40, 1.41, 1.42, 1.43, 1.44, 1.45, 1.46, 1.47, 1.48, 1.49, 1.50,
                     1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.57, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63,
                     1.64, 1.65, 1.66, 1.67, 1.68, 1.69, 1.70, 1.71, 1.72, 1.73, 1.74, 1.75, 1.76,
                     1.77, 1.78, 1.79, 1.80, 1.81, 1.82, 1.83, 1.84, 1.85, 1.86, 1.87, 1.88, 1.89,
                     1.90, 1.91, 1.92, 1.93, 1.94, 1.95, 1.96, 1.97, 1.98, 1.99, 2])
    voltage = np.array([1.992, 1.702, 1.411, 1.119, 0.8270, 0.6600, 0.5850, 0.5090, 0.4410, 0.5090,
                        0.5850, 0.6610, 0.6820, 0.6820, 0.6820, 0.6820, 0.6810, 0.7280, 0.8030,
                        0.8730, 0.9320, 0.9800, 1.013, 1.030, 1.030, 1.013, 0.9800, 0.9330, 0.8730,
                        0.8040, 0.7290, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6820, 0.6840, 0.7050, 0.7160, 0.7140, 0.6970, 0.6820, 0.6820,
                        0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6830, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6810, 0.7450, 0.8160, 0.8700, 0.9000, 0.9130, 0.8990, 0.8570,
                        0.7900, 0.7050, 0.6830, 0.6830, 0.6820, 0.6820, 0.6810, 0.6770, 0.8960,
                        1.185, 1.475, 1.764, 2.052, 2.225, 1.929, 1.636, 1.344, 1.052, 0.7580,
                        0.6460, 0.5680, 0.4930, 0.4470, 0.5240, 0.6000, 0.6750, 0.6810, 0.6820,
                        0.6820, 0.6820, 0.6820, 0.7460, 0.8200, 0.8870, 0.9450, 0.9890, 1.019,
                        1.032, 1.028, 1.007, 0.9710, 0.9200, 0.8580, 0.7870, 0.7100, 0.6830,
                        0.6830, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6890,
                        0.7090, 0.7170, 0.7110, 0.6920, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6830, 0.6830, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820,
                        0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6820, 0.6850, 0.7620,
                        0.8300, 0.8790, 0.9040, 0.9120, 0.8910, 0.8440, 0.7710, 0.6880, 0.6820,
                        0.6810, 0.6810, 0.6810, 0.6810, 0.6890, 0.9590, 1.249, 1.539, 1.830,
                        2.122, 2.155, 1.860, 1.568, 1.277, 0.9870, 0.7050, 0.625])
    assert(calc_inst_hr(time,voltage) == 62)
"""

'''
    def test_case():
        """
        @author: Tim Hoer
        @date: September 16, 2017
        @notes: Asserts that the output given a known input is as expected.
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

    # test_input()
test_write_to_file()
test_Checking_Threshold()
    # test_case()
    # test_handling()


if __name__ == '__main__':
    test_hrm()

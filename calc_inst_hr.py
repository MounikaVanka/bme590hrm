import numpy as np
import scipy.signal
import Code_1.py



def calc_inst_hr(time, voltage):
    """ calculate instantaneous HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :return: heart rate in bpm
    """


    # indices = peakutils.indexes(voltage, thres = 0.95*np.max(voltage), min_dist = 1000)
    indices = scipy.signal.find_peaks_cwt(voltage, np.arange(1, 200))

    # TODO: make min dist (or np.arange) relate to sampling rate. right now just placeholder parameters

    r_peaks = time(indices)
    # just take first two peaks to get instantaneous. not that accurate obviously, could give more control
    beat_diff = r_peaks[1] - r_peaks[0]

    bpm = beat_diff / 60


    return bpm


# if __name__ == '__main__':


import numpy as np
import scipy.signal


def calc_inst_hr(time, voltage):
    """ calculate instantaneous HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :return: heart rate in bpm
    """

    # indices = peakutils.indexes(voltage, thres = 0.95*np.max(voltage), min_dist = 1000)

    # get sampling rate
    fs = 1 / (time[1] - time[0])

    # choose HRs to search for
    rates = np.arange(40, 200, 20) / 60
    # find peaks. factor of 10 set kind of arbitrarily
    peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates / 50)

    # just take first two peaks to get instantaneous. not that accurate obviously, could give more control
    beat_diff = time[peaks[1]] - time[peaks[0]] # seconds per beat
    bpm = 1 / beat_diff * 60 # beats per minute

    return bpm


# if __name__ == '__main__':


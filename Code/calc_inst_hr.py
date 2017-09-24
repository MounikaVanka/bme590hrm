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
    # rates = np.arange(40, 200, 20) / 60

    rates = np.array([voltage.size()/50])  # search width
    # find peaks
    peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates)

    max_val = np.amax(voltage)

    keep_peaks = np.array([])
    for index in peaks:
        if voltage[index] >= 0.7 * max_val:
            keep_peaks = np.append(keep_peaks, index)

    keep_peaks = keep_peaks.astype(int)

    # just take first two peaks to get instantaneous. not that accurate obviously, could give more control
    beat_diff = time[keep_peaks[1]] - time[keep_peaks[0]] # seconds per beat
    bpm = 1 / beat_diff * 60 # beats per minute

    return bpm




import numpy as np
import scipy.signal


def calc_avg_hr(time, voltage):
    """ calculate average HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :return: heart rate in bpm
    """

    # indices = peakutils.indexes(voltage, thres = 0.95*np.max(voltage), min_dist = 1000)

    fs = 1 / (time[1] - time[0])

    rates = np.arange(40, 200, 20) / 60
    peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates / 10)

    # calling average HR the avg over whole time period
    # TODO: give control in function input parameter

    num_beats = peaks.size

    time_elapsed = time[peaks[num_beats-1]] - time[peaks[0]]  # seconds

    bpm = (num_beats / time_elapsed) * 60  # beats per minute

    return bpm


# if __name__ == '__main__':


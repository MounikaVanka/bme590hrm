def calc_inst_hr(time, voltage):
    """ calculate instantaneous HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :return: heart rate in bpm
    """
    import numpy as np
    import scipy.signal

    # get sampling rate
    fs = 1 / (time[1] - time[0])

    rates = np.array([np.size(voltage)/200])  # search width
    # find peaks
    peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates)

    max_val = np.amax(voltage)

    keep_peaks = np.array([])
    for index in peaks:
        if voltage[index] >= 0.7 * max_val:
            keep_peaks = np.append(keep_peaks, index)

    keep_peaks = keep_peaks.astype(int)

    """ just take last two peaks to get instantaneous.
    not that accurate obviously
    """
    beat_diff = time[keep_peaks[1]] - time[keep_peaks[0]]   # seconds per beat
    bpm = int(1 / beat_diff * 60)    # beats per minute

    return bpm

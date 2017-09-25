import numpy as np
import scipy.signal


def calc_avg_hr(time, voltage, window):
    """ calculate average HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :param window: window size to search for avg heart rate, s
    :return: bmp: array of heart rates in window, bpm
    """

    # indices = peakutils.indexes(voltage, thres = 0.95*np.max(voltage), min_dist = 1000)

    # get sample rate
    fs = 1 / (time[1] - time[0])

    # search width
    rates = np.array([np.size(voltage)/200])

    # get peaks.
    peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates)

    max_val = np.amax(voltage)

    keep_peaks = np.array([])
    for index in peaks:
        if voltage[index] >= 0.7 * max_val:
            keep_peaks = np.append(keep_peaks, index)

    keep_peaks = keep_peaks.astype(int)

    wind = np.array([])
    bpm = np.array([])

    k = 0  # for new window start index
    for i, ind in enumerate(keep_peaks):
        # if we're within one window, add the time to it
        if time[keep_peaks[i]] - time[keep_peaks[k]] <= window:
            wind = np.append(wind, time[i])
        # if we're at the end of file or end of window, calculate average and reset
        if i == np.size(keep_peaks) - 1 or time[keep_peaks[i]] - time[keep_peaks[k]] > window:
            avg_in_window = int((np.size(wind) / (time[keep_peaks[i]] - time[keep_peaks[k]])) * 60)

            bpm = np.append((bpm),(avg_in_window))
            bpm = np.ndarray.astype(bpm,int)
            # reset for next window
            if i < np.size(keep_peaks) - 2:
                k = i + 1
            wind = np.array([])

    # num_beats = keep_peaks.size
    #
    # time_elapsed = time[keep_peaks[num_beats-1]] - time[keep_peaks[0]]  # seconds
    #
    # bpm = (num_beats / time_elapsed) * 60  # beats per minute
    
    return bpm




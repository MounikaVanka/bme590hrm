def calc_avg_hr(time, voltage, window):
    """ calculate average HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :param window: window size to search for avg heart rate, s
    :return: array of heart rates in window, bpm
    """
    import numpy as np
    # import scipy.signal
    import peakutils

    # get sample rate
    fs = 1 / (time[1] - time[0])

    # search width
    # rates = np.array([np.size(voltage)/200])

    # get peaks.
    # peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates)

    # try using peakutils
    kernel = np.ones(200) / 200
    base = np.convolve(voltage, kernel, 'same')
    voltage = voltage - base
    peaks = peakutils.indexes(voltage, .73, int(np.size(voltage) / 200))

    avg_val = np.average(voltage)

    std_dev = np.std(voltage)

    # keep_peaks = np.array([])
    # for index in peaks:
    #     if voltage[index] >= avg_val + 1.2 * std_dev:
    #         keep_peaks = np.append(keep_peaks, index)
    # keep_peaks = keep_peaks.astype(int)

    wind = np.array([])
    bpm = np.array([])

    keep_peaks = peaks

    k = 0  # for new window start index
    for i, ind in enumerate(keep_peaks):
        # if we're within one window, add the time to it
        if time[keep_peaks[i]] - time[keep_peaks[k]] <= window:
            wind = np.append(wind, time[i])
        # if at the end of file or end of window, calculate average and reset
        if i == np.size(keep_peaks) - 1 or \
           time[keep_peaks[i]] - time[keep_peaks[k]] > window:
            avg_in_window = int((np.size(wind) / (time[keep_peaks[i]] -
                                time[keep_peaks[k]])) * 60)

            bpm = np.append(bpm, avg_in_window)
            bpm = np.ndarray.astype(bpm, int)
            # reset for next window
            if i < np.size(keep_peaks) - 2:
                k = i + 1
            wind = np.array([])

    bpm_out = np.zeros(len(time))
    bpm_ind = 0
    for count, t in enumerate(time):
        if t <= bpm_ind+1 * window and bpm_ind <= len(bpm) -1:
            bpm_out[count] = bpm[bpm_ind]
        else:
            bpm_out[count] = bpm_out[count-1]
            bpm_ind += 1

    bpm_out = np.ndarray.astype(bpm_out, int)

    # num_beats = keep_peaks.size
    #
    """ time_elapsed = time[keep_peaks[num_beats-1]] -
                            time[keep_peaks[0]]  # seconds
    """
    #
    # bpm = (num_beats / time_elapsed) * 60  # beats per minute

    return bpm_out

def calc_inst_hr(time, voltage):
    """ calculate instantaneous HR from ECG data input

    :param time: numpy array, seconds
    :param voltage: numpy array, mV
    :return: numpy array, heart rate between beats in bpm
    """
    import numpy as np
    # import scipy.signal
    # import matplotlib.pyplot as plt
    import peakutils

    # get sampling rate
    fs = 1 / (time[1] - time[0])

    rates = np.array([np.size(voltage)/200])  # search width
    # find peaks
    # peaks = scipy.signal.find_peaks_cwt(voltage, fs / rates)

    # base = peakutils.baseline(voltage, 3, 1000)
    # voltage = voltage - base

    kernel = np.ones(200) / 200
    base = np.convolve(voltage, kernel, 'same')
    voltage = voltage - base
    peaks = peakutils.indexes(voltage, .73, int(np.size(voltage)/200))

    # avg_val = np.average(voltage)
    # std_dev = np.std(voltage)
    # keep_peaks = np.array([])
    # for index in peaks:
    #     if voltage[index] >= avg_val + 1.2 * std_dev:
    #         keep_peaks = np.append(keep_peaks, index)

    # print(avg_val)
    # print(std_dev)
    # print(len(peaks), len(keep_peaks))

    # keep_peaks = keep_peaks.astype(int)
    keep_peaks = peaks

    # plt.plot(time, voltage)
    # plt.plot(time[keep_peaks], voltage[keep_peaks], '.r')
    # plt.show()

    bpm = np.zeros(len(time))
    curr_keep_ind = 0
    for count, t in enumerate(time):

        # if in keep_peaks and t less than t of new peak
        if curr_keep_ind < len(keep_peaks)-1 and \
                        t <= time[keep_peaks[curr_keep_ind]]:

            beat_diff = time[keep_peaks[curr_keep_ind + 1]] -\
                        time[[keep_peaks[curr_keep_ind]]]
            bpm[count] = int(1/beat_diff * 60)

        # if after last peak time, make bpm 0
        elif curr_keep_ind == len(keep_peaks) - 1:
            bpm[count] = 0

        # otherwise set curr bpm to end of last and go to next keep ind
        else:
            bpm[count] = bpm[count-1]
            curr_keep_ind += 1

    bpm = np.ndarray.astype(bpm, int)

    return bpm

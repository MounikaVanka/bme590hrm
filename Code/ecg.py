class ECG:
    def __init__(self, file, window, brady_max, tachy_min):
        """Initializes ECG class given input parameters. Performs analysis
        on data in file to find heart condition, as well as instantaneous
        and average heart rate in BPM.

        :param file: str, name of input csv file
        :param window: int, window size in seconds for diagnosis
        :param brady_max: int, upper threshold for bradycardia in BPM
        :param tachy_min: int, lower threshold for tachycardia in BPM
        :return: none
        """
        from input_csv_file import read_in
        from calc_inst_hr import calc_inst_hr
        import numpy as np
        from checking_threshold import checking_threshold
        from calc_avg_hr import calc_avg_hr

        self.input_file = file
        self.window = window
        self.threshold = (brady_max, tachy_min)
        (self.time, self.voltage) = read_in(self.input_file)

        self.avg_hr = calc_avg_hr(self.time, self.voltage, self.window)
        self.inst_hr = calc_inst_hr(self.time, self.voltage)

        window_states = np.array([])
        for row in self.avg_hr:
            window = checking_threshold(self.threshold[0], self.threshold[1],
                                        row)
            window_states = np.append(window_states, window)
        self.condition = window_states

    def write_file(self):
        """ Writes ECG class data to file for heart condition and average and
        instantaneous heart rate to output file.

        :return: none
        """
        from write_output_file import write_to_file
        output_file = self.input_file.split(".")[0] + "_out"
        output_file = '.'.join([output_file, 'txt'])
        write_to_file(output_file, self.inst_hr, self.avg_hr[0],
                      self.condition)

    def print_results(self):
        """ Prints ECG class data for heart condition and average and
        instantaneous heart
        rate to output file.

        :return: none
        """
        print('Instantaneous Heart Rate is:', self.inst_hr, '\n',
              'Average Heart Rate is:', self.avg_hr[0], '\n',
              'The condition for each window is', self.condition)

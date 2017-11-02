class ECG:
    def __init__(self, **kwargs):
        """Initializes ECG class given input parameters. Performs analysis
        on data in file to find heart condition, as well as instantaneous
        and average heart rate in BPM.

        :param file: str, name of input csv file (optional, but must be provided with
                    params window, brady_max, and tachy_max)
        :param window: int, window size in seconds for diagnosis
        :param brady_max: int, upper threshold for bradycardia in BPM
        :param tachy_min: int, lower threshold for tachycardia in BPM
        :return: none
        """
        from calc_inst_hr import calc_inst_hr
        import numpy as np
        from checking_threshold import checking_threshold
        from calc_avg_hr import calc_avg_hr

        if len(kwargs) == 2:
            self.time = np.array(kwargs['time'])
            self.voltage = np.array(kwargs['voltage'])
            self.inst_hr = calc_inst_hr(self.time, self.voltage)
            self.threshold = (40, 120)
        elif len(kwargs) == 3:
            self.window = kwargs['window']
            self.time = np.array(kwargs['time'])
            self.voltage = np.array(kwargs['voltage'])
            self.avg_hr = calc_avg_hr(self.time, self.voltage, self.window)
            self.threshold = (40, 120)
        elif len(kwargs) == 4:
            from input_csv_file import read_in
            self.input_file = kwargs['file']
            self.window = kwargs['window']
            self.threshold = (kwargs['brady_max'], kwargs['tachy_min'])
            [self.time, self.voltage] = read_in(self.input_file)
            self.avg_hr = calc_avg_hr(self.time, self.voltage, self.window)
            self.inst_hr = calc_inst_hr(self.time, self.voltage)

        if len(kwargs) == 2:
            data = self.inst_hr
        else:
            data = self.avg_hr
        tachy_states = np.array([], dtype=bool)
        brady_states = np.array([], dtype=bool)
        for row in data:
            window = checking_threshold(self.threshold[0],
                                        self.threshold[1], row)
            brady_states = np.append(brady_states, window[0])
            tachy_states = np.append(tachy_states, window[1])
        self.brady_states = brady_states
        self.tachy_states = tachy_states

    def write_file(self):
        """ Writes ECG class data to file for heart condition and average and
        instantaneous heart rate to output file.

        :return: none
        """
        from write_output_file import write_to_file
        output_file = self.input_file.split(".")[0] + "_out"
        output_file = '.'.join([output_file, 'txt'])
        write_to_file(output_file, self.inst_hr, self.avg_hr,
                      self.brady_states, self.tachy_states)

    def print_results(self):
        """ Prints ECG class data for heart condition and average and
        instantaneous heart rate to output file.

        :return: none
        """
        print('Instantaneous Heart Rate is:', self.inst_hr, '\n',
              'Average Heart Rate is:', self.avg_hr, '\n',
              'Bradycardia Annotations:', self.brady_states, '\n'
              'Tachycardia Annotations:', self.tachy_states, '\n'
              )

    def get_average(self):
        """ Returns ECG averaging period, time interval vector, average heart
        rate for each interval, and tachycardia and bradycardia annotations
        for each interval

        :return: dictionary containing keys averaging_period, time_interval,
        average_heart_rate, tachycardia_annotations, bradycardia_annotations
        """
        import numpy as np
        time = np.ndappend.tolist(self.time)
        avg_period = self.window
        avg_hr = np.ndarray.tolist(self.avg_hr)
        brady_cardia = np.ndarray.tolist(self.brady_states)
        tachy_cardia = np.ndarray.tolist(self.tachy_states)
        output = {"average_heart_rate": avg_hr, "bradycardia_annotations":
                  brady_cardia, "avg_period": avg_period, "time_interval":
                  time, "tachycardia_annotations":
                  tachy_cardia}
        return output

    def get_summary(self):
        """ Returns ECG time vector, instantaneous heart rate for each time
        interval, and tachycardia and bradycardia annotations for each interval

        :return: dictionary containing keys time, instanteous_heart_rate,
        tachycardia_annotations, bradycardia_annotations
        """
        import numpy as np
        time = np.ndappend.tolist(self.time)
        inst_hr = np.ndarray.tolist(self.inst_hr)
        tachy_annotations = np.ndarray.tolist(self.tachy_states)
        brady_annotations = np.ndarray.tolist(self.brady_states)
        output = {'time': time, 'instantaneous_heart_rate': inst_hr,
                  'tachycardia_annotations': tachy_annotations,
                  'bradycardia_annotations': brady_annotations}
        return output

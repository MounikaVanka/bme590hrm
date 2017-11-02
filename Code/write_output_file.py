def write_to_file(output_filename, inst_hr, avg_hr, brady_states,
                  tachy_states):
    """ Writes the output to a separate file

    :param: output_filename: str, name for output
    :param inst_hr: int instantaneous heart rate
    :param avg_hr: int avg_heart_rate
    :param brady_states: array of boolean Bradycardia indicators
    :param tachy_states: array of boolean Tachycardia indicators

    """
    import sys

    file = open(output_filename, "w")
    file.write('Instantaneous Heart Rate: ')
    file.write(str(inst_hr))
    file.write("\n")
    file.write('Average Heart Rate: ')
    file.write(str(avg_hr))
    file.write("\n")
    file.write('Bradycardia Annotations: ')
    file.write(str(brady_states))
    file.write("\n")
    file.write('Tachycardia Annotations: ')
    file.write(str(tachy_states))
    file.close()

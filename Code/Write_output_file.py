def write_to_file(output_filename, inst_hr, avg_hr, output):
    """ Writes the output to a separate file

    :param: output_filename: str, name for output
    :param inst_hr: int instantaneous heart rate
    :param avg_hr: int avg_heart_rate
    :param output: string output

    """
    import sys

    file = open(output_filename, "w")
    file.write('Instantaneous Heart Rate: ')
    file.write(str(inst_hr))
    file.write("\n")
    file.write('Average Heart Rate: ')
    file.write(str(avg_hr))
    file.write("\n")
    file.write('Condition: ')
    file.write(str(output))
    file.close()

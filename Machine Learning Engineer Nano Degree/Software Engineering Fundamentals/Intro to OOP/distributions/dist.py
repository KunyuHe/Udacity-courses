import math
import matplotlib.pyplot as plt


class Distribution():
    """
    Generic distribution class for calculating and
    visualizing a probability distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
    	data_list (list of floats) a list of floats extracted from the data file
    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """
        Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated

        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        """
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()

        self.data = data_list[:]


if __name__ == "__main__":
    pass

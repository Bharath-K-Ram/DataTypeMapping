# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 4:34 PM 25/05/23 using PyCharm
import numpy as np
import pandas

from utils.constants import SAMPLE_SIZE, SYS_RANDOM_SAMPLING, RANDOM_SAMPLING
import random as rd


class Sampling:
    """
    In sampling, we select a group of individuals from a target population. This group of individuals forms a sample
    """
    def __init__(self, data):
        self.data: pandas.DataFrame = data
        self.size: int = 0
        self.systematic_sample_data = None
        self.simple_random_data = None
        self.shape_dict = {}

    def sampling_data(self) -> pandas.DataFrame:
        """
        From this method we call two sampling techniques and find the technique which gives more non-empty value and
        return the data by using that sampling technique
        :return: pandas.DataFrame
        """
        self.size = self.data.shape[0]
        key_with_max_value = max(self.shape_dict, key=lambda key: self.shape_dict[key])
        return self.systematic_sample_data if key_with_max_value == SYS_RANDOM_SAMPLING else self.simple_random_data

    @staticmethod
    def size_of_systematic_sampling(data) -> int:
        return data.shape[0] // SAMPLE_SIZE

    def systematic_sampling(self):
        """
        systematic sampling is a type of probability sampling, where a random selection of the first element for the
        sample is made and then the subsequent items are selected using fixed or systematic intervals until reaching the
        desired sample size.
        :return: None
        """
        interval = Sampling.size_of_systematic_sampling(self.data)
        start = rd.randint(0, interval)
        indexes = np.arange(start, self.size, step=interval)
        self.systematic_sample_data = self.data.iloc[indexes]
        self.shape_dict[SYS_RANDOM_SAMPLING] = self.systematic_sample_data.dropna().shape[0]

    def random_sampling(self):
        """
        As the name suggests, we pick the sample, at random. There is no pattern, and it’s a purely random selection
        using random package.
        :return: None
        """
        self.simple_random_data = self.data.sample(n=SAMPLE_SIZE)
        self.shape_dict[RANDOM_SAMPLING] = self.simple_random_data.dropna().shape[0]

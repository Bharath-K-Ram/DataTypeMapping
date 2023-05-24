# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 12:13 PM 24/05/23 using PyCharm
import pandas as pd

from utils.logging_config import log


class DataTypeMappingController:
    def __init__(self, model, data):
        """

        :param model: Loaded model of paraphrase-multilingual-MiniLM-L12-v2l
        :param data: csv file which is then converted to pandas.DataFrame in controller method
        """
        self.model = model
        self.data = data
        self.dim = None
        self.log_flag = False

    def controller(self):
        self.data = pd.read_csv(self.data)
        self.dim = self.data.shape
        log(logger=self.log_flag, msg=f"Shape of input {self.dim}", exception=False)

        return self.data


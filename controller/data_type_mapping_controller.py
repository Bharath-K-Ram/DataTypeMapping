# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 12:13 PM 24/05/23 using PyCharm
import pandas as pd

from model.data_sampling import Sampling
from model.pattern_matching_using_regex import PatternMatching
from model.pattern_matching_using_similarity import TextSimilarity
from utils.constants import INFO, EXCEPTION
from utils.logging_config import log


class DataTypeMappingController:
    def __init__(self, model, data):
        """
        Mapping the Crm data types with customer uploaded data fields
        :param model: Loaded model of paraphrase-multilingual-MiniLM-L12-v2l
        :param data: csv file which is then converted to pandas.DataFrame in controller method
        """
        self.model = model
        self.data = data
        self.dim = None
        self.log_flag = True
        self.sampled_data = None
        self.result_dict = {}

    def controller(self):
        """
        Data Type Mapping Controller
        :return: dictionary crm data type and list of fields that matches the crm data types.
        """
        try:
            self.data = pd.read_csv(self.data)
            self.dim = self.data.shape
            log(logger=self.log_flag, msg=f"Shape of input {self.dim}", level=INFO)
            if self.dim[0] >= 2000:
                s = Sampling(data=self.data)
                self.sampled_data = s.sampling_data()
            else:
                self.sampled_data = self.data
            log(logger=self.log_flag, msg=f"Shape of sample data {self.sampled_data.shape}", level=INFO)
            # Regex based column mapping
            pm = PatternMatching(self.data)
            self.result_dict = pm.column_mapping()
            # Similarity based column mapping
            si = TextSimilarity(model=self.model, data=self.data, data_type_mapped_dict=self.result_dict)
            self.result_dict = si.column_wise_similarity()
            return self.result_dict, self.data
        except Exception as exception:
            log(logger=True, msg=str(exception), level=EXCEPTION)

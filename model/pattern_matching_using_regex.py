# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 11:20 AM 25/05/23 using PyCharm
import re

import pandas as pd

from utils.constants import EMAIL_REGEX, EMAIL, URL_REGEX, URL, IMAGE_REGEX, IMAGE, INFO
from utils.logging_config import log


class PatternMatching:
    def __init__(self, data):
        """
        Pattern matching using regex
        :param data: pandas.DataFrame user given.
        """
        self.data = data
        self.mapped_result_dict = {}

    def column_mapping(self):
        log(logger=True, msg="Pattern Matching Class Initiated :: ", level=INFO)
        email_regex = re.compile(EMAIL_REGEX)
        url_regex = re.compile(URL_REGEX)
        image_regex = re.compile(IMAGE_REGEX)
        self.pattern_verification(regex=email_regex, data_type=EMAIL)
        self.pattern_verification(regex=url_regex, data_type=URL)
        self.pattern_verification(regex=image_regex, data_type=IMAGE)
        log(logger=True, msg="Pattern Matching Completed", level=INFO)
        log(logger=True, msg=str(self.mapped_result_dict), level=INFO)
        return self.mapped_result_dict

    def pattern_verification(self, regex, data_type):
        log(logger=True, msg=f"Pattern Verification for {data_type} :: ", level=INFO)
        data = self.data
        columns = self.data.columns
        pattern_wise_dict = {}
        for column in columns:
            pattern_wise_dict[column] = data[column].apply(lambda x: regex.search(str(x)))
            self.mapped_result_dict[data_type] = list(pd.DataFrame(pattern_wise_dict).dropna(axis=1).columns)

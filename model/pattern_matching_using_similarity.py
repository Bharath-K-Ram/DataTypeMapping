# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 11:53 AM 26/05/23 using PyCharm
import json

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from utils.constants import SINGLE_LINE_VALUES, DATA_TYPE_LIST, SIMILARITY_THRESHOLD, INFO, SINGLE_LINE, OTHER
from utils.logging_config import log


class TextSimilarity:
    def __init__(self, model, data, data_type_mapped_dict):
        self.model = model
        self.data = data
        self.data_type_mapped_dict = data_type_mapped_dict

    def column_wise_similarity(self) -> dict:
        log(logger=True, msg="Text Similarity Started :: ", level=INFO)
        log(logger=True, msg=str(self.data_type_mapped_dict), level=INFO)
        self.data_type_mapping_by_text_similarity()
        return self.data_type_mapped_dict

    def data_type_mapping_by_text_similarity(self):
        """
        Find the similarity between the crm data types and the user given data's column.Two separate types of similarity
        mapping is done.
        - For single line data type we compare the crm default single line fields with user given data fields
        - For Other data types we compare Crm default data types of Email, Phone, Url etc with User given data fields
        :return: Dictionary with Crm data type and list of user defined data fields
        """
        user_defined_fields = self.data.columns
        crm_data_type_single_line = SINGLE_LINE_VALUES
        crm_data_type_single_line_excluded = DATA_TYPE_LIST
        similarity_matrix_single_line = cosine_similarity(np.array(self.model.encode(user_defined_fields)),
                                                          np.array(self.model.encode(crm_data_type_single_line)))
        similarity_matrix_single_line_excluded = cosine_similarity(np.array(self.model.encode(user_defined_fields)),
                                                                   np.array(self.model.encode(
                                                                       crm_data_type_single_line_excluded)))
        single_line_df = pd.DataFrame(similarity_matrix_single_line, columns=crm_data_type_single_line,
                                      index=user_defined_fields)
        single_line_excluded_df = pd.DataFrame(similarity_matrix_single_line_excluded,
                                               columns=crm_data_type_single_line_excluded, index=user_defined_fields)
        self.data_type_mapped_dict[SINGLE_LINE] = []
        self.filtering_and_mapping_similar_column(single_line_df, SINGLE_LINE)
        self.filtering_and_mapping_similar_column(single_line_excluded_df, OTHER)

    def filtering_and_mapping_similar_column(self, df, data_type):
        df = df.to_json()
        df = json.loads(df)

        for column_name, column_data in df.items():
            max_value = max(column_data.values())
            if max_value > SIMILARITY_THRESHOLD:
                max_index = max(column_data, key=column_data.get)
                if data_type != SINGLE_LINE:
                    if column_name in self.data_type_mapped_dict:
                        values_list = self.data_type_mapped_dict[column_name]
                        if max_index not in values_list:
                            values_list.append(max_index)
                            self.data_type_mapped_dict[column_name] = values_list
                    else:
                        self.data_type_mapped_dict[column_name] = [max_index]
                else:
                    single_list = self.data_type_mapped_dict[SINGLE_LINE]
                    if max_index not in single_list or len(single_list) == 0:
                        single_list.append(max_index)
                        self.data_type_mapped_dict[SINGLE_LINE] = single_list
        return self.data_type_mapped_dict

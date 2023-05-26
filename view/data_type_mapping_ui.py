# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 11:45 AM 24/05/23 using PyCharm
import pandas as pd
import streamlit as st

from controller.data_type_mapping_controller import DataTypeMappingController


def data_type_mapping_ui(model):
    with st.sidebar:
        st.header("Data type mapping")
        uploaded_file = st.file_uploader("Choose a file", type=['csv'], help="Upload a file of type csv")
        button_flag = False if uploaded_file is not None else True
        action = st.button("Submit", disabled=button_flag)
        if action and not button_flag:
            obj = DataTypeMappingController(model, uploaded_file)
            if obj is not None:
                result_dict, data = obj.controller()
                return result_dict, data
    return None, None

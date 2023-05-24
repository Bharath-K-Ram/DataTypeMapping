# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 11:45 AM 24/05/23 using PyCharm
import streamlit as st

from controller.data_type_mapping_controller import DataTypeMappingController


def data_type_mapping_ui(model):
    with st.sidebar:
        st.header("Data type mapping")
        uploaded_file = st.file_uploader("Choose a file", type=['csv'], help="Upload a file of type csv")
        if uploaded_file is not None:
            obj = DataTypeMappingController(model, uploaded_file)
            return obj.controller()

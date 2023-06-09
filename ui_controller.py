# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 11:29 AM 24/05/23 using PyCharm
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer

from view.data_type_mapping_ui import data_type_mapping_ui

st.set_page_config(
    page_title="Data Type Mapping",
    page_icon="ui_config/zia-img.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_resource
def _load_model():
    """
    This method will load the model once the server is started and store it in the cache.
    :return: SentenceTransformer model
    """
    _model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    return _model


if __name__ == "__main__":
    model = _load_model()
    mapped_result, input_data = data_type_mapping_ui(model)

    if mapped_result is not None:
        st.header("User Uploaded File")
        st.dataframe(input_data)
        st.header("Crm data types mapped with User given data")
        st.write(mapped_result)


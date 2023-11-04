"""Client side for prepexcel applciation"""
import streamlit as st
import pandas as pd
from excel_filter import filter_smaller_value


pd.set_option("display.max_columns", None)

st.header("Prep Excel")
st.markdown("Some explanation ...")


content = st.file_uploader("Upload File", type="xlsx")
if content:
    try:
        df = pd.read_excel(content)
        st.markdown("Actual Content:")
        st.dataframe(df)
        try:
            filtered_df = filter_smaller_value(df, 20)
            st.markdown("Filtered Content:")
            st.dataframe(filtered_df)
        except:
            st.error("Please upload a valid excel file")
    except:
        st.error("Please upload a valid excel file")

    
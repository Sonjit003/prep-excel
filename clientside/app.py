import streamlit as st
import pandas as pd
from excel_processing import reading_input_data
from excel_processing import delete_tours_from_collumnB
from excel_processing import drop_lane_by_count
from excel_processing import change_date_formate


pd.set_option("display.max_columns", None)

st.header("prep Excel")

st.markdown("This is the code that will give me a excel file that will need to create tour for TAP scheduleing team in wednesday and Friday")
content = st.file_uploader("upload the downloaded file frome FMC", type= "csv")
if content:
    try:
        df = pd.read_csv(content)
        st.markdown("actula content")
        st.dataframe(df)
        try:
            filtered_df = reading_input_data("inputdata.csv")
            df = delete_tours_from_collumnB(filtered_df)
            df = drop_lane_by_count(df)
            df = change_date_formate(df, "%m/%d/%y")
            st.markdown("Filtered Content:")
            st.dataframe(df)
        except:
            print("Hei please upload the correct file")
    except:
        print("please upload the coreect file")

download_buton = st.download_button("clcik me to download the file", "csv")    



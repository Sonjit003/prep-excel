import streamlit as st
import pandas as pd
# from excel_processing import reading_input_data
# from excel_processing import delete_tours_from_collumnB
# from excel_processing import drop_lane_by_count
# from excel_processing import change_date_formate

import excel_processing as ep

pd.set_option("display.max_columns", None)

st.header("prep Excel")

st.markdown("This is the code that will give me a excel file that will need to create tour for TAP scheduleing team in wednesday and Friday")
content = st.file_uploader("upload the downloaded file frome FMC", type= "csv")
def download_output():
    if content:
        try:
            df = pd.read_csv(content)
            st.markdown("actula content")
            st.dataframe(df)
            try:
                filtered_df = ep.reading_input_data("inputdata.csv")
                df = ep.delete_tours_from_collumnB(filtered_df)
                df = ep.drop_lane_by_count(df)
                df = ep.change_date_formate(df, "%m/%d/%y")
                st.markdown("Filtered Content:")
                st.dataframe(df)
            except:
                print("Hei please upload the correct file")
        except:
            print("please upload the coreect file")
    return df
df = download_output()
df = df.to_csv().encode('utf-8')

download_buton = st.download_button("button",data = df, file_name= "inputdata.csv", mime='text/csv')   
db = pd.read_csv(download_buton)
st.markdown("download the data from here")
st.dataframe(db)



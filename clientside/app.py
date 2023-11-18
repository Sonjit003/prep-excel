import streamlit as st
import pandas as pd
# from excel_processing import reading_input_data
# from excel_processing import delete_tours_from_collumnB
# from excel_processing import drop_lane_by_count
# from excel_processing import change_date_formate
from datetime import datetime
import excel_processing as ep

pd.set_option("display.max_columns", None)

st.header("prep Excel")

def create_filename() -> str:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d-%H-%M-%S")
    return f"{formatted_date}_vrid-pull.csv.csv"

class PrepExcel:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.filtered_df = None

    

    def prepare_vrid_pull(self):
        filtered_df = ep.delete_tours_from_collumnB(self.df)
        filtered_df = ep.drop_lane_by_count(filtered_df)
        filtered_df = ep.change_date_formate(filtered_df, "%m/%d/%y")
        self.filtered_df = filtered_df

st.markdown("This is the code that will give me a excel file that will need to create tour for TAP scheduleing team in wednesday and Friday")
content = st.file_uploader("upload the downloaded file frome FMC", type= "csv")
if content:
    try:
        df = pd.read_csv(content, low_memory=False)
        # st.markdown("actula content")
        # st.dataframe(df)
        excel_processor = PrepExcel(df)
        try:
            excel_processor.prepare_vrid_pull()
            st.markdown("Processed Content:")
            st.dataframe(excel_processor.filtered_df)
        except:
            print("Here, please upload the correct file")
    except:
        print("please upload the coreect file")

    df_as_str = df.to_csv().encode('utf-8')
    file_name = create_filename()
    download_buton = st.download_button("Download Processed File", data = df_as_str, file_name=file_name, mime='text/csv')



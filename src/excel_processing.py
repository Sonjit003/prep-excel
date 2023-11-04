from pathlib import Path

import pandas as pd

INPUT_PATH = Path("data").joinpath("input")
OUTPUT_PATH = Path("data").joinpath("output")


def reading_input_data(filename: str) -> pd.DataFrame:
    """_summary_: this function will read the from the directory


    Args:
        filename (str): he filename willbe a string. this function will read data as per the filename

    Returns:
        pd.DataFrame: after reading the data this funtion willl reaturn a DataFrame
    """
    file_path = INPUT_PATH.joinpath(filename)
    df = pd.read_csv(file_path, low_memory=False)
    return df


# df = reading_input_data("inputdata.csv")
def delete_tours_from_collumnB(df: pd.DataFrame):
    """_summary_:this function filter the rows that have tour already and delete all  the tours from column B and keep blank rows.
    Args:
        df (pd.DataFrame): it takes the Dataframe that we read from function "reading input data"

    Returns:
        _type_: DataFrame
    """

    df = df[df["Tour ID"].isnull()]
    return df


def lentg_of_Lane(text: str) -> bool:
    """_summary_:in Cloumn "j" it split the lane by "->" and counts the number of sites in the lane and put it in a new column


      Args:
        text (str): count number of "->" in column "j"

    Returns:
        bool: it return bool value
    """

    p = len(text.split("->"))
    if p == 2:
        return True
    return False


def drop_lane_by_count(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_:This Function change the date formate of column AM and Ao from "ddmmyy" to "MMDDYY"


    Args:
         df (pd.DataFrame): it will change the date formate

     Returns:
         pd.DataFrame: return DataFrame with changed date formate
    """

    lane_count = df["Lane"].apply(lambda x: lentg_of_Lane(x))
    # df["lane_count"] = lane_count
    df = df.loc[lane_count]
    return df


def change_date_formate(df: pd.DataFrame, date_formate: str) -> pd.DataFrame:
    """_summary_: this function chnage date formate in column AM and in column AO

    Args:
        df (pd.DataFrame): DataFrame get from "drop_lane_by_count" function
        date_formate (_type_): change the date formate to MMDDYYYY

    Returns:
        pd.DataFrame: The retun is a DataFrame and it is the output file
    """
    columns = ["Scheduled Truck Arrival - 1 date", "Scheduled Truck Arrival - 2 date"]
    for column in columns:
        df[column] = pd.to_datetime(df[column], format="mixed").dt.strftime(
            date_formate
        )
    df["Corresponding CPT"] = pd.to_datetime(
        df["Corresponding CPT"], format="mixed"
    ).dt.strftime("%m/%d/%y  %H:%M")
    return df


def main():
    df = reading_input_data("inputdata.csv")
    df = delete_tours_from_collumnB(df)
    df = drop_lane_by_count(df)
    df = change_date_formate(df, "%m/%d/%y")
    df.to_csv(OUTPUT_PATH.joinpath("vrid-pull.csv"), index=False)


if __name__ == "__main__":
    main()

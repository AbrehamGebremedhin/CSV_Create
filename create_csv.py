import os
import pandas as pd


def create_csv(directory: str, output: str):
    """This function creates a csv of filename with their corresponding label using 
        their parent directory act as the label, gets the main directory as an input
        and returns a csv file named to a given output name."""
    list_dir = os.listdir(path=directory)
    df = pd.DataFrame()

    for i in list_dir:
        file_list = []
        print("Creating " + i + "...")
        for file in os.listdir(path=directory + "/" + i):
            file_list.append(file)
            df1 = pd.DataFrame({"filename": file_list, "label": i})
        df = df.append(df1)

    df.to_csv(f"{output}.csv", index=False)

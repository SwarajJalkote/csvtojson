import pandas as pd
import json
import typing
import traceback


def read_csv_file(input_file, input_del, column_names):
    '''
    This function reads the csv file and takes column_names parameter to filter out the data.\n
    Description:
        input_file: csv file which needs to be processed
        input_del: delimiter used in input file. Default: , (comma)
        column_names: list of names of columns which you want to extract from csv
    '''
    if input_file.endswith() != ".csv":
        if column_names != []:
            return pd.read_csv(filepath_or_buffer=input_file, 
                                sep=input_del,
                                usecols=column_names,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
        else:
            return pd.read_csv(filepath_or_buffer=input_file, 
                                sep=input_del,
                                skip_blank_lines=True,
                                encoding="UTF-8",
                                engine="python")
    else:
        traceback.print_exc()
        raise Exception("Input file is incorrect. Check the extension. e.g. input_file.csv")
    return []

def csv_to_json(input_file, input_del=",", column_names=list()) -> str:
    '''
    This function converts the csv file into JSON and takes column_names parameter to filter out the data.\n
    Description:
        input_file: csv file which needs to be processed and converted to json
        input_del: delimiter used in input file. Default: , (comma)
        column_names: list of names of columns which you want to extract from csv
    '''
    csv_data = read_csv_file(input_file, input_del, column_names)
    if csv_data != []:
        column_names = list(csv_data)
        for indx, col in enumerate(column_names):
            if "Unnamed" in col:
                column_names[indx] = f"col{indx}"

        for row in csv_data.itertuples(index=False):
            pass
        
    else:
        pass

if __name__ == "__main__":

    input_file = "input_file.csv"
    input_del = ","
    json_data = csv_to_json(input_file, input_del, column_names=[])


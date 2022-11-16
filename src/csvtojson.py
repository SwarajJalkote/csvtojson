import pandas as pd
import json
import typing
import traceback


def read_csv_file(input_file, input_del, column_names) -> pd.DataFrame:
    '''
    This function reads the csv file and takes column_names parameter to filter out the data.\n
    Description:
        input_file: csv file which needs to be processed
        input_del: delimiter used in input file. Default: , (comma)
        column_names: list of names of columns which you want to extract from csv
    '''
    if input_file.endswith(".csv"):
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
    return pd.DataFrame()

def csv_to_json(input_file, input_del=",", column_names=list()) -> str:
    '''
    This function converts the csv file into JSON and takes column_names parameter to filter out the data.\n
    Description:
        input_file: csv file which needs to be processed and converted to json
        input_del: delimiter used in input file. Default: , (comma)
        column_names: list of names of columns which you want to extract from csv
    '''
    csv_data = read_csv_file(input_file, input_del, column_names)
    json_data = []
    if csv_data.empty == False:
        column_names = list(csv_data)
        for indx, col in enumerate(column_names):
            if "Unnamed" in col:
                column_names[indx] = f"col{indx}"

        for row in csv_data.itertuples(index=False):
            temp = {}
            for key, row in zip(column_names, list(row)):
                temp[key] = row
            json_data.append(temp)
    else:
        return f"Input_File: {input_file} is empty"


    return json.dumps(json_data, indent=4)


if __name__ == "__main__":

    input_file = "input_file.cs"
    input_del = ","
    json_data = csv_to_json(input_file, input_del, column_names=['Rank in India','Changes Rank from last Year','Forbes 2000 rank in World','Changes Rank from last Year','Name','Headquarters'])
    with open("output_data.json", 'w') as f:
        f.write(json_data)

import pytest
import pandas as pd
from csvtojson import read_csv_file, csv_to_json

def test_read_csv_file():
    df = {
        'Rank in India': [1,2],
        'Changes Rank from last Year': [0, 0],
        'Forbes 2000 rank in World': [54, 105],
        'Name': ['Reliance Industries', 'State Bank of India'],
        'Headquarters': ['Mumbai', 'Mumbai']
    }

    assert_dataframe = pd.DataFrame(df)
    
    x = read_csv_file("input_file.csv", ",", column_names=[])

    pd.testing.assert_frame_equal(assert_dataframe, x)


def test_csv_to_json():
    x = csv_to_json("input_file.csv", ",", column_names=[])

    print(x)
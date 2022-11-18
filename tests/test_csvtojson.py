import pytest
import pandas as pd
import json
from src.csvtojsonlib import read_csv_file, csv_to_json

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
    assert_json = [
    {
        "Rank in India": 1,
        "Changes Rank from last Year": 0,
        "Forbes 2000 rank in World": 54,
        "Name": "Reliance Industries",
        "Headquarters": "Mumbai"
    },
    {
        "Rank in India": 2,
        "Changes Rank from last Year": 0,
        "Forbes 2000 rank in World": 105,
        "Name": "State Bank of India",
        "Headquarters": "Mumbai"
    }
    ]
    x = csv_to_json("input_file.csv", ",", column_names=[])
    x = json.loads(x)
    assert assert_json == x


def test_read_csv_file_exception():
    with pytest.raises(Exception, match="Input file is incorrect. Check the extension. e.g. input_file.csv"):
        read_csv_file("Input.cs", ",", [])
# csvtojsonlib
Python Library to convert CSV file into JSON

# Description: 
**PyPi:** https://pypi.org/project/csvtojsonlib/ <br />
![image](https://user-images.githubusercontent.com/29909977/202204672-c35eaee8-801b-45c1-9734-a4554dabaef5.png)

# Installation:
```python
pip install csvtojsonlib
```

# Functions:

 ```python
 csv_to_json(input_file, input_del=",", column_names=list())
 ```
| Parameter | Description |
| --- | --- |
| `input_file` | csv file which needs to be processed and converted to json |
| `input_del` | delimiter used in input file. Default: , (comma) |
| `column_names` | list of names of columns which you want to extract from csv |

```python
read_csv_file(input_file, input_del, column_names)
```
| Parameter | Description |
| --- | --- |
| `input_file` | csv file which needs to be processed |
| `input_del` | delimiter used in input file. Default: , (comma) |
| `column_names` | list of names of columns which you want to extract from csv |


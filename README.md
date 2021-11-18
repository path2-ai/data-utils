# data-utils
Use this repository to easily convert your source files (csv, txt, excel, json, html) into record-oriented JSON files that can be uploaded into onetask.

## Installation
Clone this repository and install the dependencies into an environment (e.g. Conda) using
`pip install -r requirements.txt`

## How to use
This tool is CLI-based, so you can just open a terminal, change directory into this repository, and then execute
`python json_converter.py --filename <your_filename>`.

For instance, if you have a file `my_input_file.csv` with the following data
```csv
running_id,text
1,hello world!
2,how are you doing?
3,if you have any questions about onetask - contact us anytime
```
, running `python json_converter.py --filename my_input_file.csv` will output

```json
[
    {
        "running_id": 1,
        "text": "hello world!"
    },
    {
        "running_id": 2,
        "text": "how are you doing?"
    },
    {
        "running_id": 3,
        "text": "if you have any questions about onetask - contact us anytime"
    }
]
```

You can configure the conversion in typical Pandas style by providing arguments, e.g. for the delimiter of csv files such as
`python json_converter.py --filename my_input_file.csv --sep ';'`. 

We currently support:
- [Excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) (supports xls, xlsx, xlsm, xlsb, odf, ods and odt file extensions read from a local filesystem or URL)
- [CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) (also working for .txt files)
- [HTML](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)
- [JSON](https://pandas.pydata.org/docs/reference/api/pandas.io.json.read_json.html)

## Support
If you have any questions or run into issues, feel free to contact us anytime.

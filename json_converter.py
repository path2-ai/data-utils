import argparse
import pandas as pd
from wasabi import msg
import sys


def convert_to_json(filename: str, **kwargs):
    """
    Loads a file, and converts it into a record-oriented JSON file.

    Args:
        filename (str): name of the source file
    """
    if filename.count(".") == 0:
        msg.fail(f"File type is not given: please check the docs")
        sys.exit()
    filetype = filename.split(".")[-1]
    if filetype in ["xls", "xlsm", "xlsb", "odf", "ods", "odt"]:
        filetype = "xlsx"
    filename_json = f"{'.'.join(filename.split('.')[:-1])}.json"
    msg.info(f"Convertig {filename} to {filename_json}")

    try:
        if filetype == "csv":
            df = pd.read_csv(filename, **kwargs)
        elif filetype == "xlsx":
            df = pd.read_excel(filename, **kwargs)
        elif filetype == "html":
            df = pd.read_html(filename, **kwargs)
        elif filetype == "json":
            df = pd.read_json(filename, **kwargs)
        else:
            msg.fail(f"File Type '{filetype}' is not known: please check the docs")
            sys.exit()
    except TypeError as e:
        msg.fail(str(e))
        sys.exit()
    df.to_json(filename_json, orient="records")
    msg.good("Converted and stored file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert various file types into JSON records."
    )
    parser.add_argument(
        "--filename",
        type=str,
        help="name of the source file",
    )
    parser.add_argument("--doublequote")
    parser.add_argument("--flavor")
    parser.add_argument("--typ")
    parser.add_argument("--names")
    parser.add_argument("--dayfirst")
    parser.add_argument("--keep_default_dates")
    parser.add_argument("--false_values")
    parser.add_argument("--lineterminator")
    parser.add_argument("--memory_map")
    parser.add_argument("--precise_float")
    parser.add_argument("--keep_default_na")
    parser.add_argument("--na_filter")
    parser.add_argument("--convert_dates")
    parser.add_argument("--orient")
    parser.add_argument("--converters")
    parser.add_argument("--convert_axes")
    parser.add_argument("--parse_dates")
    parser.add_argument("--encoding_errors")
    parser.add_argument("--warn_bad_lines")
    parser.add_argument("--storage_options")
    parser.add_argument("--nrows")
    parser.add_argument("--skipinitialspace")
    parser.add_argument("--infer_datetime_format")
    parser.add_argument("--escapechar")
    parser.add_argument("--error_bad_lines")
    parser.add_argument("--attrs")
    parser.add_argument("--index_col")
    parser.add_argument("--numpy")
    parser.add_argument("--displayed_only")
    parser.add_argument("--mangle_dupe_cols")
    parser.add_argument("--date_parser")
    parser.add_argument("--quoting")
    parser.add_argument("--encoding")
    parser.add_argument("--dialect")
    parser.add_argument("--skiprows")
    parser.add_argument("--decimal")
    parser.add_argument("--sep")
    parser.add_argument("--skip_blank_lines")
    parser.add_argument("--iterator")
    parser.add_argument("--convert_float")
    parser.add_argument("--delim_whitespace")
    parser.add_argument("--true_values")
    parser.add_argument("--na_values")
    parser.add_argument("--quotechar")
    parser.add_argument("--lines")
    parser.add_argument("--usecols")
    parser.add_argument("--cache_dates")
    parser.add_argument("--sheet_name")
    parser.add_argument("--date_unit")
    parser.add_argument("--squeeze")
    parser.add_argument("--dtype")
    parser.add_argument("--comment")
    parser.add_argument("--delimiter")
    parser.add_argument("--prefix")
    parser.add_argument("--chunksize")
    parser.add_argument("--skipfooter")
    parser.add_argument("--float_precision")
    parser.add_argument("--thousands")
    parser.add_argument("--engine")
    parser.add_argument("--on_bad_lines")
    parser.add_argument("--header")
    parser.add_argument("--low_memory")
    parser.add_argument("--match")
    parser.add_argument("--compression")
    parser.add_argument("--keep_date_col")
    parser.add_argument("--verbose")

    args = parser.parse_args()
    kwargs = {}
    for arg in vars(args):
        val = getattr(args, arg)
        if val is not None and arg != "filename":
            kwargs[arg] = val

    convert_to_json(args.filename, **kwargs)

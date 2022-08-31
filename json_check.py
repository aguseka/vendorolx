#!/usr/bin/env python3


import pandas as pd
import sys
import argparse
from cleantext import clean
from pathlib import Path

# logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filepath", type=str, help="fill out with the path to your files:"
    )
    parser.add_argument(
        "--operation",
        type=str,
        help="csv: merge csv files into csv, json: merge json files into csv, excel: merge excel files",
    )
    parser.add_argument(
        "--result",
        type=str,
        help="fill out with the result file name in csv, json, or excel depend on operation type",
    )
    parser.add_argument(
        "--source",
        nargs="+",
        help="fill with source file1.csv, file2.csv, etc.csv or source file1.json, file2.json, etc.json",
    )
    # parser.add_argument('--target', help=" fill with the file you want to be inserted with the column" )
    args = parser.parse_args()
    if args.operation == "csv":
        merge_csv_to_csv(args)
    if args.operation == "json":
        merge_json_to_csv(args)
    if args.operation == "excel":
        merge_excel_to_excel(args)


def merge_csv_to_csv(args):
    data_path = Path(args.filepath)
    source = data_path / args.source
    headers = [
        "category_id",
        "prop_addrs",
        "lst_val",
        "lt",
        "lb",
        "proc_status",
        "human_url",
        "user_name",
        "link_whatsapp",
        "user_url",
    ]
    dataframes = pd.concat([pd.read_csv(f) for f in source])
    clean_data = dataframes.drop_duplicates()
    with open(args.result, "w+") as result:
        return clean_data.to_csv(result, fieldnames=headers)


def merge_json_to_csv(args):
    data_path = Path(args.filepath)
    source = data_path / args.source
    headers = [
        "category_id",
        "prop_addrs",
        "lst_val",
        "lt",
        "lb",
        "proc_status",
        "human_url",
        "user_name",
        "link_whatsapp",
        "user_url",
    ]
    dataframes = pd.concat([pd.read_json(f) for f in source])
    clean_data = dataframes.drop_duplicates()
    with open(args.result, "w+") as result:
        return clean_data.to_csv(result, fieldnames=headers)


def merge_excel_to_excel(args):
    data_path = Path(args.filepath)
    source = data_path / args.source
    headers = [
        "category_id",
        "prop_addrs",
        "lst_val",
        "lt",
        "lb",
        "proc_status",
        "human_url",
        "user_name",
        "link_whatsapp",
        "user_url",
    ]
    dataframes = pd.concat([pd.read_excel(f) for f in source])
    clean_data = dataframes.drop_duplicates()
    with open(args.result, "w+") as result:
        return clean_data.to_excel(result, fieldnames=headers)


# from thi part below are still non functional
# further exploration needed on how to run all of this class from command line.


if __name__ == "__main__":
    main()


"""    
logging.info("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(a,b)))
device_values = check_append(sys.argv[1], sys.argv[2])
"""

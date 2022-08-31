#!/usr/bin/env python3


import glob
import pandas as pd

# ambil semua file dengan ekstensi .json
source_json = glob.glob(
    "/Users/ekaaditya/Desktop/ScrapeResult/**/*.json", recursive=True
)
# masukkan ke dalam data frame panda
if source_json:

    print("Processing %s" % len(source_json) + " json files")
    df = pd.DataFrame()
    for file_json in source_json:

        try:
            df = df.append(pd.read_json(file_json))
        except pd.errors.EmptyDataError:
            print("Found empty file : %s" % file_json)
            continue

    df.sort_values("user_url", inplace=True)
    print("Before drop_duplicates() of json files:%s" % len(df))
    df.drop_duplicates(subset="user_url", keep="last", inplace=True)
    # ubah dan simpan dalam data frame
    print("After drop_duplicates()of json files:%s" % len(df))
else:
    print("No more json files jumping on the bed!")

source = glob.glob("/Users/ekaaditya/Desktop/ScrapeResult/**/*.csv", recursive=True)
if source:

    print("Processing %s" % len(source) + " csv files")
    df = pd.DataFrame()
    for file in source:
        try:
            df = df.append(pd.read_csv(file))
        except pd.errors.EmptyDataError:
            print("Found empty file : %s" % file)
            continue

    # print("Isi filenya adalah sbb: %s" % len(df))
    df.sort_values("user_url", inplace=True)
    before = len(df)
    df.drop_duplicates(subset="user_url", keep="last", inplace=True)
    after = len(df)
    duplicates = before - after
    print("Found:%s " % duplicates + " duplicates, and has been dropped")
    print("Total: %s" % after + " singular data")
    with open("master.csv", "w+") as result:
        df.to_csv(result, header=True)
else:
    print("No more csv files jumping on the bed!")

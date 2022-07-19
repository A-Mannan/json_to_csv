import os
import pandas as pd


def convert_in_text(obj):
    if type(obj) is list:
        return ";".join(obj)
    elif type(obj) is dict:
        return ";".join(obj.values())
    else:
        return obj


def convert_json_to_csv(json_filename):
    csv_filename = os.path.basename(json_filename).split(".")[0] + ".csv"
    chunks = pd.read_json(json_filename, lines=True, chunksize=10000)
    header = True
    for chunk in chunks:
        for column in chunk:
            chunk[column] = chunk[column].apply(convert_in_text)
        chunk.to_csv(
            csv_filename,
            header=header,
            mode="a",
            escapechar="\\",
        )
        header = False
        # chunk.to_csv(
        #     "test.csv",
        #     header=header,
        #     mode="a",
        #     escapechar="\\"
        # )
        # header = False
        # break


if __name__ == "__main__":
    convert_json_to_csv(r"C:\Users\Dell\Downloads\meta_Electronics.json")
    # convert_json_to_csv("test.json")
    # with open(r"C:\Users\Dell\Downloads\meta_Electronics.json") as f:
    #     d=1
    #     while True:
    #         data = eval(f.readline())
    #         if data["tech1"]:
    #             print(data["tech1"])
    #             print(d)
    #             break
    #         d+=1

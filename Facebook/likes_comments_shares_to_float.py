import pandas as pd
import csv

path = "E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\csv_docs_def\posts4.csv"
posts = pd.read_csv(path, quotechar='"', quoting=csv.QUOTE_ALL, encoding="utf-8", low_memory=False)

def simplify_columns(row):
    if row["likes"][-1] == "K":
        row["likes"] = float(row["likes"][:-1])*1000
    else:
        row["likes"] = float(row["likes"])
    num_comments = row["num_comments"].split()[0]
    if num_comments[-1] == "K":
        row["num_comments"] = float(num_comments[:-1])*1000
    else:
        row["num_comments"] = float(num_comments)
    num_shares = row["num_shares"].split()[0]
    if num_shares[-1] == "K":
        row["num_shares"] = float(num_shares[:-1])*1000
    else:
        row["num_shares"] = float(num_shares)
    return row

# Apply the function to each row
posts = posts.apply(simplify_columns, axis=1)

path2 = "E:\Gianluca\Master Big Data Pisa\Progetto_Finale\Agricolo\Facebook\csv_docs_def\posts4.csv"
posts.to_csv(path2, sep=',', na_rep='', index=False, encoding="utf-8", quoting=csv.QUOTE_ALL, quotechar='"')
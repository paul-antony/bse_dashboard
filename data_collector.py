import csv
from bsedata.bse import BSE



def read_bookmark(fname = "bookmark.csv"):
    with open(fname) as csvfile:
        wishlist = [x['id'] for x in csv.DictReader(csvfile, fieldnames = ["id","Name"])]

        return wishlist

def collect_data(id_list):

    bse = BSE(update_codes = True)
    data = []

    for id in id_list:
        print(id)
        quote = bse.getQuote(id)
        temp = {}

        temp["Name"] = quote["companyName"]
        temp["Value"] = quote["currentValue"]
        temp["Change"] = quote["change"] if (quote["change"][0] == '-') else '+' + quote["change"]
        temp["Change_type"] = quote["change"][0] if (quote["change"][0] == '-') else '+'

        print(temp)

        data.append(temp)

    return data

def bookmark_stock_data():

    return collect_data(read_bookmark())
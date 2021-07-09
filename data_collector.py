import csv
from bsedata.bse import BSE



def read_bookmark(fname = "bookmark.csv"):
	with open(fname) as csvfile:
		wishlist = {x["name"][2:-1]:x["id"] for x in csv.DictReader(csvfile, fieldnames = ["id","name"])}
		return wishlist

def collect_data(id_list):

	data = []
	for id in id_list:
		data.append(company_price_data(id))

	return data

def bookmark_stock_data():

	wishlist = read_bookmark()
	id_list = [wishlist[x] for x in wishlist.keys()]
	print(id_list)

	return collect_data(id_list)



def company_price_data(id):

	bse = BSE()

	quote = bse.getQuote(id)
	company = {}
	company["Id"] = id
	company["Name"] = quote["companyName"]
	company["Value"] = quote["currentValue"]
	company["Change"] = quote["change"] if (quote["change"][0] == '-') else '+' + quote["change"]
	company["Change_type"] = quote["change"][0] if (quote["change"][0] == '-') else '+'

	return company


def company_data(id):
	bse = BSE()

	quote = bse.getQuote(id)
	company = {}

	company["Id"] = id
	company["Name"] = quote["companyName"]
	company["Value"] = quote["currentValue"]
	company["Change"] = quote["change"] if (quote["change"][0] == '-') else '+' + quote["change"]
	company["Change_type"] = quote["change"][0] if (quote["change"][0] == '-') else '+'

	company["ftweekHigh"] = quote["52weekHigh"]
	company["ftweekLow"] = quote["52weekLow"]
	company["dayHigh"] = quote["dayHigh"]
	company["dayLow"] = quote["dayLow"]
	company["previousClose"] = quote["previousClose"]
	company["previousOpen"] = quote["previousOpen"]

	return company


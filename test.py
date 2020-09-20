from bsedata.bse import BSE
b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)
codelist = ["500116", "512573"]
for code in codelist:
    quote = b.getQuote(code)
    print(quote["companyName"])
    print(quote["currentValue"])
    print(quote["change"])
    print(type(quote["change"]),int(quote["change"]))


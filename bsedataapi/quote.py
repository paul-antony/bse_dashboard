"""

    MIT License

    Copyright (c) 2018 - 2024 Shrey Dabhi

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""

from bsedataapi.exceptions import InvalidStockException
from bsedataapi.helper import COMMON_REQUEST_HEADERS, driver
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs







def quote(scripCode: str) -> dict:
    baseurl = """https://m.bseindia.com/StockReach.aspx?scripcd="""

    driver.get(baseurl + scripCode)
    c = driver.page_source
    #driver.close()
    #res = requests.get(baseurl + scripCode, headers=COMMON_REQUEST_HEADERS)
    #c = res.content

    soup = bs(c, "lxml")

    res = {}

    for span in soup("span"):
        updt_date = soup.find("span", id="strongDate").text.split("-")[1].strip()
        updt_diff = dt.strptime(updt_date, "%d %b %y | %I:%M %p") - dt.now()
        if updt_diff.days < -7:
            error_text = ""
            error_text_element = soup.find("td", id="tdDispTxt")
            if error_text_element is not None:
                error_text = error_text_element.text
            raise InvalidStockException(status=error_text)
        try:
            if span["class"][0] == "srcovalue":
                try:
                    if span["id"] == "spanchangVal":
                        res["change"] = span.string.split("(")[0].strip()
                        res["pChange"] = span.string.split("(")[1].strip()[:-2]
                except KeyError:
                    res["currentValue"] = span.strong.string
            elif span["class"][0] == "companyname":
                res["companyName"] = span.string
        except KeyError:
            try:
                if span["id"] == "lblPBdate":
                    try:
                        res["priceBand"] = span.string.split(":")[1].strip()
                    except AttributeError:
                        res["priceBand"] = ""
                elif span["id"] == "strongDate":
                    res["updatedOn"] = span.string.split("-")[1].strip()
            except KeyError:
                continue

    for td in soup("td"):
        try:
            if td["id"] == "tdCShortName":
                res["securityID"] = td.string.strip()
            elif td["id"] == "tdscripcode":
                res["scripCode"] = td.string.strip()
            elif td["id"] == "tdgroup":
                res["group"] = td.string.strip()
            elif td["id"] == "tdfacevalue":
                res["faceValue"] = td.string.strip()
            elif td["id"] == "tdIndustry":
                res["industry"] = td.string.strip()
            elif td["id"] == "tdpcloseopen":
                res["previousClose"] = td.string.split("/")[0].strip()
                res["previousOpen"] = td.string.split("/")[1].strip()
            elif td["id"] == "tdDHL":
                res["dayHigh"] = td.string.split("/")[0].strip()
                res["dayLow"] = td.string.split("/")[1].strip()
            elif td["id"] == "td52WHL":
                res["52weekHigh"] = td.string.split("/")[0].strip()
                res["52weekLow"] = td.string.split("/")[1].strip()
            elif td["id"] == "tdWAp":
                res["weightedAvgPrice"] = td.string.strip()
            elif td["id"] == "tdTTV":
                res["totalTradedValue"] = td.string.strip() + " Cr."
            elif td["id"] == "tdTTQW":
                res["totalTradedQuantity"] = td.string.split("/")[0].strip() + " Lakh"
                res["2WeekAvgQuantity"] = td.string.split("/")[1].strip() + " Lakh"
            elif td["id"] == "tdMktCapVal":
                res["marketCapFull"] = td.string.split("/")[0].strip() + " Cr."
                res["marketCapFreeFloat"] = td.string.split("/")[1].strip() + " Cr."
        except KeyError:
            continue

    if res.get("priceBand", "") != "":
        for tbody in soup("tbody"):
            try:
                if tbody["id"] == "PBtablebody":
                    data = tbody.contents[2]
                    res["upperPriceBand"] = data.contents[1].string.strip()
                    res["lowerPriceBand"] = data.contents[2].string.strip()
            except KeyError:
                continue

    buy = {}
    sell = {}
    for td in soup("td"):
        try:
            if td["id"] == "tdBQ1":
                buy["1"] = {
                    "quantity": td.string,
                    "price": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdBQ2":
                buy["2"] = {
                    "quantity": td.string,
                    "price": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdBQ3":
                buy["3"] = {
                    "quantity": td.string,
                    "price": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdBQ4":
                buy["4"] = {
                    "quantity": td.string,
                    "price": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdBQ5":
                buy["5"] = {
                    "quantity": td.string,
                    "price": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdSP1":
                sell["1"] = {
                    "price": td.string,
                    "quantity": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdSP2":
                sell["2"] = {
                    "price": td.string,
                    "quantity": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdSP3":
                sell["3"] = {
                    "price": td.string,
                    "quantity": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdSP4":
                sell["4"] = {
                    "price": td.string,
                    "quantity": td.next_sibling.next_sibling.string,
                }
            elif td["id"] == "tdSP5":
                sell["5"] = {
                    "price": td.string,
                    "quantity": td.next_sibling.next_sibling.string,
                }
        except KeyError:
            continue
    res["buy"] = buy
    res["sell"] = sell

    return res

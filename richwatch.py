#!/usr/bin/env python3

from binance.spot import Spot 
import datetime
from datetime import timedelta
from pprint import pprint
import os

APIKEY=os.environ["BINANCEKEY"]
APISECRET=os.environ["BINANCESECRET"]

client = Spot(key=APIKEY, secret=APISECRET)

# Get account information
spotsum = client.account_snapshot("SPOT")

# print report
print ("Richwatch 0.2")
assetsum = 0.0
# once the last snapshot is selected, crypto with 0 value is ignored, while crypto I have is accounted
for balance in client.account()["balances"]:
    if float(balance["free"]) != 0 or float(balance["locked"]) != 0:
        assetqty = float(balance["free"]) + float(balance["locked"])
        if balance["asset"] != "USDT":
            # if the crypto is not called USDT, it must be multiplied by its value in USDT
            assetvalue = float(client.avg_price(balance["asset"] + "USDT")["price"])
        else:
            # if the crypto is called USDT, it must be multiplied by 1
            assetvalue = 1.0 
        usvalue = assetvalue * assetqty
        assetsum += usvalue
        print("  %s: US$ %.2f = %.2f @ US$ %.2f" % (balance["asset"], usvalue, assetqty, assetvalue ))
brlvalue = float(client.avg_price("USDTBRL")["price"])
# total is also measured in BRL for additional commodity
print("Total: US$ %.2f / R$ %.2f" % (assetsum, assetsum * brlvalue))

# spotsum is a json with snapshots of crypto values, so we get the last entry (-1) and translate the date to print
#print (" Data from: %s" % (datetime.datetime.fromtimestamp(int(spotsum["snapshotVos"][-1]['updateTime'])/1000)))
#assetsum = 0.0
#
## once the last snapshot is selected, crypto with 0 value is ignored, while crypto I have is accounted
#for balance in spotsum["snapshotVos"][-1]['data']['balances']:
#    if float(balance["free"]) != 0:
#        assetqty = float(balance["free"])
#        if balance["asset"] != "USDT":
#            # if the crypto is not called USDT, it must be multiplied by its value in USDT
#            assetvalue = float(client.avg_price(balance["asset"] + "USDT")["price"])
#        else:
#            # if the crypto is called USDT, it must be multiplied by 1
#            assetvalue = 1.0 
#        usvalue = assetvalue * assetqty
#        assetsum += usvalue
#        print("  %s: US$ %.2f = %.2f @ US$ %.2f" % (balance["asset"], usvalue, assetqty, assetvalue ))
#brlvalue = float(client.avg_price("USDTBRL")["price"])
## total is also measured in BRL for additional commodity
#print("Total: US$ %.2f / R$ %.2f" % (assetsum, assetsum * brlvalue))
#
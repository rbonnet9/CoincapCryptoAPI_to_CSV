#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ricardo Bonnet, Kura Labs, Cohort 3
# Created Date: Thurs September 15 23:59:59 EST 2022
# ================================================================================================================================
""" This script will pull from the Coincap API and create a CSV file with the requested Info (i.e. Symbol, Price in USD, etc.) """
# ================================================================================================================================
# Imports: requests, csv, datetime, date, os.path, pytz
# =============================================================================

import requests
import csv
from datetime import datetime
from datetime import date
import os.path 
import pytz

# Convert timezone to EST which is my timezone. Can be modified to accommodate for different timezones, depending on what timezone user wants in CSV file when data is pulled from API
datetime.now(pytz.timezone('US/Eastern'))

# Specifying API URL path from which information will be pulled
url = 'http://api.coincap.io/v2/assets'

# HTTP Headers, Accept and Content-Type used to inform the server of the multimedia type (MIME) being requested, JSON in this case.
headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json'
}

# Responses is constructing and sending a request. Formatted in our case as: (HTTP method, referencing url variable, headers being requested and equated to variable headers, and 'data' refers to the dictionary of data listed in the API which we are requesting from)
# Empty list called ourdata created
# Headers to be listed in CSV file are created under the headers variable. Each header will correspond to a header being requested from the API
# File_exists checks for the existence of the file named 'coincap{todays date}.csv' before we attempt to modify it in any form
responses = requests.request("GET", url,headers=headers, data= {})
myjson = responses.json()
ourdata = []
headers = ['Symbol', 'Name', 'Current Price(USD)', 'Current Supply', 'Volume of USD In Last 24Hrs', 'Percent Change In Last 24Hrs', 'Current Time']
file_exists = os.path.exists(f'coincap{date.today()}.csv')

# Iterating over the Python list using a For loop. Pulling the requested variables/data, i.e. symbol, name, priceUsd, etc., as named in the data dictionary of the API
# ourdata was our empty list initially, appended it with the data pulled from the data assets within the API. Now contains all the information from the variables in listing
# datetime listed last to show when the information was pulled, to be listed in the CSV file
for x in myjson['data']:
    listing = [x['symbol'],x['name'],x['priceUsd'],x['supply'],x['volumeUsd24Hr'],x['changePercent24Hr'],datetime.now()]
    ourdata.append(listing)

# Writing multiple rows with headers and corresponding data to CSV file
# f' used to format our string, a+ opens file for reading and appending (writing at end of file). The file is being created as if it doesn't exist
# newline removes whitespace that exist between each row of data so that it's uniform and together
with open(f'coincap{date.today()}.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(headers)
    writer.writerows(ourdata)

# Once operation is successful, let user know via print
print('Success! CSV File created with requested info')
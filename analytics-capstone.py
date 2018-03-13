
import os
import requests
from pprint import pprint
import pandas as pd

api_key = os.environ['NOAA_API_KEY']
headers = {'token': api_key}

endpoint = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations"
payload = {
    'datasetid' : 'GSOM',
    'locationcategoryid' : 'HYD_REG',
    'startdate' : '2000-01-01',
    'enddate' : '2000-01-31'
}
response = requests.get(endpoint, headers=headers, params=payload)
response = response.json()
pprint(response)

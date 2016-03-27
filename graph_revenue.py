# Ignore all this crap ---------
import httplib2
from apiclient.discovery import build
from oauth2client import client
from decimal import *
from datetime import datetime
import requests
import collections
from oauth2client.service_account import ServiceAccountCredentials
import sys

# Do you want a different date range? Change it here!
START_DATE = '2016-03-14'
END_DATE = '2016-03-26'

# Program starts here!
def main():
    # 1. Get the dashboard data and format it
    dashboard_data = as_dashboard_data(with_headers(get_revenues()))

    # 2. Push it to the Cyfe dashboard
    response = push_to_dashboard(dashboard_data)

    # 3. Report back what happened - did it work?
    show_error_or_success_message(response)

# Connects to the Analytics API and downloads the transaction revenues
def get_revenues():
    print('Getting data from analytics...')
    return analytics_service().data().ga().get(
        ids='ga:118417785',
        start_date=START_DATE,
        end_date=END_DATE,
        dimensions='ga:date',
        metrics='ga:transactionRevenue',
        max_results=10000
    ).execute()

# This connects to analytics and makes sure we're authorised to download the data
def analytics_service():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secrets.json',
        ['https://www.googleapis.com/auth/analytics.readonly'])
    http = credentials.authorize(httplib2.Http())
    return build('analytics', 'v3', http=http)

# All this is to convert the data from Analytics API format to Cyfe API format
def with_headers(data):
    headers = extract_headers(data)
    rows = extract_rows(data)
    return [dict(zip(headers, row)) for row in rows]

def extract_rows(data):
    return data['rows']

def extract_headers(data):
    return [header['name'] for header in data['columnHeaders']]

def as_dashboard_data(rows):
    return { 'data': [as_ordered_dict(row) for row in rows], 'onduplicate': { 'Revenue': 'replace' } }

def as_ordered_dict(row):
    return collections.OrderedDict([('Date', row['ga:date']), ('Revenue', row['ga:transactionRevenue'])])

# Now for the exciting bit - push it to the Cyfe API!
def push_to_dashboard(data):
    print('Pushing data to Cyfe dashboard...')
    return requests.post(sys.argv[0], json = data)

# Boring. Just report back on what just happened. Did it work?
def show_error_or_success_message(response):
    if response.status_code == 200:
        print('Data pushed successfully!')
    else:
        print('Uh oh, looks like there was an error: ' + response.json()['message'])

# Kick things off.
if len(sys.argv) == 1:
    main()
else:
    print("Whoops. You need to enter your Cyfe widget URL when running this command.")
    print("Type: python graph_revenue.py your-cyfe-widget-url")
    print("Example: python graph_revenue.py https://app.cyfe.com/api/push/56f7a767cbd212158125742061285")

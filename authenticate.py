import sys
from apiclient.discovery import build
from oauth2client import client

CLIENT_ID = "446748390608-mifmice6kfahp8k6o0o4c3qj1n3vvkvp.apps.googleusercontent.com"
CLIENT_SECRET = "Tg-bpq4qcdAmE-GcD5qg2uYk"
def authorize_with_flow():
    flow = client.OAuth2WebServerFlow(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope='https://www.googleapis.com/auth/analytics.readonly',
        user_agent='Analytics Python Client Library',
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    authorize_url = flow.step1_get_authorize_url()
    print('Log into the Google Account you use to access your Analytics account and go to the following URL: \n%s\n' % (authorize_url))
    print('After approving the token enter the verification code (if specified).')
    code = input('Code: ').strip()
    try:
        credential = flow.step2_exchange(code)
    except client.FlowExchangeError:
        print('Authentication has failed')
        sys.exit(1)
    else:
        print('OAuth 2.0 authorization successful!\n\n'
               'Your access token is:\n %s\n\nYour refresh token is:\n %s'
               % (credential.access_token, credential.refresh_token))
        return credential

authorize_with_flow()
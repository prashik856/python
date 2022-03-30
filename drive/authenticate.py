import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

class Authenticate:
    def __init__(self, token, credentials, scopes):
        self.creds = None
        # validate from token
        if os.path.exists(token):
            self.creds = Credentials.from_authorized_user_file(token, scopes)
        
        # if no valid token available, user needs to login
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file(credentials, scopes)
                self.creds = self.flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(token, 'w') as token_file:
                token_file.write(self.creds.to_json())
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Service:
    def __init__(self, api_name, api_version, credentials, logging):
        try:
            self.service = build(api_name, api_version, credentials=credentials)
        except HttpError as error:
            logging.error(f'An error occurred: {error}')
        except Exception as e:
            print(e)
            logging.error("Error occured while creating drive service")
            raise RuntimeError
        logging.info("Successfully created drive service")
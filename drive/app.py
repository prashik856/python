import time
import logging
import datetime

from drive.config import Config
from drive.authenticate import Authenticate
from drive.service import Service
from drive.search import SearchFolder, SearchFile
from drive.create import CreateFolder, CreateFile
from drive.delete import DeleteFile

def main():
    # Load config
    config = Config("config.json")
    # current day
    current_day = datetime.datetime.today().day

    # Create log file
    time_millis = str(int(time.time() * 1000))
    log_file_name = config.logging_directory + "/secrets_backup_" + time_millis
    logging.basicConfig(filename=log_file_name, level=logging.DEBUG)
    
    logging.info("Creating access token")
    authenticate = Authenticate(config.token, config.credentials, config.scopes)
    
    logging.info("Create drive service")
    drive_service = Service(config.api_name, config.api_version, authenticate.creds, logging)

    logging.info("Searching if %s directory exists" % (config.drive_backup_directory))
    search_result = SearchFolder(drive_service.service, config.drive_backup_directory, logging)

    folder_id = None
    if search_result.found:
        logging.info("Directory exists. Skipping directory creation.")
        folder_id = search_result.folder_id
    else:
        logging.info("Directory does not exists.")
        logging.info("Creating directory %s" % (config.drive_backup_directory))
        create_folder = CreateFolder(drive_service.service, config.drive_backup_directory, logging)
        folder_id = create_folder.folder_id

    config.backup_file = "%s_%s.zip" % (config.backup_file, current_day)
    logging.info("Checking if %s file exists in %s directory" % (config.backup_file, config.drive_backup_directory))
    file_search_result = SearchFile(drive_service.service, config.backup_file, folder_id, logging)

    file_id = None
    if file_search_result.found:
        # file already there. Need to delete it
        file_id = file_search_result.file_id
        logging.info("Backup file %s already present with file id %s." % (config.backup_file, file_id))
        logging.info("Need to delete %s file from Drive." % (config.backup_file))
        DeleteFile(drive_service.service, file_id, logging)
        logging.info("Creating backup file %s." % (config.backup_file))
        CreateFile(drive_service.service, config.backup_file, folder_id, logging)
    else:
        logging.info("Backup file %s not found." % (config.backup_file))
        logging.info("Creating backup file %s." % (config.backup_file))
        CreateFile(drive_service.service, config.backup_file, folder_id, logging)


if __name__ == "__main__":
    main()

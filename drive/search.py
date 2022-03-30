class SearchFolder:
    def __init__(self, service, drive_backup_directory, logging):
        page_token = None
        query = "mimeType='application/vnd.google-apps.folder' and name='" + drive_backup_directory + "'"
        self.found = False
        stopSearching = False
        directory_dict = {}
        while not self.found and not stopSearching:
            try:
                self.response = service.files().list(q=query,
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name, ownedByMe)',
                                                    pageToken=page_token).execute()
            except Exception as e:
                print(e)
                logging.error("Error occured while getting the list of directories")
                raise RuntimeError
            # If nothing returns
            if len(self.response.get('files', [])) == 0:
                logging.info("No directory found")
                self.found = False
                stopSearching = True
                break
            
            # loop through all folders found
            for folder in self.response.get('files', []):
                # Process change
                local_folder_id = folder.get('id')
                # check if already searched
                if local_folder_id in directory_dict:
                    logging.info("Duplicate searching")
                    self.found = False
                    stopSearching = True
                    break
                else:
                    directory_dict[local_folder_id] = 1
                
                # Check if name matches
                if(str(folder.get('name')) == str(drive_backup_directory)):
                    logging.info("Found directory %s" % (drive_backup_directory))
                    self.found = True
                    self.folder_id = folder.get("id")
                    break
                
                # Update page token
                page_token = self.response.get('nextPageToken', None)
                if page_token is None:
                    logging.info("No directory found")
                    self.found = False
                    stopSearching = True
                    break

class SearchFile:
    def __init__(self, service, backup_file, folder_id, logging):
        page_token = None
        query = "mimeType='application/zip' and name='" + backup_file + "' and '" + folder_id + "' in parents"
        self.found = False
        stopSearching = False
        directory_dict = {}
        while not self.found and not stopSearching:
            try:
                self.response = service.files().list(q=query,
                                                    spaces='drive',
                                                    fields='nextPageToken, files(id, name, ownedByMe)',
                                                    pageToken=page_token).execute()
            except Exception as e:
                print(e)
                logging.error("Error occured while trying to get the list of files")
                raise RuntimeError
            
            # If nothing returns
            if len(self.response.get('files', [])) == 0:
                logging.info("Backup file not found")
                self.found = False
                stopSearching = True
                break
            
            # loop through all folders found
            for file in self.response.get('files', []):
                # Process change
                local_file_id = file.get('id')

                # check if already searched
                if local_file_id in directory_dict:
                    logging.info("Duplicate searching")
                    self.found = False
                    stopSearching = True
                    break
                else:
                    directory_dict[local_file_id] = 1
                
                # Check if name matches
                if(str(file.get('name')) == str(backup_file)):
                    logging.info("Found backup file %s" % (backup_file))
                    self.found = True
                    self.file_id = file.get("id")
                    break
                
                # Update page token
                page_token = self.response.get('nextPageToken', None)
                if page_token is None:
                    logging.info("No backup file found")
                    self.found = False
                    stopSearching = True
                    break
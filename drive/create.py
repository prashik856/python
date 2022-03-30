from apiclient.http import MediaFileUpload


class CreateFolder:
    def __init__(self, drive_service, drive_backup_directory,  logging):
        self.file_metadata = {
            'name': drive_backup_directory,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        try:
            self.file = drive_service.files().create(body=self.file_metadata,
                                                    fields='id').execute()
        except Exception as e:
            print(e)
            logging.error("Error occured while creating directory %s" % (drive_backup_directory))
            raise RuntimeError
        self.folder_id = self.file.get('id')
        logging.info("Folder ID: %s" % (self.file.get('id')))


class CreateFile:
    def __init__(self, drive_service, backup_file, folder_id, logging):
        self.file_metadata = {
            'name': backup_file,
            'parents': [folder_id]
        }
        self.media = MediaFileUpload(backup_file,
                        mimetype='application/zip',
                        resumable=True)
        try:
            self.file = drive_service.files().create(body=self.file_metadata,
                                                    media_body=self.media,
                                                    fields='id').execute()
        except Exception as e:
            print(e)
            logging.error("Error occured while creating file %s" % (backup_file))
            raise RuntimeError
        self.file_id = self.file.get('id')
        logging.info("Created backup file %s with file ID %s" % (backup_file, self.file_id))
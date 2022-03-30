class DeleteFile:
    def __init__(self, drive_service, file_id, logging):
        try:
            self.delete_result = drive_service.files().delete(fileId=file_id).execute()
        except Exception as e:
            print(e)
            logging.error("Error occured while deleting file with file_id %s" % (file_id))
            raise RuntimeError
        logging.info("Successfully deleted file with file_id %s" % (file_id))
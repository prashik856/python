import json

class Config:
    def __init__(self, path):
        with open(path, 'r') as config_file:
            config_data = json.load(config_file)
        self.scopes = config_data["scopes"]
        self.token = config_data["token"]
        self.credentials = config_data["credentials"]
        self.logging_directory = config_data["logging_directory"]
        self.api_name = config_data["api_name"]
        self.api_version = config_data["api_version"]
        self.drive_backup_directory = config_data["drive_backup_directory"]
        self.backup_file = config_data["backup_file"]
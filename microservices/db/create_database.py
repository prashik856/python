import mysql.connector
import json


def readJson(file_name: str):
    with open(file_name, "r") as json_file:
        data: dict = json.load(json_file)
    return data


project_config_file: str = "project-config.json"
project_config: dict = readJson(project_config_file)

microservice_name: str = project_config["name"]

db_config: dict = project_config["mysql"]
admin_user: str = db_config["adminUser"]
admin_password: str = db_config["adminPassword"]
conn = None

try:
    conn = mysql.connector.connect(user=admin_user, password=admin_password)
except Exception as e:
    print("Error connecting to mysql database.")
    print(e)
    exit(1)
    
db_name: str = microservice_name.replace("-", "_").upper()
# create database statement

print(f"Creating database {db_name}.")
try:
    if conn and conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            
            print(f"Checking if database {db_name} exists")
            result = cursor.execute(f"show databases where `Database`='{db_name}'")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
except Exception as e:
    print(f"Error creating database {db_name}.")
    print(e)
    exit(1)

conn.close()

conn = None
# Connect to root using db_name database
try:
    conn = mysql.connector.connect(user=admin_user, password=admin_password, database=db_name)
except Exception as e:
    print(f"Error connecting to {db_name} database.")
    print(e)
    exit(1)

tenant_name: str = "TENANT_" + db_name
tenant_password: str = admin_password
print(f"Create user in new user {tenant_name} in database {db_name}")
try:
    if conn and conn.is_connected():
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE USER IF NOT EXISTS '{tenant_name}'@'localhost' IDENTIFIED BY '{tenant_password}'")

            print(f"Providing Grants to {tenant_name}")
            cursor.execute(f"GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD ON *.* TO '{tenant_name}'@'localhost'")
            cursor.execute("FLUSH PRIVILEGES")
            cursor.execute("commit")

            print(f"Checking if user {tenant_name} is created.")
            result = cursor.execute(f"SELECT User FROM mysql.user where `USER`='{tenant_name}'")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

except Exception as e:
    print(f"Error creating user {tenant_name} in db {db_name}")
    print(e)
    exit(1)

conn.close()

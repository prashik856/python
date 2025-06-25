import mysql.connector
import json


def read_json(file_name: str):
    with open(file_name, "r") as json_file:
        data: dict = json.load(json_file)
    return data


def get_admin_connection(admin_user: str, admin_password: str):
    conn = None
    try:
        conn = mysql.connector.connect(user=admin_user, password=admin_password)
    except Exception as e:
        print("Error connecting to mysql database.")
        print(e)
        exit(1)
    return conn


def create_database(conn, db_name: str):
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


def get_database_connection(admin_user: str, admin_password: str, db_name: str):
    conn = None
    # Connect to root using db_name database
    try:
        conn = mysql.connector.connect(user=admin_user, password=admin_password, database=db_name)
    except Exception as e:
        print(f"Error connecting to {db_name} database.")
        print(e)
        exit(1)
    return conn


def create_user(conn, tenant_name: str, tenant_password: str, db_name: str):
    print(f"Create user in new user {tenant_name} in database {db_name}")
    try:
        if conn and conn.is_connected():
            with conn.cursor() as cursor:
                cursor.execute(f"CREATE USER IF NOT EXISTS '{tenant_name}'@'localhost' IDENTIFIED BY '{tenant_password}'")

                print(f"Providing Grants to {tenant_name}")
                cursor.execute(f"GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD ON *.* TO '{tenant_name}'@'localhost'")
                cursor.execute("FLUSH PRIVILEGES")
                cursor.execute("commit")

                print(f"Checking if user {tenant_name} is created in db {db_name}.")
                result = cursor.execute(f"SELECT User FROM mysql.user where `USER`='{tenant_name}'")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

    except Exception as e:
        print(f"Error creating user {tenant_name} in db {db_name}")
        print(e)
        exit(1)
    conn.close()


def setup_pyway_config(pyway_config_file: str, pyway_config_template_file: str, 
                       tenant_name: str, tenant_password: str,
                       db_name: str, db_migration_dir: str) -> None:
    with open(pyway_config_template_file, 'r') as txt_file:
        pyway_config = txt_file.read()

    pyway_config = pyway_config.replace('@@TENANT_USERNAME@@', tenant_name)
    pyway_config = pyway_config.replace('@@TENANT_PASSWORD@@', tenant_password)
    pyway_config = pyway_config.replace('@@DATABASE_NAME@@', db_name)
    pyway_config = pyway_config.replace('@@DATABASE_MIGRATION_DIR@@', db_migration_dir)

    with open(pyway_config_file, 'w') as text_file:
        text_file.write(pyway_config)


project_config_file: str = "project-config.json"
project_config: dict = read_json(project_config_file)

microservice_name: str = project_config["name"]

db_config: dict = project_config["mysql"]
db_name: str = microservice_name.replace("-", "_").upper()

admin_user: str = db_config["adminUser"]
admin_password: str = db_config["adminPassword"]

tenant_name: str = "TENANT_" + db_name
tenant_password: str = admin_password

pyway_config_file: str = project_config["pywayConfig"]
pyway_config_template_file: str = project_config["pywayConfigTemplate"]
db_migration_dir: str = project_config["dbMigrationDir"]

conn = get_admin_connection(admin_user, admin_password)
create_database(conn, db_name)

conn = get_database_connection(admin_user, admin_password, db_name)
create_user(conn, tenant_name, tenant_password, db_name)

setup_pyway_config(pyway_config_file, pyway_config_template_file, 
                   tenant_name, tenant_password, db_name, db_migration_dir)


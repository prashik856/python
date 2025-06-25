import mysql.connector


def get_admin_connection(admin_user: str, admin_password: str):
    conn = None
    try:
        conn = mysql.connector.connect(user=admin_user, password=admin_password)
    except Exception as e:
        print("Error connecting to mysql database.")
        print(e)
        exit(1)
    return conn


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


def get_tenant_connection(tenant_user: str, tenant_password: str, db_name: str):
    conn = None
    # Connect to root using db_name database
    try:
        conn = mysql.connector.connect(user=tenant_user, password=tenant_password, database=db_name)
    except Exception as e:
        print(f"Error getting connection for tenant {tenant_user} for {db_name} database.")
        print(e)
    return conn

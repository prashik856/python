# Installing MYSQL

```bash
For linux installation, follow this guide:
https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/

# Download repository
https://dev.mysql.com/downloads/repo/apt/

# Install repository
sudo dpkg -i mysql-apt-config_0.8.33-1_all.deb

# Update repo
sudo apt-get update

# Install mysql server
sudo apt-get install mysql-server
# You can give your system password as root password while installation.

# Check server status
systemctl status mysql

# Using similar commands, we can start, stop, or get the status of server
# Stop server
systemctl stop mysql

# Start server
systemctl start mysql

# Restart server
systemctl restart mysql
```

# Post Installation
```bash
# The server should already be running

# Connect to server
mysql -u root -p
# Same password as the one that we provided during installation
# My System password

```

# Install Django
```bash
# Install pipx first
sudo apt install pipx

# Make sure /bin is in path
pipx ensurepath

# Install django
pipx install Django

# Installed django using python3 
python3 -m pip install Django --break-system-packages
```

# Tutorial
```bash
# Create project directory
mkdir django_tutorial

# Create django project
django-admin startproject prashiksite django_tutorial

# Run server
python3 manage.py runserver

# Follow this: https://docs.djangoproject.com/en/5.1/intro/tutorial02/

# Create polls
python3 manage.py startapp polls

# Apply migrations
python3 manage.py migrate

# Making changes in models
python3 manage.py makemigrations polls
# Remake migrations after changing any models

# See what SQL migration would look like
python3 manage.py sqlmigrate polls 0001

# Check for problems in project without touching database
python3 manage.py check

# Run migrate again to create those tables in the database
python3 manage.py migrate

# Playing with API
python3 manage.py shell
```

# Django Admin
```bash
# Creating admin user
python3 manage.py createsuperuser
# Can use superuser as admin
# We can use our password as system password

# Start development server
python3 manage.py runserver

# Make poll app modifiable in the admin
```

# Tutorial 3

Follow this: https://docs.djangoproject.com/en/5.1/intro/tutorial03/

```bash
# Writing more views


```
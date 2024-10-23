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
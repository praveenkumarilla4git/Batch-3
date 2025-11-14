#!/bin/bash
set -e
set -o pipefail
set -x

# Become root
#sudo su - # removed this command

# Update metadata (optional, good practice)
sudo dnf makecache --refresh

# Install MySQL Server
sudo dnf install mysql-server -y

# Start MySQL service
sudo systemctl start mysqld

# Set MySQL root password (automated version for repeatable setup, but not interactive)
echo "ALTER USER 'root'@'localhost' IDENTIFIED BY 'database@1';" | sudo mysql

# Secure installation mock (password is already set above)
sudo mysql_secure_installation --set-root-pass database@1

# Update MySQL config to allow remote access
sudo sed -i '/\[mysqld\]/a bind-address = 0.0.0.0' /etc/my.cnf.d/mysql-server.cnf

# Restart MySQL for config changes to apply
sudo systemctl restart mysqld

# Install Python 3 and pip
sudo dnf install python3 python3-pip -y

# Install required Python package for MySQL
pip3 install mysql-connector-python

echo "Setup completed. Now run your Python scripts as needed!"

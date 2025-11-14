#!/bin/bash
set -e
set -o pipefail
set -x

# Install MySQL Server
sudo dnf install mysql-server -y

# Start MySQL service
sudo systemctl start mysqld

# Set MySQL root password for root@localhost
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'database@1';"

# Allow remote access in MySQL config
sudo sed -i '/\[mysqld\]/a bind-address = 0.0.0.0' /etc/my.cnf.d/mysql-server.cnf

# Restart MySQL for changes to take effect
sudo systemctl restart mysqld

# Create database if not exists
sudo mysql -u root -pdatabase@1 -e "CREATE DATABASE IF NOT EXISTS school_db;"

# Grant all privileges for root from any host and flush privileges
sudo mysql -u root -pdatabase@1 -e "GRANT ALL PRIVILEGES ON school_db.* TO 'root'@'%' IDENTIFIED BY 'database@1'; FLUSH PRIVILEGES;"

echo "MySQL setup, school_db created, and remote access configured!"

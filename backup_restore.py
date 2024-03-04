import os
from datetime import datetime
import subprocess

# Input MySQL connection parameters as required
MYSQL_HOST = "localhost"
MYSQL_USER = "your_mysql_username"
MYSQL_PASSWORD = "your_mysql_password"
DATABASE_NAME = "your_database_name"

# Directory to store backup files
BACKUP_DIR = "/path/to/backup/directory"

# Function to create backup
def create_backup():
    # Creating timestamp for backup filename
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # Constructing a backup filename
    backup_filename = os.path.join(BACKUP_DIR, f"{DATABASE_NAME}-{timestamp}.sql")

    # Create backup
    try:
        subprocess.run(["mysqldump", "-u", MYSQL_USER, "-p" + MYSQL_PASSWORD, DATABASE_NAME], stdout=open(backup_filename, "w"))

        print(f"Backup created successfully: {backup_filename}")

    except Exception as e:
        print(f"Error creating backup: {e}")

# Function to restore backup
def restore_backup(backup_file):
    # Restore backup
    try:
        subprocess.run(["mysql", "-u", MYSQL_USER, "-p" + MYSQL_PASSWORD, DATABASE_NAME], stdin=open(backup_file))

        print(f"Database {DATABASE_NAME} restored successfully from backup")

    except Exception as e:
        print(f"Error restoring backup: {e}")

# Run backup function
create_backup()

# Run restoration function
restore_backup(backup_filename)

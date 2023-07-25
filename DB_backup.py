import os
from datetime import datetime
import shutil

def backup_db(serverAddr, user, password, service_name, folderPath):
    connStr = f"oracle+cx_oracle://{user}:{password}@{serverAddr}:1521/{service_name}?mode=SYSDBA"
    try:
        curr_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"DBbackup_{curr_timestamp}.dmp"
        log_file = f"DBbackp_log_{curr_timestamp}.log"
        
        expdp_path = 'C:/instantclient_tools/instantclient_19_19/expdp'
        backup_expdp_command = f"{expdp_path} {user}/{password}@{service_name} directory=. dumpfile={backup_file} logfile={log_file} full=y"
        
        os.system(backup_expdp_command)

        shutil.move(f"{backup_file}", f"{backup_folder_path}")

        print(f"Backup successfully placed in {backup_folder_path}/{backup_file}")
    except Exception as e:
        print(e)
        print("Backup failed")

if __name__ == "__main__":
    server_name = "localhost"
    user = "sys"
    password = "Sai1234"
    service_name = "orcl"
    # backup_folder_path = "C:/Users/Public/DE_DB_Backup_Automation"
    backup_folder_path = "C:/SQL2019"

    backup_db(server_name, user, password, service_name, backup_folder_path)
import subprocess
import logging

def backup_database(db_name: str, output_dir: str):
    """
    Runs a PostgreSQL dump command to backup the specified database.
    """
    logging.info(f"Starting backup for database: {db_name}")
    
    # CRITICAL ISSUE: OS Command Injection
    # Using shell=True with raw string interpolation allows an attacker 
    # to append malicious commands. 
    # Example malicious db_name: "mydb; cat /etc/passwd" or "mydb; rm -rf /"
    
    command = f"pg_dump -U admin -d {db_name} > {output_dir}/backup.sql"
    
    try:
        # shell=True executes the string exactly as typed in a real terminal
        subprocess.run(command, shell=True, check=True)
        return {"status": "success", "file": f"{output_dir}/backup.sql"}
    except subprocess.CalledProcessError as e:
        logging.error(f"Backup failed: {e}")
        return {"status": "error"}

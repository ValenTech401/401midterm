#!/usr/bin/env python3
import subprocess
import sys
import time

# Function to install required packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if paramiko is installed, if not, install it
try:
    import paramiko
except ImportError:
    install('paramiko')
    import paramiko

host = "your.test.instance.ip"
port = 22
username = "testuser"
password = "wrongpassword"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

total_attempts = 10
error_messages = []

for attempt in range(total_attempts):
    try:
        client.connect(host, port, username, password, timeout=3)
    except paramiko.AuthenticationException:
        error_messages.append("Failed login - as expected")
    except paramiko.SSHException as e:
        error_messages.append(f"SSH Protocol Error: {e}")
    except Exception as e:
        error_messages.append(f"General Error: {e}")
    finally:
        client.close()

    # Update progress bar in place
    progress = (attempt + 1) / total_attempts * 100
    progress_bar = '#' * int(progress // 10) + '.' * (10 - int(progress // 10))
    print(f"Shots fired: [{progress_bar}] {progress:.0f}%", end='\r')
    time.sleep(1)

print("\nDone")

# Ask the user if they want to view the error messages
if error_messages:
    view_messages = input("\nWould you like to view the error messages? (y/n): ")
    if view_messages.lower() == 'y':
        print("\n" + "\n".join(error_messages))

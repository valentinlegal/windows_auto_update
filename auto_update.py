'''
Windows Auto Update script

VERSION: 1.2.0
AUTHOR: Valentin Le Gal
'''

import os, shutil

desktop_path = "C:\\Users\\Valentin\\Desktop"

# Create a Windows restore point
os.system("powershell.exe Checkpoint-Computer -Description \"AutoUpdate\" -RestorePointType \"MODIFY_SETTINGS\"")

# Saves existing files on Desktop folder
existing_files = []

for item in os.listdir(desktop_path):
	existing_files.append(item)

# Updates softwares with Chocolatey
os.system("choco upgrade all -y")

# Check if there are new files on Desktop folder
for item in os.listdir(desktop_path):
	if not item in existing_files:
		# Delete these files
		try:
			if os.path.isfile(desktop_path + "\\" + item):
				os.remove(desktop_path + "\\" + item)
			elif os.path.isdir(desktop_path + "\\" + item):
				shutil.rmtree(desktop_path + "\\" + item)
		except Exception as e:
			print("[ERROR] Delete files: " + e)

# Updates Windows with PSWindowsUpdate
os.system("powershell.exe Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force")
os.system("powershell.exe Get-WindowsUpdate -MicrosoftUpdate -Verbose")
os.system("powershell.exe Install-WindowsUpdate -MicrosoftUpdate -AcceptAll")

# Restart computer
os.system("powershell.exe Restart-Computer -Force")
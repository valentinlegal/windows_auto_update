# Windows Auto Update script
# VERSION: 1.2.1
# AUTHOR: Valentin Le Gal

import os, shutil


desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
desktop_public_path = "C:\\Users\\Public\\Desktop"

# Create a Windows restore point
os.system("powershell.exe Checkpoint-Computer -Description \"AutoUpdate\" -RestorePointType \"APPLICATION_INSTALL\"")

# Saves existing files on Desktop folder
existing_files = []

for item in os.listdir(desktop_path):
	existing_files.append(item)

for item in os.listdir(desktop_public_path):
	existing_files.append(item)

# Updates softwares with Chocolatey
os.system("choco upgrade all -y")

# Check if there are new files on Personal Desktop folder
for item in os.listdir(desktop_path):
	if not item in existing_files:
		path = os.path.join(desktop_path, item)
		
		# Delete these files
		try:
			if os.path.exists(path):
				if os.path.isdir(path):
					if os.path.islink(path):
						os.unlink(path)
					else:
						shutil.rmtree(path)
				else:
					if os.path.islink(path):
						os.unlink(path)
					else:
						os.remove(path)
		except Exception as error:
			print("[ERROR] Delete files: " + error)

# Check if there are new files on Public Desktop folder
for item in os.listdir(desktop_public_path):
	if not item in existing_files:
		path = os.path.join(desktop_public_path, item)
		
		# Delete these files
		try:
			if os.path.exists(path):
				if os.path.isdir(path):
					if os.path.islink(path):
						os.unlink(path)
					else:
						shutil.rmtree(path)
				else:
					if os.path.islink(path):
						os.unlink(path)
					else:
						os.remove(path)
		except Exception as error:
			print("[ERROR] Delete files: " + error)

# Updates Windows with PSWindowsUpdate
os.system("powershell.exe Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force")
os.system("powershell.exe Get-WindowsUpdate -MicrosoftUpdate -Verbose")
os.system("powershell.exe Install-WindowsUpdate -MicrosoftUpdate -AcceptAll")

# Restart computer
os.system("powershell.exe Restart-Computer -Force")
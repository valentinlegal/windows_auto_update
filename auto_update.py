# Windows Auto Update script
# VERSION: 1.3.0
# AUTHOR: Valentin Le Gal

import os, shutil


class Computer:
	def __init__(self):
		self.desktop_private_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
		self.desktop_public_path = "C:\\Users\\Public\\Desktop"
		self.saved_files = []

	def save_folder_files(self, folder):
		for item in os.listdir(folder):
			self.saved_files.append(item)
	
	def check_new_folder_files(self, folder):
		for item in os.listdir(folder):
			if not item in self.saved_files:
				path = os.path.join(folder, item)
				
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
	
	def create_restore_point(self, name, type):
		os.system("powershell.exe Checkpoint-Computer -Description \"" + name + "\" -RestorePointType \"" + type + "\"")
		os.system("cls")

	def choco_update(self):
		os.system("choco upgrade all -y")
		os.system("cls")

	def windows_update(self):
		os.system("powershell.exe Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force")
		os.system("powershell.exe Get-WindowsUpdate -MicrosoftUpdate -Verbose")
		os.system("powershell.exe Install-WindowsUpdate -MicrosoftUpdate -AcceptAll")
		os.system("cls")

	def restart(self):
		os.system("powershell.exe Restart-Computer -Force")


# Create the Computer object
pc = Computer()

# Create a Windows restore point
pc.create_restore_point("AutoUpdate", "APPLICATION_INSTALL")

# Saves existing files on Private and Public Desktop folders
pc.save_folder_files(pc.desktop_private_path)
pc.save_folder_files(pc.desktop_public_path)

# Updates softwares with Chocolatey
pc.choco_update()

# Check if there are new files on Private and Public Desktop folders
pc.check_new_folder_files(pc.desktop_private_path)
pc.check_new_folder_files(pc.desktop_public_path)

# Updates Windows with PSWindowsUpdate
pc.windows_update()

# Restart the computer
pc.restart()
# Windows Auto Update script
# VERSION: 1.4.0
# AUTHOR: Valentin Le Gal


import os
from pyautogui import confirm
from threading import Thread
from time import sleep


class Computer:
	def __init__(self):
		self.desktop_private_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
		self.desktop_public_path = "C:\\Users\\Public\\Desktop"
		self.saved_files = []
		self.thread_running = False

	def save_folder_files(self, folder):
		for item in os.listdir(folder):
			self.saved_files.append(item)
	
	def check_new_folder_files(self, folder):
		for item in os.listdir(folder):
			if not item in self.saved_files:
				path = os.path.join(folder, item)

				# Delete these files
				try:
					if os.path.islink(path):
						os.unlink(path)
					elif os.path.isfile(path):
						os.remove(path)

				except Exception as error:
					print("[ERROR] Delete links: " + error)
	
	def create_restore_point(self, name, type):
		os.system("powershell.exe Checkpoint-Computer -Description \"" + name + "\" -RestorePointType \"" + type + "\"")
		os.system("cls")

	def choco_update(self):
		os.system("choco upgrade all -y --ignore-checksums")
		os.system("cls")

	def windows_update(self):
		os.system("powershell.exe Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force")
		os.system("powershell.exe Get-WindowsUpdate -MicrosoftUpdate -Verbose")
		os.system("powershell.exe Install-WindowsUpdate -MicrosoftUpdate -AcceptAll")
		os.system("cls")

	def restart(self):
		self.thread_running = True
		
		t1 = Thread(target=self.dialog)
		t2 = Thread(target=self.timer)

		t1.start()
		t2.start()

	def dialog(self):
		message = "Votre PC va redémarrer dans environ 60 secondes...\nVoulez-vous le redémarrer maintenant ?"
		response = confirm(message, "Windows Auto Update")

		if response == "OK":
			self.thread_running = False
			print("PC will restart")
			os.system("powershell.exe Restart-Computer -Force")
		else:
			self.thread_running = False

	def timer(self):
		cpt = 0
		while self.thread_running and cpt < 60:
			sleep(1)
			cpt = cpt + 1
		
		if cpt >= 60:
			self.thread_running = False
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

# Restart the computer (with Confirm Dialog)
pc.restart()

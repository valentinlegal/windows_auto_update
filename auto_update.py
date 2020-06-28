'''
Windows Auto Update script

VERSION: 1.0.0
AUTHOR: Valentin Le Gal
'''

import os

# Update softwares with Chocolatey
os.system("choco upgrade all -y")

# Update Windows with PSWindowsUpdate
os.system("powershell.exe Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted -Force")
os.system("powershell.exe Get-WindowsUpdate -MicrosoftUpdate -Verbose")
os.system("powershell.exe Install-WindowsUpdate -MicrosoftUpdate -AcceptAll")

# Restart computer
os.system("powershell.exe Restart-Computer -Force")
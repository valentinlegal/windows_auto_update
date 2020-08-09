# Windows Auto Update

A Python script to automatically update the software and system for Windows.

## Table of contents

- [Warnings](#warnings)
- [Running the script](#running-the-script)
- [Versions](#versions)
- [License](#license)

## Warnings

Please take note of the following warnings to avoid any problems:

- Save your work and close all running software
- Do not create new folders or files in the Desktop folder while the script is running (otherwise they will be deleted at the end of the script execution)
- Your PC will automatically restart at the end of the script execution
- The script must be run with administrator rights

## Running the script

Before executing the script you must follow these instructions:

- You must have installed the [PSWindowsUpdate](https://raymii.org/s/blog/Windows_10_Updates_with_PowerShell_PSWindowsUpdpate.html#toc_2) module to update Windows with Powershell commands
- Your software must be installed with [Chocolatey](https://chocolatey.org/) (only software installed with Chocolatey will be updated)
- Python 3 must be installed (with Chocolatey if possible)
- The following Python modules must be installed:
    - `pyautogui`
- The _Windows Restore Point_ feature must be enabled for your `C:` drive
- Create a Windows shortcut with the target: `powershell.exe python C:\PATH\TO\THE\SCRIPT\auto_update.py`
- Make the shortcut executable with administrator rights

Then to run the script:

- Double click on the previously created shortcut

## Versions

 Version |    Date    | Description
---------|------------|-------------
 1.4.0   | 2020-08-09 | Adds a confirm dialog to restart PC
 1.3.0   | 2020-07-06 | Converts the program to OOP
 1.2.1   | 2020-06-29 | Changes restore point type, fixes removal of shortcuts and automatically detects the Desktop folder
 1.2.0   | 2020-06-28 | Creates a Windows restore point before updating
 1.1.0   | 2020-06-28 | Deletes new files created in the Desktop folder (shortcuts...) after updates
 1.0.0   | 2020-06-28 | The script can update the software and the system

## License

Released under the [MIT license](LICENSE).
# Windows Auto Update

A Python script to automatically update the software and system for Windows.

## Table of contents

- [Warnings](#warnings)
- [Running the script](#running-the-script)
- [Versions](#versions)

## Warnings

Please take note of the following warnings to avoid any problems:

- Save your work and close all running software
- Your PC will restart after the execution of the script is finished

## Running the script

Before executing the script you must follow these instructions:

- You must have installed the [PSWindowsUpdate](https://raymii.org/s/blog/Windows_10_Updates_with_PowerShell_PSWindowsUpdpate.html#toc_2) module to update Windows with Powershell commands
- Your software must be installed with [Chocolatey](https://chocolatey.org/) (only software installed with Chocolatey will be updated)
- Python 3 must be installed (with Chocolatey if possible)
- The following Python modules must be installed:
    - `pytest-shutil`
- In the `auto_update.py` file:
    - Change the `desktop_path` variable (the path to your Desktop folder) on line 10

Then to run the script:

- The script must be run with administrator rights

## Versions

 Version |    Date    | Description
---------|------------|-------------
 1.1.0   | 2020-06-28 | Deletes new files created in the Desktop folder (shortcuts...) after updates
 1.0.0   | 2020-06-28 | The script can update the software and the system
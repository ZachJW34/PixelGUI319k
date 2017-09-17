# PixelGUI319k

Introduction
------------
This program was made to allows EE 319k students (or anyone who finds themselves using an ST7735R LCD screen) to easily make art for their videogame. 

Requirements and Install
------------------------
If you wish to use this program with Python 3 rather than the executable, the only requirement is PILLOW so that you can import pictures. If you are new to python, follow these steps:

1.) Install Python3 (add the python executable to your path if you are using the command line for accessability)
  *Versions of python other than python 3 and up will not work with this GUI
  *tkinter, the module that creates the GUI is included in Python3
  
2.) Navigate to the folder in which pip is installed using the command line/terminal.
  *Pip allows one to easily download libraries
  *Pip will be where your python deafault scripts are stored. 
  
3.) Do: pip3 install PILLOW 
  *If you have multiple versions of python isntalled, pip3 will make sure that PILLOW is installed in the correct directories.
  
4.) Download the PixelGUI.py file and place it in a folder. The folder will help contain images that you will import into the         program.

5.) To run the program with the command Line/terminal, do: python *your directory
  *Example, if my program is in a folder in my downloads directory, do: python C:\Users\your_username\Downloads\folder_name\PixelGUI.py
 
Configuration
-------------
No configuration required.

Troubleshooting
---------------
Program is in, let's say, alpha. It is not perfect and will have some bugs.

Maintainers
-----------
Zachary Williams

FAQ
---
Q: I define a color and click on a color and nothing happens. What do?
A: You are most likely defining a color that is not supported by tkinter. Click on View->Color Chart to see all supported colors.
   If you are using a hexadecimal value, make sure it is 16/24/32 bit color and you include the "#", such as "#000FFF000

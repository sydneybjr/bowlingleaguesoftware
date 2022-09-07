import sqlite3 as sql
import logging as log
import datetime as dt
import tkinter as tk
from tkinter import Menu


log.basicConfig(level=log.DEBUG,
                format="{asctime} {levelname:<8} {message}",
                style='{',
                filename='BLSLauncher.log',
                filemode='w')
# build window for interface
window = tk.Tk()
window.title("Bowling League Software")
window.geometry("800x600")
log.info('Setting up Window')

# Build menu bar for window
menubar = Menu(window)
window.config(menu = menubar)
log.info('Setting up Menu Bar')

# Create the file menu
file_menu = Menu(menubar, tearoff = 0)
file_menu.add_command(label="Exit Program", underline=1, command=window.destroy)
file_menu.add_separator()
log.info('set up file menu')

# Build sub menu off the New option from the file menu
new_sub_menu = Menu(file_menu, tearoff=0)
new_sub_menu.add_command(label="Create League from Template")
new_sub_menu.add_command(label="Build League")
file_menu.add_cascade(label="New", menu=new_sub_menu)
file_menu.add_separator()
log.info('Setting up sub menu')

# Create the Options menu
options_menu = Menu(menubar, tearoff = 0)
options_menu.add_command(label="Option choice 1")
log.info('Setting up Options menu')

# Create Maintenance menu
maintenance_menu = Menu(menubar, tearoff = 0)
maintenance_menu.add_command(label="Maintenance Option 1")
log.info('Setting up the Maintenance menu')

# Create Certify menu
certify_menu = Menu(menubar, tearoff=0)
certify_menu.add_command(label="Certify option 1")
log.info('Setting up Certify menu')

# Create Help Menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About")
log.info('Setting up help menu')

menubar.add_cascade(label="File",menu=file_menu,underline=0)
menubar.add_cascade(label="Options", menu=options_menu,underline=1)
menubar.add_cascade(label="Maintenance", menu=maintenance_menu,underline=0)
menubar.add_cascade(label="Certify", menu=certify_menu,underline=0)
menubar.add_cascade(label="Help", menu=help_menu,underline=0)
log.info('Complete menu setup')

window.mainloop()

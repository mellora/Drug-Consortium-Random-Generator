# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:28:12 2020

@author: MIWWGE
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class main_window():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Drug Consortium")
        self.file_path = tk.StringVar()
        self.create_widgets()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def get_file_path(self):
        self.file_path = os.path.normpath(filedialog.askopenfilename(initialdir="C:/", title="Select File", filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*"))))
        self.entry_file_path.delete(0, len(self.entry_file_path.get()))
        self.entry_file_path.insert(0, self.file_path)


    def create_widgets(self):
        #
        # Master LabelFrame for User Input for pulling
        #
        label_group_master = ttk.LabelFrame(self.win)
        label_group_master.grid(column=0, row=0)

        #
        # LabelFrame for pull config
        #
        label_group_pull_numbers = ttk.LabelFrame(label_group_master, text=" Config ")
        label_group_pull_numbers.grid(column=0, row=0)

        #
        # LabelFrame for file path
        #
        label_group_file_path = ttk.LabelFrame(label_group_pull_numbers, text=" File Path ")
        label_group_file_path.grid(column=0, row=0, columnspan=2)
        # Entry to type in file path
        self.entry_file_path = ttk.Entry(label_group_file_path, width=50, textvariable=self.file_path)
        self.entry_file_path.grid(column=0, row=0)
        # Button to browse to file
        button_browse_to_file = tk.Button(label_group_file_path, text="Browse", command=self.get_file_path)
        button_browse_to_file.grid(column=1, row=0)

        #
        # LabelFrame for Randoms
        #
        label_group_randoms = ttk.LabelFrame(label_group_pull_numbers, text=" Randoms ")
        label_group_randoms.grid(column=0, row=1)
        # Label
        ttk.Label(label_group_randoms, text="Number to pull:").grid(column=0, row=0)
        # Spinbox
        self.spin_random = tk.Spinbox(label_group_randoms, from_=0, to=100)
        self.spin_random.grid(column=1, row=0)

        #
        # LabelFrame for Alternates
        #
        label_group_alternates = ttk.LabelFrame(label_group_pull_numbers, text=" Alternates ")
        label_group_alternates.grid(column=1, row=1)
        # Label
        ttk.Label(label_group_alternates, text="Number to pull:").grid(column=0, row=0)
        # SpinBox
        self.spin_alternate = tk.Spinbox(label_group_alternates, from_=0, to=100)
        self.spin_alternate.grid(column=1, row=0)

    def get_path(self):
        return self.file_path

    def get_num_random(self):
        return self.spin_random.get()

    def get_num_alternate(self):
        return self.spin_alternate.get()

if __name__ == "__main__":
    main = main_window()
    main.win.mainloop()
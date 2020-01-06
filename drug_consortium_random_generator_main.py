# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:59:28 2020

@author: MIWWGE
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import pandas as pd
from datetime import datetime

class DrugConsortiumRandomPuller:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Drug Consortium")
        self.win.resizable(False, False)
        self.file_path = tk.StringVar()
        self.create_widgets()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def get_data_from_file(self):
        self.file_data = pd.read_excel(os.path.normpath(filedialog.askopenfilename(initialdir="C:/", title="Select File", filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))), header=None)
        self.label_pop_size.configure(text=f"There Are {self.file_data.size} Employees in this list")

    def pull_randoms(self):
        num_rand = int(self.spin_random.get())
        num_alt = int(self.spin_alternate.get())
        sampled_pop = self.file_data.sample(num_rand + num_alt)
        pulled_randoms = sampled_pop.iloc[:num_rand][0].values.tolist()
        pulled_alternates = sampled_pop.iloc[num_rand:][0].values.tolist()
        self.label_random.configure(text="Randoms Pulled:\n" + "\n".join(pulled_randoms))
        self.label_alternate.configure(text="Alternates Pulled:\n" + "\n".join(pulled_alternates))
        self.label_timestamp.configure(text="Time List Was Pulled: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def create_widgets(self):
        #
        # Menu Bar
        #
        menu_bar = tk.Menu(self.win)
        self.win.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.get_data_from_file)
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        #
        # Master LabelFrame for User Input for pulling
        #
        label_group_master = ttk.LabelFrame(self.win)
        label_group_master.grid(column=0, row=0, sticky=tk.W)

        #
        # LabelFrame for pull config
        #
        label_group_pull_numbers = ttk.LabelFrame(label_group_master, text=" Config ")
        label_group_pull_numbers.grid(column=0, row=0, sticky=tk.W)

        #
        # LabelFrame for Randoms
        #
        label_group_randoms = ttk.LabelFrame(label_group_pull_numbers, text=" Randoms ")
        label_group_randoms.grid(column=0, row=1, sticky=tk.W)
        # Label
        ttk.Label(label_group_randoms, text="Number to pull:").grid(column=0, row=0)
        # Spinbox
        self.spin_random = tk.Spinbox(label_group_randoms, from_=0, to=100)
        self.spin_random.grid(column=1, row=0)

        #
        # LabelFrame for Alternates
        #
        label_group_alternates = ttk.LabelFrame(label_group_pull_numbers, text=" Alternates ")
        label_group_alternates.grid(column=1, row=1, sticky=tk.W)
        # Label
        ttk.Label(label_group_alternates, text="Number to pull:").grid(column=0, row=0)
        # SpinBox
        self.spin_alternate = tk.Spinbox(label_group_alternates, from_=0, to=100)
        self.spin_alternate.grid(column=1, row=0)

        #
        # LabelFrame for output
        #
        label_group_output = ttk.LabelFrame(label_group_master, text=" Pulled Employees")
        label_group_output.grid(column=0, row=1, sticky=tk.W)
        # Pop Size Label
        self.label_pop_size = ttk.Label(label_group_output, text="")
        self.label_pop_size.grid(column=0, row=0, columnspan=2)
        # Button to pull randoms and alternates
        button_puller = ttk.Button(label_group_output, text="Pull Randoms", command=self.pull_randoms)
        button_puller.grid(column=0, row=1, columnspan=2)
        # Random Pull Output
        self.label_random = ttk.Label(label_group_output, text="Randoms Pulled")
        self.label_random.grid(column=0, row=2)
        # Alternate Pull Output
        self.label_alternate = ttk.Label(label_group_output, text="Alternates Pulled")
        self.label_alternate.grid(column=1, row=2)
        # TImestamp Label
        self.label_timestamp = ttk.Label(label_group_output, text="TIme List Was Pulled:")
        self.label_timestamp.grid(column=0, row=3, columnspan=2)

        #
        # Set Label Padding
        #
        for group in label_group_master.winfo_children():
            group.grid_configure(padx=5, pady=5)
            for child in group.winfo_children():
                child.grid_configure(padx=5, pady=5)

if __name__ == "__main__":
    consortium_main = DrugConsortiumRandomPuller()
    consortium_main.win.mainloop()
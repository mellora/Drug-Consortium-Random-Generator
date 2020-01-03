# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:59:28 2020

@author: MIWWGE
"""

#%%
# import numpy as np
import pandas as pd
import os
# import sys

path_to_dir = os.path.normpath("D:/Spyder/DrugConsortiumData")
os.chdir(path_to_dir)

class random_puller:
    def load_data(self, file_name):
        self.data = pd.read_excel(file_name, header=None)

    def pull_from_data(self, rand_num, alt_num):
        full_list = self.data.sample(rand_num + alt_num)
        self.pulled_randoms = full_list.iloc[:rand_num]
        self.pulled_alternates = full_list.iloc[rand_num:]

    def output_pulled_randoms(self):
        return self.pulled_randoms[0].values.tolist()

    def output_pulled_alternates(self):
        return self.pulled_alternates[0].values.tolist()

random_operations = random_puller()
random_operations.load_data("MOCK_DATA.xlsx")

# Get Input from user for how many to pull with error checking to make sure value
# input can be used in calculations.
def output_error():
    print("Error: not an Integer Value")
    print("Try Again")
while True:
    randoms_to_pull = input("Enter number of randoms to pull: ")
    if randoms_to_pull.isdigit():
        randoms_to_pull = int(randoms_to_pull)
        break
    else:
        output_error()
while True:
    alternates_to_pull = input("Enter number of alternates to pull: ")
    if alternates_to_pull.isdigit():
        alternates_to_pull = int(alternates_to_pull)
        break
    else:
        output_error()

# Pull from data with user specified values.
random_operations.pull_from_data(randoms_to_pull, alternates_to_pull)

pulled_randoms = random_operations.output_pulled_randoms()
pulled_alternates = random_operations.output_pulled_alternates()


# Output to console the results.
def output_to_console(data):
    for x, name in enumerate(data):
        print(x + 1, name)
print()
print("Randoms Pulled")
output_to_console(pulled_randoms)
print()
print("Alternates Pulled")
output_to_console(pulled_alternates)
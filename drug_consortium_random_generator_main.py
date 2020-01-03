# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:59:28 2020

@author: MIWWGE
"""

import os
import random_puller

os.chdir(os.path.normpath("D:/Spyder/DrugConsortiumData"))

if __name__ == "__main__":
    puller = RandomPuller.random_puller()
    puller.load_data(os.path.normpath("D:/Spyder/DrugConsortiumData/MOCK_DATA.xlsx"))

    print("There are", puller.get_population_size(), "entries in the population.")
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
    puller.pull_from_data(randoms_to_pull, alternates_to_pull)

    pulled_time = puller.output_pulled_time()
    pulled_randoms = puller.output_pulled_randoms()
    pulled_alternates = puller.output_pulled_alternates()

    # Output to console the results.
    def output_to_console(data):
        for x, name in enumerate(data):
            print(x + 1, name)
    print()
    print("Randoms Pulled at:", pulled_time)
    print()
    print("Randoms Pulled")
    output_to_console(pulled_randoms)
    print()
    print("Alternates Pulled")
    output_to_console(pulled_alternates)
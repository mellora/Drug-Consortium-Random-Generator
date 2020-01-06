# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 11:38:02 2020

@author: MIWWGE
"""

import pandas as pd
from datetime import datetime

class RandomPuller:
    def load_data(self, file_name):
        self.data = pd.read_excel(file_name, header=None)

    def pull_from_data(self, rand_num, alt_num):
        full_list = self.data.sample(rand_num + alt_num)
        self.pulled_randoms = full_list.iloc[:rand_num]
        self.pulled_alternates = full_list.iloc[rand_num:]

    def get_pulled_randoms(self):
        return self.pulled_randoms[0].values.tolist()

    def get_pulled_alternates(self):
        return self.pulled_alternates[0].values.tolist()

    def get_pulled_time(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_population_size(self):
        return self.data.size

if __name__ == "__main__":
    import os
    os.chdir(os.path.normpath("D:/Spyder/DrugConsortiumData"))
    puller = RandomPuller()
    puller.load_data("MOCK_DATA.xlsx")

    pop_size = puller.get_population_size()
    puller.pull_from_data(5,5)
    time = puller.get_pulled_time()
    randoms = puller.get_pulled_randoms()
    alternates = puller.get_pulled_alternates()

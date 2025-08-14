## this file is to import chemicals into the dry or wet csv datasets 

import pandas as pd
import csv
import os

datadry = pd.read_csv('Chemical Libraries\dry.csv', index_col="DryChemical")
print(datadry.head)


datawet = pd.read_csv('Chemical Libraries\wet.csv', index_col="WetChemical")
#print(datawet.head)


chemical = input("Enter the name of the chemical: ")
chemical = chemical.upper().strip()
weight = float(input("Enter the molecular weight of the chemical: "))
newrow = {'DryChemical': chemical, 'MolecularWeight': weight}
datadry = datadry.append(newrow, ignore_index=True)
datadry.to_csv('Chemical Libraries\dry.csv')

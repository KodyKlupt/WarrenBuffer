

import pandas as pd
import csv

dry = pd.read_csv("dry.csv", index_col="DryChemical")  # this reads the data csv and uses the chemical name as the index for the data to eventually look up the MW
print(dry.head())

wet = pd.read_csv("wet.csv", index_col="WetChemical") #will index and search molarity instead
print(wet)

volumeinput = input("Enter the volume of the solution in L: ") #this is the input for the volume of the solution
volumeinput = int(volumeinput)

drydict = {} #this is the dictionary for the dry chemicals

dryinput = input("Enter the dry chemical name in caps: ") #this is the input for the chemical name
while dryinput != "DONE": #this is the loop that will keep asking for input until the user enters exit
    promptmm = int(input("Enter the conc of the dry chemical in M: ")) #this is the input for the conc of the chemical
    MW = dry.loc[dryinput, "WEIGHT"] #this looks up the MW of the chemical in the data csv
    drymass = promptmm*MW*volumeinput #this calculates the mass of the chemical needed for the buffer
    drydict.update({dryinput: drymass}) #this adds the chemical and its mass to the dictionary
    dryinput = input("Enter the dry chemical name in caps: ") #this is the input for the chemical name
print(drydict, "note the values are all in grams") #this prints the dictionary

volumeinput = input("Enter the volume of the solution in L: ") #this is the input for the volume of the solution
volumeinput = int(volumeinput)

wetdict = {} #this is the dictionary for the dry chemicals

wetinput = input("Enter the wet chemical name in caps: ") #this is the input for the chemical name
while wetinput != "DONE": #this is the loop that will keep asking for input until the user enters exit
    promptmm = int(input("Enter the conc of the chemical in M: ")) #this is the input for the conc of the chemical
    stock = wet.loc[wetinput, "MOLARITY"] #this looks up the MW of the chemical in the data csv
    wetvol = volumeinput*promptmm/stock*1000 #this calculates the mass of the chemical needed for the buffer
    wetdict.update({wetinput: wetvol}) #this adds the chemical and its mass to the dictionary
    wetinput = input("Enter the wet chemical name in caps: ") #this is the input for the chemical name
print(wetdict, "note the values are all in mL") #this prints the dictionary
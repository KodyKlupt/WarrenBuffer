

import pandas as pd
import csv
import os 
import time


dry = pd.read_csv("Chemical Libraries\dry.csv", index_col="DryChemical")  # this reads the data csv and uses the chemical name as the index for the data to eventually look up the MW
wet = pd.read_csv("Chemical Libraries/wet.csv", index_col="WetChemical") #will index and search molarity instead

volumeinput = float(input("Enter the volume of the solution in L: ")) #this is the input for the volume of the solution


drydict = {} #this is the dictionary for the dry chemicals
dryinput = input("Enter the dry chemical name: ") #this is the input for the chemical name
dryinput = dryinput.upper().strip()
while dryinput != "DONE": #this is the loop that will keep asking for input until the user enters exit
    promptmm = float(input("Enter the conc of the dry chemical in M: ")) #this is the input for the conc of the chemical
    MW = dry.loc[dryinput, "WEIGHT"] #this looks up the MW of the chemical in the data csv
    drymass = promptmm*MW*volumeinput #this calculates the mass of the chemical needed for the buffer
    drydict.update({dryinput: drymass}) #this adds the chemical and its mass to the dictionary
    dryinput = input("Enter the dry chemical name, type DONE to exit: ") #this is the input for the chemical name
    dryinput = dryinput.upper().strip()
# print(drydict, "note the values are all in grams") #this prints the dictionary


wetdict = {} #this is the dictionary for the dry chemicals
wet_question = input("Do you need to add wet chemicals? (yes/no): ")
if wet_question == "yes":
    wetinput = input("Enter the wet chemical name, type DONE to exit: ") #this is the input for the chemical name
    wetinput = wetinput.upper().strip()
    while wetinput != "DONE": #this is the loop that will keep asking for input until the user enters exit
        promptmm = float(input("Enter the conc of the chemical in M: ")) #this is the input for the conc of the chemical
        stock = wet.loc[wetinput, "MOLARITY"] #this looks up the MW of the chemical in the data csv
        wetvol = volumeinput*promptmm/stock*1000 #this calculates the mass of the chemical needed for the buffer
        wetdict.update({wetinput: wetvol}) #this adds the chemical and its mass to the dictionary
        wetinput = input("Enter the wet chemical name, type DONE to exit: ") #this is the input for the chemical name
        wetinput = wetinput.upper().strip()
    # print(wetdict, "note the values are all in mL") #this prints the dictionary
else:
    pass

    
dataframedry = pd.DataFrame.from_dict(drydict, orient="index", columns=["Mass (g)"]) #this converts the dictionary to a dataframe
dataframewet = pd.DataFrame.from_dict(wetdict, orient="index", columns=["Volume (mL)"]) #this converts the dictionary to a dataframe

combined = pd.concat([dataframedry, dataframewet], axis=1) #this combines the two dataframes
print("Here is the buffer recipe for", volumeinput, "L of buffer:", "\n", combined) #this prints the combined dataframe

time = time.strftime("%Y%m%d-%H%M%S") #this gets the current date and time
dir = os.chdir("Outputs")
combined.to_csv("logbuffer" + time + ".csv") #this saves the dataframe to a csv file



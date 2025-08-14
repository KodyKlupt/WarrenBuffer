import pandas as pd
import os
import time
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Calculate buffer recipes.')
parser.add_argument('--volume', type=float, required=True, help='Total volume of the solution in L')
parser.add_argument('--dry', nargs=2, action='append', metavar=('NAME', 'CONC_mM'), help='Dry chemical name and concentration in mM. Can be specified multiple times.')
parser.add_argument('--wet', nargs=2, action='append', metavar=('NAME', 'CONC_mM'), help='Wet chemical name and concentration in mM. Can be specified multiple times.')
parser.add_argument('--name', type=str, required=True, help='Name of the buffer solution')
args = parser.parse_args()

# Read chemical libraries
dry_lib = pd.read_csv("Chemical_Libraries/dry_gemini.csv")
wet_lib = pd.read_csv("Chemical_Libraries/wet_gemini.csv")


volumeinput = args.volume

drydict = {}
if args.dry:
    for dry_chem in args.dry:
        name, conc_mM_str = dry_chem
        conc_mM = float(conc_mM_str)
        conc_M = conc_mM / 1000 # convert mM to M

        # Find the row with the matching reagent name (case-insensitive)
        row = dry_lib[dry_lib['Reagent'].str.lower() == name.lower()]

        if not row.empty:
            mw = row.iloc[0]['Molecular Weight (g/mol)']
            drymass = conc_M * mw * volumeinput #mass is reported in grams
            drydict[row.iloc[0]['Reagent']] = drymass
        else:
            print(f"Error: Dry chemical '{name}' not found in the library.")


wetdict = {}
if args.wet:
    for wet_chem in args.wet:
        name, conc_mM_str = wet_chem
        conc_mM = float(conc_mM_str)
        conc_M = conc_mM / 1000 # convert mM to M

        # Find the row with the matching reagent name (case-insensitive)
        row = wet_lib[wet_lib['Reagent'].str.lower() == name.lower()]

        if not row.empty:
            stock = row.iloc[0]['Molarity (mol/L)']
            wetvol = volumeinput * conc_M / stock * 1000 # convert L to mL
            wetdict[row.iloc[0]['Reagent']] = wetvol
        else:
            print(f"Error: Wet chemical '{name}' not found in the library.")


dataframedry = pd.DataFrame.from_dict(drydict, orient="index", columns=["Mass (g)"])
dataframewet = pd.DataFrame.from_dict(wetdict, orient="index", columns=["Volume (mL)"])

if not dataframedry.empty or not dataframewet.empty:
    combined = pd.concat([dataframedry, dataframewet], axis=1)
    print("Here is the buffer recipe for", volumeinput, "L of buffer:", "\n", combined)

    time_str = time.strftime("%Y%m%d-%H%M%S")
    if not os.path.exists("Outputs"):
        os.makedirs("Outputs")
    
    output_path = os.path.join("Outputs", f"{args.name}_{time_str}.csv")
    combined.to_csv(output_path)
    print(f"Recipe saved to {output_path}")
else:
    print("No valid chemicals were specified. Nothing to do.")

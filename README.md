# Buffer Calculator

A simple calculator program that performs buffer calculations.

## Features

- Entry into an imported or new user generated chemical library that can be updated each time a new buffer is created
- Scale buffers to any volume required simply
- Export buffers to a CSV file for easy printing and logging

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/kodyklupt/WarrenBuffer
   ```

## Usage

Run the script from the command line, providing the total volume and the chemicals to add.
The script accepts concentrations in mM.

### Command Structure

```bash
python buffercalculator.py --name test --volume <L> --dry <name> <concentration> --wet <name> <concentration>
```

### Example

To create a 1.5 L buffer with 200 mM Sodium Chloride, 100 mM Tris, and 50 mM HCl, you would run:

```bash
python buffercalculator.py --volume 1.5 --dry "Sodium Chloride" 200 --dry "Tris" 100 --wet "HCl" 50
```

## Chemical Libraries

The `Chemical Libraries` folder contains lists of wet and dry reagents that can be used by the buffer calculator. You can easily add your own chemicals to these lists.

- `dry.csv`: This file contains a list of dry reagents and their corresponding molecular weights in g/mol.
- `wet.csv`: This file contains a list of wet reagents and their corresponding molarities in mol/L.

## Google Gemini Chemical Libraries

Gemini was prompted to generate a list of common chemical reagents and associated molecular weights. These are the loaded default files. Use caution when using these libraries.

## Generating user specific dictionaries

Go to ```/Chemical_Libraries/.gitignore``` and uncomment the dry.csv or wet.csv so your libraries are not written over in future pulls from Git. Alternatively, you can use redirect the library in buffercalculator.py
```bash
dry_lib = pd.read_csv("Chemical_Libraries/dry.csv")
wet_lib = pd.read_csv("Chemical_Libraries/wet.csv")
```

## Outputs

The `Outputs` folder contains the generated buffer recipes in CSV format. Each time you create a new buffer, a CSV file with the recipe will be saved in this folder.
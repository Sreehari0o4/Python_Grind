"""
pizza.py
This program reads a CSV file containing pizza menu data and prints it in a formatted table using the 'tabulate' library.
Usage:
    python pizza.py <filename.csv>
Command-line Arguments:
    <filename.csv> : The path to the CSV file to be read. Must have a '.csv' extension.
Program Description:
    - Checks for correct number of command-line arguments.
    - Validates that the provided file has a '.csv' extension.
    - Reads the CSV file and displays its contents as a table with headers using the 'tabulate' library.
    - Handles errors for missing arguments, too many arguments, incorrect file extension, and file not found.
Exceptions:
    - IndexError: Raised if too few command-line arguments are provided.
    - FileNotFoundError: Raised if the specified file does not exist.
"""

import sys
import csv
from tabulate import tabulate

def main():
    try:
        fname = sys.argv[1]
        if len(sys.argv) != 2:
            sys.exit("Too many command-line arguments")
        if not fname.endswith('.csv'):
            sys.exit("Not a CSV file")
        with open(f"{fname}","r") as file:
            reader = csv.reader(file)
            print(tabulate(reader,headers = "firstrow",tablefmt = "grid"))
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
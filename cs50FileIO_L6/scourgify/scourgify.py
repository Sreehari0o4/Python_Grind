"""
Program Description:
This script reads a CSV file containing student names and houses, where names are in the format "last, first".
It writes a new CSV file with separate columns for first name, last name, and house.
The script expects two command-line arguments: the input filename and the output filename.
It handles errors for missing or extra command-line arguments and missing input files.
"""

import sys
import csv

def main():
    try:
        f1,f2 = sys.argv[1],sys.argv[2]
        if len(sys.argv)>3:
            sys.exit("Too many command-line arguments")

        with open(f"{f1}", "r") as file1, open(f"{f2}","w", newline = '') as file2:
            reader = csv.DictReader(file1)
            writer = csv.DictWriter(file2, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                lname, fname = (row['name'].split(','))
                lname = lname.strip()
                fname = fname.strip()
                house = row['house'].strip()
                writer.writerow({"first":fname, "last":lname, "house":house})

    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit(f"Could not read {f1}")

main()
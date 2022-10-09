"""Helper functions to save CSV data.

This contains a helper function for saving CSV files.

"""
import csv
from pathlib import Path


def save_csv(csvpath,data):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data to the saved CSV file.

    """
    with open(csvpath, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")

        
        # Write/Save the CSV data
        for row in data:
            csvwriter.writerow(row)
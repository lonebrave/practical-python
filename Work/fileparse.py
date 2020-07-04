# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []

        # Use select fields if specified, otherwise use all headers from file
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not row:     # Skip rows with no data
                continue

            # Only use selected fields, if specified
            if indices:
                row = [row[index] for index in indices]

            # Apply type conversion, is specified
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Create dictionary
            record = dict(zip(headers, row))

            records.append(record)

    return records

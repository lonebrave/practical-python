# fileparse.py
#
# Exercise 3.3
import csv
import logging

log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True,
              delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    records = []

    # Read the file headers
    headers = next(rows) if has_headers else []

    # Use select fields if specified, otherwise use all headers from
    # file
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    for line, row in enumerate(rows, start=1):
        if not row:     # Skip rows with no data
            continue

        # Only use selected fields, if specified
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion, if specified
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f"Row {line}: Couldn't convert {row}")
                    log.debug(f'Row {line}: Reason {e}')
                continue

        # Create record
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records

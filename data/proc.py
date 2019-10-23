#!/usr/bin/env python

import csv
from pprint import pprint

rows = []

def cleanup_row(header, row):
    row_dict = dict(zip(header, (x if x is not '' else None for x in row)))

    if row_dict['Phase'] is not None:
        current_phase = row_dict['Phase']
    else:
        row_dict['Phase'] = current_phase

    return row_dict



with open('data.tsv') as tsvfile:
  reader, header = csv.reader(tsvfile, dialect='excel-tab'), None

  current_phase = None

  for row_raw in reader:
    if header is None:
        header = row_raw
    else:
        this_row = cleanup_row(header, row_raw)
        rows.append()
        

pprint(rows)
    


    # if row_dict["Inpatient Admission"] is None:
    #     outpatient['treatments'] = outpatient['treatments'] + [row_dict]

    # pprint(outpatient)
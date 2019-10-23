#!/usr/bin/env python

import csv
from pprint import pprint



def get_data(path):
    data = []
    with open(path) as tsvfile:
        reader, header = csv.reader(tsvfile, dialect='excel-tab'), None
        current_phase = None

        for row_raw in reader:
            if header is None:
                header = row_raw
                continue
            else:
                row_dict = dict(zip(header, (x if x is not '' else None for x in row_raw)))
        
                if row_dict['Phase'] is not None:
                    current_phase = row_dict['Phase']
                else:
                    row_dict['Phase'] = current_phase

            if row_dict['Phase'].startswith('Total'):
                continue

            data.append(row_dict)

    pprint(data)
    return data
            

def clean_data(data):
    main = []

    non_treatment_keys = ['Chemotherapy Infusions', 'Clinic Visit', 'Inpatient Admission']

    group = None

    for row in data:
        
        for key in row: 
            if 


raw_data = get_data('data.tsv')

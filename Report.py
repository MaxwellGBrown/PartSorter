'''A module to decouple the Part, Part Factory, and CSV reading/writing
Will write Part Factories to a file.'''

import Part from Parts.py
import PartFactory from PartFactory.py

def getPartCSV(part):
    '''Returns a CSV string of the part and it's subparts'''
    CSV = '{0:2}, {1:4}, {2:16} \n'.format(part.getLevel(), part.getAssembly(),
                                           part.getPartNumber() )
        for subcomp in part:
            CSV = CSV + subcomp.CSV()
        return CSV

def readCSV(CSV_string):
    '''Reads a CSV_string and returns a factory with the built parts'''
    pass

def writeCSV(part_factory, new_CSV_filename,
             checkFunction=None, filterFunction=None):
    '''Writes a PartFactory into a CSV file.
       checkFunction returns True if an entry is to be included,
       False if not.
       filterFunction returns the CSV output to be written.
       (can return empty string if not to be included?)
       Both do nothing by default.'''
    # make default function for checkFunction
    if checkFunction is None:
        checkFunction = lambda part: True
    # make default function for filterFunction
    if filterFunction is None:
        filterFunction = lambda part: part.CSV()

    output_list = []
    for part in part_factory:
        if checkFunction(part):
            filtered_CSV_string = filterFunction(part)
        if filtered_CSV_string = '':
            continue
        else:
            output_list.append(filtered_part)

    CSV_file = open(new_CSV_filename, 'w')
    for part in output_list:
        CSV_file.write(part.CSV())
    CSV_file.close()


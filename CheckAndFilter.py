'''Functions to be used with Reporter class in outputting CSV files.'''

from Parts import Part

def checkFunction(part):
    '''Returns True if part should be include, False otherwise.'''
    if part.getAssembly() == 'PP':
        return False
    else:
        return True

def filterCache(function):
    '''A decorator to add functionality to my filterFunction with a persistant
dictionary of parts already written and the last part that was written'''
    function.written = {}
    function.last_level = 0
    function.skipping = False
    return function

@filterCache
def filterFunction(part):
    '''Takes a part argument and returns a CSV string for writing'''
    output_CSV_line = ''
    documented = part.getPartNumber() in filterFunction.written.keys()
    next_id = len(filterFunction.written) + 1

    if documented:
        greater = part.getLevel() > filterFunction.last_level
        if filterFunction.skipping and greater:
            output_CSV_line = ''
        else:
            # return the parts ID number
            part_id = 'Part ID {}'.format(filterFunction.written[part.getPartNumber()])
            output_CSV_line = ' ,{},{},{} \n'.format(part.getLevel(),part_id,
                                                     part.getAssembly())
            
            filterFunction.last_level = part.getLevel() # set for subcomps
            filterFunction.skipping = True
    else:
        output_CSV_line = '{},{},{},{}\n'.format(next_id, part.getLevel(),
                                                 part.getPartNumber(),
                                                 part.getAssembly())
        filterFunction.written[part.getPartNumber()] = next_id
        filterFunction.last_level = part.getLevel()
        filterFunction.skipping = False

    return output_CSV_line

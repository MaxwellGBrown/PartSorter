'''A module that allows PartFactory and Parts to interact with files'''

from PartFactory import PartFactory 
class Reporter(object):
    
    def __init__(self):
        '''Director class used to read files and operate PartFactory'''
        self._partFactory = PartFactory()
        self._checkFunction = lambda part: True
        
        from Parts import Part 
        self._filterFunction = lambda part: '{0:2}, {1:4}, {2:16} \n'.format(
                part.getLevel(), part.getAssembly(), part.getPartNumber()  )

    def setFilterFunction(self, filterFunction=None):
        '''Sets the function that writes CSV from Part'''
        if filterFunction is None:
            from Parts import Part 
            self._filterFunction = lambda part:'{0:2}, {1:4}, {2:16} \n'.format(
                part.getLevel(), part.getAssembly(), part.getPartNumber()  )
        else:
            self._filterFunction = filterFunction

    def setCheckFunction(self, checkFunction = None):
        '''Sets the function that determines whether a part is written or not'''
        if checkFunction is None:
            self._checkFunction = lambda part: True
        else:
            self._checkFunction = checkFunction
            
    def buildFromCSV(self, CSV_string):
        '''Reads a CSV_string and returns a factory with the built parts'''
        # split text into lines
        split_CSV_string = CSV_string.split('\n')
        # add all parts into build stack
        for line in split_CSV_string:
            # ERROR CHECKING
            if line == ",,\n" or len(line) < 6:
                continue
            # END ERROR CHECKING
            else:
                # split lines into parts
                split_line = line.split(',')
                # create instance from string
                self._partFactory.addPart(split_line[1], split_line[0],
                                          split_line[2])

        self._partFactory.assembleParts()
                
    def buildFromCSVfile(self, CSV_filename):
        '''Reads a CSV file and returns a populated PartFactory'''
        CSV_file = open(CSV_filename,'r')
        CSV = CSV_file.read()
        CSV_file.close()
        self.buildFromCSV(CSV)

        
    def writeCSV(self):
        '''Turns contents of a PartFactory into a CSV string.
           checkFunction returns True if an entry is to be included, in CSV.
           filterFunction returns the CSV line for a single part.'''

        output_list = []
        for part in self._partFactory:
            if self._checkFunction(part):
                filtered_CSV_line = self._filterFunction(part)
                output_list.append(filtered_CSV_line)
                        
        compiled_CSV_string = ''.join(output_list)
        return compiled_CSV_string

    def writeCSVtoFile(self, new_CSV_filename):
        '''Writes contents of a part factory to a CSV file'''
        CSV_output = self.writeCSV()
        CSV_file = open(new_CSV_filename, 'w')
        CSV_file.write(CSV_output)
        CSV_file.close()


import Parts

class PartFactory(object):
    def __init__(self):
        '''Factory takes CSV from string or file and obstantiates parts'''
        self._parts = []
        
    def __str__(self):
        pass
    
    def __repr__(self):
        string = str()
        for idx in range(len(self._parts)):
            idx_string = '[' + str(idx) + ']'
            string = string + "{0:>8}- {1}\n".format(idx_string,
                                                     self._parts[idx])
        return string
    
    def __len__(self):
        return len(self._parts)
    
    def __getitem__(self, index):
        return self._parts[index]

    def __iter__(self):
        '''Iterates recursively through all parts and subcomps'''
        for part in self._parts:
            yield part
            for sub_comp in part:
                yield sub_comp
    
    def getPart(self, index=int()):
        '''Returns Part object at the given index of Factory._parts'''
        return self._parts[index]
    
    def buildFromString(self, CSV_string):
        '''Builds parts from a Comma Seperated Value string in the format
           "level, assembly, part number \n"'''
        # split text into lines
        split_CSV_string = CSV_string.split('\n')
        build_stack = []
        # add all parts into build stack
        for part in split_CSV_string:
            # ERROR CHECKING
            if part == ",,\n" or len(part) < 6:
                continue
            # END ERROR CHECKING
            else:
                # split lines into parts
                split_part = part.split(',')
                # create instance from string
                new_part = Parts.Part(split_part[1], split_part[0],
                                      split_part[2])
                build_stack.append(new_part)

        # consolidate parts into subcomps of other parts
        finished = False
        while not finished:
            # for every index in build_stack
            old_build_stack_length = len(build_stack)
            # check if a consolidation can be made
            for idx in range(len(build_stack)-1, -1, -1):
                if build_stack[idx].getLevel() > build_stack[idx-1].getLevel():
                    build_stack[idx-1].addSubComp(build_stack.pop(idx))
                    break
            # if no consolidations are made, then it's done!
            if old_build_stack_length == len(build_stack):
                finished = True
                
        # add all parts to the _parts list  
        for part in build_stack:
            self._parts.append(part)
            
    def buildFromFile(self, CSV_filename):
        '''Builds parts from a CSV file in the format of
           "level, assembly, part number\n" '''
        CSV_file = open(CSV_filename, 'r')
        CSV = CSV_file.read()
        CSV_file.close()
        self.buildFromString(CSV)
        
    def writeCSVtoFile(self, new_CSV_filename,
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
        for part in self:
            if checkFunction(part):
                filtered_CSV_line = filterFunction(part)
                if filtered_CSV_line == '':
                    continue
                else:
                    output_list.append(filtered_CSV_line)

        CSV_file = open(new_CSV_filename, 'w')
        for filtered_output_line in output_list:
            CSV_file.write(filtered_output_line)
        CSV_file.close()

                
    def showAllParts(self):
        '''Prints all parts in factory'''
        for part in self._parts:
            # add a break for seperate parts
            if part.getLevel == 1:
                print(' ')
            part.showPart()


class PartFactory(object):
    def __init__(self):
        '''Builds parts & components from tokens. Holds unrelated parts.'''
        self._parts = []
        self._assembly = [] # added parts stored here until self.AssembleParts()
    
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
        '''Iterates recursively through all parts and their subcomps'''
        for part in self._parts:
            yield part
            for sub_comp in part:
                yield sub_comp
    
    def pop(self, index=int()):
        '''Returns & removes Part object at the given index of Factory._parts'''
        return self._parts.pop(index)

    def addPart(self, part_number=str(), level=int(), assembly=str()):
        '''From a token, adds a part to the assembly list to be constructed'''
        from Parts import Part
        new_part = Part(part_number, level, assembly)
        self._assembly.append(new_part)

    def assembleParts(self):
        '''Assembles all parts in the assembly list.
           Adds them to the completed factory'''
        finished = False
        while not finished:
            # for every index in self._assembly
            old_assembly_length = len(self._assembly)
            # check if a consolidation can be made
            for idx in range(len(self._assembly)-1, -1, -1):
                if self._assembly[idx].getLevel() > self._assembly[idx-1].getLevel():
                    self._assembly[idx-1].addSubComp(self._assembly.pop(idx))
                    break
            # if no consolidations are made, then it's done!
            if old_assembly_length == len(self._assembly):
                finished = True
                
        for idx in range(len(self._assembly)-1,-1,-1):
            self._parts.append(self._assembly.pop(idx) )
                
    def showAllParts(self):
        '''Prints all parts in factory. Primary use for error checking'''
        for part in self._parts:
            # add a break for seperate parts
            if part.getLevel == 1:
                print(' ')
            part.showPart()



class Part(object):
    def __init__(self, part_number="A-1-AA", level=int(), assembly=str()):
        '''Create a part number of the format ofPrefix-Base-Suffix-Postfix.
Level indicates where on the part hierarchy the part is.
Assembly determines how the part is produced'''
        self._base = ''    # default
        self._prefix = ''  # default
        self._suffix = ''  # default
        self._postfix = '' # default
        split_part_number = part_number.upper().split('-')
        if len(split_part_number) == 1:
            self._base = split_part_number[0]
        else:
            self._prefix = split_part_number[0]
            self._base = split_part_number[1]
        if len(split_part_number)  > 2:
            self._suffix = split_part_number[2]
        if len(split_part_number) > 3:
            self._postfix = split_part_number[3]
        self._level = level
        self._assembly = assembly.upper()
        self._parent = None
        self._subcomponents = list()
        
    def __repr__(self):
        partnumber = self.getPartNumber()
        output = "{0:<2} {1:<4} {2:<16}".format(self._level, self._assembly,
                                           partnumber)
        return output
    
    def __str__(self):
        partnumber = self.getPartNumber()
        return "{0:<2} {1:<4} {2:<16}".format(self._level, self._assembly,
                                           partnumber)

    def __eq__(self, other):
        '''Will only return true if part and all subcomponents are the same'''
        if self.getPartNumber() != other.getPartNumber():
            return False
        if len(self) == len(other):
            # compare subcomps
            for idx in range(len(self)):
                if self[idx] != other[idx]:
                    return False
        else:
            return False
        return True

    def __len__(self):
        return len(self._subcomponents)

    def __contains__(self, part):
        for sub_comp in self._subcomponents:
            if part == sub_comp:
                return True
        return False

    def __getitem__(self,index):
        return self._subcomponents[index]

    def __iter__(self):
        '''Builds a generator that recursively iterates through all sub comps'''
        for sub_comp in self._subcomponents:
            yield sub_comp
            for sub_sub_comp in sub_comp:
                yield sub_sub_comp
    
    def setPartNumber(self, new_part_number='A-1-AA'):
        '''Takes a string argument in the format of: prefix-base-suffix-postfix
 (only postfix if given) and changes the prefix, base, suffix, and postfix'''
        split_part_number = new_part_number.split('-')
        self._prefix = split_part_number[0]
        self._base = split_part_number[1]
        self._suffix = split_part_number[2]
        if len(split_part_number) > 3:
            self._postfix = split_part_number[3]
        else:
            self._postfix = ''
            
    def getPartNumber(self):
        '''Returns string containing prefix-base-suffix-postfix that represents
the part'''
        partnumber = "{}-{}-{}".format(self._prefix, self._base, self._suffix)
        if self._postfix:
            partnumber = partnumber + '-{}'.format(self._postfix)
        return partnumber

    def getBase(self):
        '''Returns the part numbers base'''
        return self._base

    def getPrefix(self):
        '''Returns the part numbers prefix'''
        return self._prefix

    def getSuffix(self):
        '''Returns the part numbers suffix'''
        return self._suffix

    def getPostfix(self):
        '''Returns the part numbers postfix'''
        return self._postfix
        
    def setLevel(self, new_level):
        '''Changes instances level'''
        self._level = new_level
        
    def getLevel(self):
        '''Returns integer level of part'''
        return self._level
    
    def setAssembly(self, new_assembly):
        '''Changes instances assembly'''
        self._assembly = new_assembly
        
    def getAssembly(self):
        '''Returns string assembly of part'''
        return self._assembly
    
    def addSubComp(self, new_subcomp):
        '''Adds a Part type object to the subcomponents list. Changes subcomp
parent'''
        self._subcomponents.append(new_subcomp)
        new_subcomp.changeParent(self)

    def changeParent(self, new_parent):
        '''Changest the parent part of which self is a sub component'''
        self._parent = new_parent

    def getParent(self):
        '''Returns parent part. Returns None if no parent exists'''
        return self._parent
    
    def showPart(self):
        '''Prints the part and it's subcomponents'''
        print(self)
        for subcomp in self._subcomponents:
            subcomp.showPart()
            
        
            

    
        
            
    
    

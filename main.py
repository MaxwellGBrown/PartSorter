
from PartFactory import PartFactory
from Parts import Part
from CheckAndFilter import *

F = PartFactory()
F.buildFromFile('SampleData.csv')
F.writeCSVtoFile('SampleOutput.csv',checkFunction=checkFunction,
                 filterFunction = filterFunction)




from Report import Reporter
from CheckAndFilter import *

R = Reporter()
R.setCheckFunction(checkFunction)
R.setFilterFunction(filterFunction)
R.buildFromCSVfile('SampleData.csv')
R.writeCSVtoFile('SampleOutput.csv')



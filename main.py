'''Opens a dialogue to allow interfacing with opening and saving a CSV file
from a reporter object.'''

def main():
    from Report import Reporter
    from CheckAndFilter import *
    from Tkinter import Tk
    from tkFileDialog import askopenfilename, asksaveasfilename

    R = Reporter()
    R.setCheckFunction(checkFunction)
    R.setFilterFunction(filterFunction)

    Tk().withdraw()
    filename = askopenfilename()
    R.buildFromCSVfile(filename)

    new_filename = asksaveasfilename()
    R.writeCSVtoFile(''.join(new_filename))

if __name__ == "__main__":
    main()

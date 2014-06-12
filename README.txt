README
======

This file was made to ease the pain of sifting through the assembly charts of 6k+ parts
to find the ones we were interested in using. v0.1 was a very simplified version of this
group of scripts, but in the case of future need/bigger files it would be more efficient
to have a better planned/scripted way to handle reporting those figures.

CSV Files should come in the form of: "Level, Assembly, Part Number\n", and are reported
in the same format


File Contents
================

Parts.py
---------
Represent the instance of a part number, level, assembly, and subparts of that part. 
Modeled with the composite pattern.

PartFactory.py 
--------------
Responsible for the compiling of lists of parts into part hierarchies.
Modeled with the factory pattern.

Main.py
---------
Executes the other pieces of the package, including reading a file, building the parts 
through the partfactory, and writing to a new CSV file.

CheckAndFilter.py
-----------------
Contains checkFunction(part) and filterFunction(part) which can both be used to override
the standard functions in PartFactory.writeCSVtoFile. They're used to give more complexity
in the CSV reporting for parts.

CheckAndFilter.EMPTY.py
-----------------------
Offers my empty template for people/me to use, so you don't have to change the main file.
Just resave as CheckAndFilter.py to replace the current one.


Future development:
===============

1. Decouple writing files from PartFactory
__________________________________________

Report.py
---------
A file that will decouple Parts.py and PartFactory.py away from the CSV format. This isn't
imperative because both Parts and PartFactory operate very well even with the CSV modules
they have, but decoupling them can allow for deviation from the CSV file format.


2. Make PartFactory a pure factory pattern
__________________________________________

At the moment, Part Factory isn't a pure factory pattern; the way PartFactory builds is
done by compiling one large list instead of being commanded by a higher-up function.

To do this, reading files and populating the factory has to be decoupled from the 
PartFactory object. To do this, a module for "addpart" and "construct parts" should be 
added so that as the high-level function gets the parts it adds them into an "unconstructed
stack" and then when necessary runs the "construct parts" function to consolidate 
subcomponents. 

Doing this will allow for different algorithms for reading different kinds of files to be
implemented. The CSV modules for PartFactory don't hurt it's functionality, so it's not
absolutely necessary in the case that PartFactory is used as a module in something else,
but it would make me happy.


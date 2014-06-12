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

Report.py
---------
Provides a director interface for PartFactory() so that PartFactory can be built with 
CSV files and write to CSV files.

Main.py
---------
Operates the Reporter from Report.py so that the SampleData.csv is read and writes to
SampleOutput.csv.

Uses a very simple Tkinter command to open a "File open" dialogue.

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

1. Clean up PartFactory.py
___________________________

PartFactory() currently exists as an object that holds the pieces that it's assembled.
This doesn't cater to my ideal outfitting of FactoryPattern which should just be used to
"assemble" parts and subcomps into one low-level part. 

Whether or not the current implementation is a direction that is suitable for future 
developments remains to be seen, but the current implementation is still suspect.

2. Add real Error Checking in reading CSV
_________________________________________

Current implementation has only checks for short or nonexistant line entries. Implementing
a module for error checking would make current and future error checking much easier and
more customizable.

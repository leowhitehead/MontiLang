# MontiLang
Imperative stack-based programming language developed in python.

# About
Monti is a stack-based language revolving around imperative commands to manipulate the stack. The syntax of the language is quite similar to the [FORTH](https://en.wikipedia.org/wiki/Forth_(programming_language)) programming language in it's syntax.

# Current State
Some of the features that are currently implemented are as follows:

* Integer, float and string data types
* Common operators (`+`, `-`, `*`, `%`, `/`, etc.)
* Multi line comments
* Nested loops and statements (`FOR`, `WHILE`, `IF`)
* Stack manipulation commands (`SWAP`, `ROT`, `NIP`, `POP`, `DUP`)
* User input
* Integer and string manipulation

The following will be coming soon:

* Control flow statements (`ELSE`, `ELSEIF`)
* User defined functions
* Equality and inequality operators (`==`, `>`, `<`, `&&`, `||` etc.)

# Installation

The easiest way to compile and use Monti is through the python package 'Pyinstaller'

Install Pyinstaller from PyPI:

    Python -m pip install pyinstaller

Navigate to /src directory and run

    pyinstaller main.py -n monti

(Note: Monti can be converted to a standalone executable with the -F flag, however this is not reccomended as it creates a noticeable drop in performance.)

Add `/dist/monti` to system path, so it can be called from anywhere.

# Usage:
To interperate a Monti file, use 

    monti file.mt
Or to run the interactive REPL, just use

    monti


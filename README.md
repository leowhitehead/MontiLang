# MontiLang
Imperative stack-based programming language developed in python.

# About
Monti is a stack-based language revolving around imperative commands to manipulate the stack. The syntax of the language is quite similar to the [FORTH](https://en.wikipedia.org/wiki/Forth_(programming_language)) programming language in its syntax.

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

    monti [file]
If no file is specified, Monti will launch into an interactive REPL

# Example

Example program that takes an input as a number, and prints that far into the fibonacci sequence.

        /# Test fibonacci program #/
        |Enter length of sequence: | INPUT NIP VAR loop .

        0 VAR a .
        1 VAR b .

        FOR loop
            a b + VAR c .
            a PRINT .
            b VAR a .
            c VAR b .
        ENDFOR
        
See the `Documentation.mt` file in `/examples` for a more detailed explination of language features.

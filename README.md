# MontiLang
An imperative stack-based programming language developed in python.

# About
Monti is a stack-based language revolving around imperative commands to manipulate the stack. 

# Current State
Some of the features that are currently implemented are as follows:

* Integer, float and string data types
* Common operators (`+`, `-`, `*`, `%`, `/`, etc.)
* Multi line comments
* Nested loops and statements (`FOR`, `WHILE`, `IF`)
* Stack manipulation commands (`SWAP`, `ROT`, `NIP`, `POP`, `DUP`)
* Equality, inequality and other operators (`==`, `>`, `<=`, etc.)
* User input
* Integer and string manipulation
* User defined commands
* And/Or/Not statements

The following will be coming soon:

* Additional data types
* String and Array iteration

# Installation

The easiest way to compile and use Monti is through the python package 'Pyinstaller'

Install Pyinstaller from PyPi and download the MontiLang source code

    git clone https://github.com/lduck11007/MontiLang.git
    cd MontiLang/src
    pyinstaller main.py -n monti
**On windows:**  

install [mysysgit](https://gitforwindows.org/), run steps above the same.
Add `\MontiLang\src\dist\monti` to system path

    SETX /M path "%path%;C:\[path_to_directory]\MontiLang\src\dist\monti"

**On Linux:** 

PyInstaller requires the `ldd` terminal application to discover the shared libraries required by each program or shared library. It is typically found in the distribution-package `glibc` or `libc-bin`. Ensure that Pyinstaller is installed and fully working.

(Note: Monti can be converted to a standalone executable with the -F flag, however this is not recommended as it creates a noticeable drop in performance.)

# Usage:
To interpret a Monti file, use 

    monti [file]
If no file is specified, Monti will launch into an interactive REPL

# Examples

Example program that takes an input as a number, and prints that far into the Fibonacci sequence.

        /# Test Fibonacci program #/
        |Enter length of sequence: | INPUT NIP VAR loop .

        0 VAR a .
        1 VAR b .

        FOR loop
            a b + VAR c .
            a PRINT .
            b VAR a .
            c VAR b .
        ENDFOR

FizzBuzz: Program that loops through numbers 1-100, prints 'fizz' if it is a multiple of 3, 'buzz' if a multiple of 5, and 'fizzbuzz' if both.

        100 VAR loop .
        1 VAR i .

        FOR loop
            || VAR ln .
            i 5 % 0 == 
            IF : .
                ln |Buzz| + VAR ln .
            ENDIF
            i 3 % 0 ==
            IF : .
                ln |Fizz| + VAR ln .
            ENDIF
            ln || ==
            IF : .
                i PRINT .
            ENDIF
            ln || !=
            IF : .
                ln PRINT .
            ENDIF
        i 1 + VAR i .
        ENDFOR
See the `Documentation.mt` file in `/examples` for a more detailed explanation of language features.

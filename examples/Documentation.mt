/# Monti Reference sheet #/

/#
Comments are multiline
Nested comments are not supported 
#/

/# All programming in Monti is done by manipulating the parameter stack #/

/# in Monti, everything is either a string or a number. Operations treat all numbers
similarly to floats, but anything without a remainder is treated as type int #/

/# numbers and strings are added to the stack from left to right #/

/# Arithmetic works by manipulating data on the stack #/

5 3 + PRINT . /# 8 #/

/#  5 and 3 are pushed onto the stack
    '+' replaces top 2 items on stack with sum of top 2 items
    'PRINT' prints out the top item on the stack
    '.' pops the top item from the stack. 
    #/

/# More arithmetic: #/

6 7 * PRINT . /# 42 #/
1360 23 - PRINT . /# 1337 #/
12 12 / PRINT . /# 1 #/
13 2 MOD PRINT . /# 1 #/

37 NEG PRINT . /# -37 #/
-12 ABS PRINT . /# 12 #/
52 23 MAX PRINT . /# 52 #/
52 23 MIN PRINT . /# 23 #/

/# There is also a wide range of commands for stack manipulation #/
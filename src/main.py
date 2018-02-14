import sys
import re
import os
import errors
import dep

def lex(instructions):
    for index, i in enumerate(instructions):
        if i == "VAR":
            instructions[index] = ['VAR', instructions[index+1]]
            del instructions[index+1:index+2]
    interp(instructions)

def interp(command):
    if type(command) == str:
        if command in dep.reserved:
            if command == "PRINT":
                PRINT()
            elif command == "PSTACK":
                PSTACK()
            elif command == "PLUS":
                PLUS()
            elif command == "MINUS":
                MINUS()
            elif command == "POP":
                POP()
            elif command == "MULT":
                MULT()
            elif command == "MOD":
                MOD()
            elif command == "NEG":
                NEG()
            elif command == "ABS":
                ABS()
            elif command == "CLEAR":
                CLEAR()
            elif command == "DIV":
                DIV()
            elif command == "INPUT":
                INPUT()
            elif command == "SWAP":
                SWAP()
            elif command == "ROT":
                ROT()
            elif command == "OUT":
                OUT()
            elif command == "MAX":
                MAX()
            elif command == "MIN":
                MIN()
            elif command == "DUP":
                DUP()
            elif command == 'NIP':
                NIP()
            elif command == 'QUIT':
                os._exit(1)
            elif command == 'EXIT':
                os._exit(1)
            elif command == 'HELP':
                dep.HELP()
            elif command == 'LICENSE':
                dep.LICENSE()
        elif command in gVars:
            stack.append(gVars[command])
        elif command[-1] == '|' and command[0] == '|':
            stack.append(command[1:-1])
        else:
            errors.invalidCommand(command)
    elif type(command) == list:
        if command[0] == 'VAR':
            VAR(*command)
        elif command[0] == 'FOR':
            FOR(command[1:-1])
        elif command[0] == 'WHILE':
            WHILE(command[1:-1])
        elif command[0] == 'IF':
            IF(command[1:-1])
        else:
            command = dep.sublists(command)
            for i in command:
                interp(i) #recursion op
    elif type(command) in [int, float]:
        stack.append(command)

def main():
    global stack
    global gVars
    stack = []
    gVars = dep.globalVs
    if len(sys.argv) == 1:
        repl()
    elif sys.argv[1].upper() == '-V':
        print "Monti v{}".format(dep.globalVs["_VERSION"])
        sys.exit()
    file = open(sys.argv[1], 'r')
    instructions = file.read().replace('\n', ' ')
    instructions = dep.parse(instructions)
    lex(instructions)

def repl(first = True):
    if first:
        print "Monti {} on {}".format(dep.globalVs['_VERSION'], dep.globalVs['_PLATFORM'])
        print "Type 'Help' or 'License' for more information, or type 'QUIT' to quit"
    while True:
        try:
            line = raw_input('>>> ')
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        line = dep.parse(line)
        try:
            lex(line)
        except:
            repl(False)

def PRINT():
    """Print item on top of stack"""
    if len(stack) < 1:
        print "None"
    else:
        print stack[-1]

def PSTACK():
    """print entire stack"""
    print stack
    
def PLUS():
    """Add top 2 items of stack"""
    global stack
    if len(stack) < 2:
            errors.stackArgumentLenError("PLUS")
    else:
        try:
            temp = stack[-1] + stack[-2]
        except TypeError:
            errors.opError()
        stack = stack[:-2]
        stack.append(temp)

def MINUS():
    """Subtract top 2 items of stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MINUS")
    else:
        temp = stack[-2] - stack[-1]
        stack = stack[:-2]
        stack.append(temp)

def MULT():
    """Multiply top 2 items of stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MULTIPLY")
    else:
        temp = stack[-2] * stack[-1]
        stack = stack[:-2]
        stack.append(temp)

def DIV():
    """Divide top 2 items of stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("DIVIDE")
    else:
        temp = float(stack[-2]) / float(stack[-1])
        stack = stack[:-2]
        if str(temp)[-2:] == '.0':
            stack.append(int(temp))
        else:
            stack.append(temp)

def POP():
    """Remove top item from stack"""
    global stack
    stack.pop()

def ROT():
    global stack
    if len(stack) < 3:
        errors.stackArgumentLenError("ROT")
    else:
        temp = stack[-3]
        del stack[-3]
        stack.append(temp)

def MOD():
    """Perform modulus of top 2 items of stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MOD")
    else:
        temp = stack[-2] % stack[-1]
        stack = stack[:-2]
        stack.append(temp)

def NEG():
    """negate top item of stack"""
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("NEGATE")
    else:
        stack[-1] = -stack[-1]

def ABS():
    """get absolute value of top item on stack"""
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("ABS")
    else:
        stack[-1] = abs(stack[-1])

def MAX():
    """replaces top item of stack with largest of top 2"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MAX")
    else:
        stack = stack[:-2] + [max(stack[-2:])]

def MIN():
    """replaces top item of stack with smallest of the top 2"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MIN")
    else:
        stack = stack[:-2] + [min(stack[-2:])]

def DUP():
    """duplicates top item on stack"""
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("DUP")
    else:
        stack.append(stack[-1])

def NIP():
    """deletes 2nd top item from stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("NIP")
    else:
        del stack[-2]

def CLEAR():
    """Wipe stack"""
    global stack
    stack = []

def VAR(call, name):
    """declares a new variable"""
    global stack
    if name in dep.reserved:
        errors.reserved()
    gVars[name] = stack[-1]

def INPUT():
    """puts user input on top of stack"""
    global stack
    if len(stack) > 0:
        if type(stack[-1]) == str:
            prompt = stack[-1]
        else:
            prompt = ''
    else:
        prompt = ''
    ln = dep.tryconvert(raw_input(prompt), True)
    stack.append(ln)

def FOR(inst):
    try:
        if inst[1] == 'PASS':
            return
    except IndexError:
        errors.valueError()
    if type(inst[0]) == int:
        for i in range(inst[0]):
            interp(inst[1:])
    elif type(gVars[inst[0]]) != int:
        errors.valueError()
    else:
        for i in range(gVars[inst[0]]):
            interp(inst[1:])

def WHILE(inst):
    try:
        if inst[1] == 'PASS':
            return
    except IndexError:
        errors.valueError()
    if type(inst[0]) in [int, float]:
        if inst[0] > 0:
            while True:
                interp(inst[1:])
        else:
            return
    elif type(inst[0]) == str and inst[0] not in gVars:
        if len(inst[0]) > 0:
            while True:
                interp(inst[1:])
        else:
            return
    elif inst[0] in gVars:
        if type(gVars[inst[0]]) == str:
            while len(gVars[inst[0]]) > 0:
                interp(inst[1:])
        elif type(gVars[inst[0]]) in [int, float]:
            while gVars[inst[0]] > 0:
                interp(inst[1:])
    else:
        errors.syntaxError()

def IF(inst):
    try:
        if inst[0] == 'PASS':
            return
    except IndexError:
        errors.valueError()
    if type(inst[0]) in [int, float]:
        if inst[0] > 0:
            interp(inst[1:]) 
        else:
            return
    elif type(inst[0]) == str and inst[0] not in gVars:
        if len(inst[0]) > 0:
            interp(inst[1:])
        else:
            return
    elif inst[0] in gVars:
        if type(gVars[inst[0]]) == str:
            if len(gVars[inst[0]]) > 0:
                interp(inst[1:])
        elif type(gVars[inst[0]]) in [int, float]:
            if gVars[inst[0]] > 0:
                interp(inst[1:])
            else:
                return
        else:
            errors.valueError()
    
def SWAP():
    global stack
    stack = stack[:-2] + stack[-2:][::-1]

def OUT():
    if len(stack) < 1:
        sys.stdout.write("None")
        sys.stdout.flush()
    else:
        sys.stdout.write(stack[-1])
        sys.stdout.flush()
if __name__ == "__main__":
    main()

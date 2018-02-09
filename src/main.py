import sys
import re
import errors
import dep

def lex(instructions):
    for index, i in enumerate(instructions):
        if i == "VAR":
            instructions[index] = ['VAR', instructions[index+1]]
            del instructions[index+1:index+2]
    instructions = dep.getLoops(instructions)
    for i in instructions:
        interp(i)

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
            elif command == "MULTIPLY":
                MULTIPLY()
            elif command == "MOD":
                MOD()
            elif command == "NEG":
                NEG()
            elif command == "ABS":
                ABS()
            elif command == "CLEAR":
                CLEAR()
            elif command == "DIVIDE":
                DIVIDE()
            elif command == "INPUT":
                INPUT()
            elif command == "ROT":
                ROT()
            elif command == "OUT":
                OUT()
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
        else:
            for i in command:
                interp(i) #recursion op
    elif type(command) in [int, float]:
        stack.append(command)


def main():
    global stack
    global gVars
    stack = []
    gVars = {'TRUE':1, 'FALSE':0}
    rep = dep.replace
    try:
        file = open(sys.argv[1], 'r')
    except IndexError:
        errors.noFile()
    instructions = file.read().replace('\n', ' ')
    instructions = re.sub(' +', ' ', instructions)
    instructions = re.sub('/#[ a-zA-Z0-9!@$%^&*()\'\",|.-_=+]*#/', '', instructions)
    instructions = dep.getArgs(instructions)
    for index, item in enumerate(instructions):
        for i in rep:
            if item == i[0]:
                instructions[index] = i[1]

    instructions = [dep.tryconvert(i) for i in instructions if i != '']
    lex(instructions)



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

def MULTIPLY():
    """Multiply top 2 items of stack"""
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("MULTIPLY")
    else:
        temp = stack[-2] * stack[-1]
        stack = stack[:-2]
        stack.append(temp)

def DIVIDE():
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

def CLEAR():
    """Wipe stack"""
    global stack
    stack = []

def VAR(call, name):
    global stack
    if name in dep.reserved:
        errors.syntaxError()
    gVars[name] = stack[-1]

def INPUT():
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
    print inst
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
    if type(inst[0]) == int:
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
    elif type(gVars[inst[0]]) == str:
        while len(gVars[inst0]) > 0:
            interp(inst[1:])
    elif type(gVars[inst[0]]) == int:
        while gVars[inst[0]] > 0:
            interp(inst[1:])

    
def ROT():
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

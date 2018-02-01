import sys
import re
from shlex import split as _split
import errors
import dep


def interp(instructions):
    for index, i in enumerate(instructions):
        if type(i) in [int, float]:
            stack.append(i)
        elif i in dep.reserved:
            if i == "PRINT":
                PRINT()
            elif i == "PSTACK":
                PSTACK()
            elif i == "PLUS":
                PLUS()
            elif i == "MINUS":
                MINUS()
            elif i == "POP":
                POP()
            elif i == "MULTIPLY":
                MULTIPLY()
            elif i == "MOD":
                MOD()
            elif i == "NEG":
                NEG()
            elif i == "ABS":
                ABS()
            elif i == "DIVIDE":
                DIVIDE()
            elif i == "VAR":
                instructions[index] = ['VAR', instructions[index+1]]
                del instructions[index+1:index+2]
                VAR(*instructions[index])
        elif type(i) == str:
            if i in gVars:
                stack.append(gVars[i])
            else:
                stack.append(i)
        

def main():
    global stack
    global gVars
    stack = []
    gVars = {}
    rep = dep.rep
    try:
        file = open(sys.argv[1], 'r')
    except IndexError:
        errors.noFile()
    instructions = file.read().replace('\n', ' ')
    instructions = re.sub(' +', ' ', instructions)
    instructions = re.sub('/#[ a-zA-Z0-9]*#/', '', instructions)
    instructions = _split(instructions)
    for index, item in enumerate(instructions):
        for i in rep:
            if item == i[0]:
                instructions[index] = i[1]

    instructions = [dep.tryconvert(i) for i in instructions if i != '']
    interp(instructions)



def PRINT():
    """Print item on top of stack"""
    if len(stack) < 1:
        errors.stackArgumentLenError('PRINT')
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

        

def VAR(call, name):
    global stack
    if name in dep.reserved:
        errors.syntaxError()
    gVars[name] = stack[-1]
    


if __name__ == "__main__":
    main()

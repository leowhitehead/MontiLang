import sys
import re
import os
import errors
import dep

def main():
    global stack
    global gVars
    global defs
    stack = []
    gVars = dep.globalVs
    defs = dep.defs
    if len(sys.argv) == 1:
        repl()
    elif sys.argv[1].upper() == '-V':
        print "Monti v{}".format(dep.globalVs["_VERSION"])
        sys.exit()
    try:
        file = open(sys.argv[1], 'r')
    except IOError:
        print "Invalid file"
        sys.exit()
    instructions = file.read().replace('\n', ' ')
    instructions = dep.parse(instructions, "-c" in ' '.join(sys.argv).lower())
    lex(instructions)

def lex(instructions, inter=True):
    for index, i in enumerate(instructions):
        if i == "VAR":
            instructions[index] = ['VAR', instructions[index+1]]
            del instructions[index+1:index+2]
        elif i == "INSERT":
            instructions[index] = ['INSERT', instructions[index+1]]
            del instructions[index+1:index+2]
        elif i == 'DEL':
            instructions[index] = ['DEL', instructions[index+1]]
            del instructions[index+1:index+2]
        elif i == 'GET':
            instructions[index] = ['GET', instructions[index+1]]
            del instructions[index+1:index+2]
    instructions = dep.getLoops(instructions)
    if inter:
        interp(instructions)

def interp(command):
    if type(command) == str:
        if command in dep.calls:
            globals()[command]()
        elif command in gVars:
            stack.append(gVars[command])
        elif command[-1] == '|' and command[0] == '|':
            stack.append(command[1:-1])
        elif command in defs:
            interp(defs[command])
        else:
            errors.invalidCommand(command)
    elif type(command) == list:
        try:
            if command[0] == 'VAR':
                VAR(*command)
            elif command[0] == 'FOR':
                FOR(command[1:-1])
            elif command[0] == 'WHILE':
                WHILE(command[1:-1])
            elif command[0] == 'IF':
                IF(command[1:-1])
            elif command[0] == 'DEF':
                DEF(command[1:-1])
            elif command[0] == "INSERT":
                INSERT(command[1])
            elif command[0] == "DEL":
                DEL(command[1])
            elif command[0] == "GET":
                GET(command[1])
            else:
                for i in command:
                    interp(i) #recursion op
        except IndexError:
            sys.exit()
    elif type(command) in [int, float]:
        stack.append(command)

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

def DROP():
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("DROP")
    else:
        if type(stack[-1]) != list:
            errors.valueError()
        else:
            if len(stack[-1]) < 1:
                errors.indexError("DROP from empty list")
            else:
                del stack[-1][-1]
def APPEND():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("APPEND")
    else:
        if type(stack[-2]) != list:
            errors.valueError()
        else:
            stack[-2].append(stack[-1])

def INDEX():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError("INDEX")
    else:
        if type(stack[-2]) != list or type(stack[-1]) != int:
            errors.valueError()
        else:
            try:            
                stack.append(stack[-2][stack[-1]])
            except:
                errors.indexError("Array index out of range")

def WIPE():
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("WIPE")
    else:
        if type(stack[-1]) != list:
            errors.valueError()
        else:
            del stack[-1][:]

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

def STKLEN():
    global stack
    stack.append(len(stack))

def CLEAR():
    """Wipe stack"""
    global stack
    stack = []

def VAR(call, name):
    """declares a new variable"""
    global stack
    if name in dep.reserved or name in dep.calls:
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
    if inst[0] == 'TOP':
        arg = stack[-1]
    else:
        arg = inst[0]
    try:
        if inst[1] == 'PASS':
            return
    except IndexError:
        errors.valueError()
    if type(arg) == int:
        for i in range(arg):
            interp(inst[1:])
    elif type(gVars[arg]) != int:
        errors.valueError()
    else:
        for i in range(gVars[arg]):
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
    if inst[0] == "TOP":
        arg = stack[-1]
    else:
        arg = inst[0]
    try:
        if inst[1] == 'PASS':
            return
    except IndexError:
        errors.valueError()
    if type(arg) in [int, float]:
        if arg > 0:
            interp(inst[1:]) 
        else:
            return
    elif type(arg) == str and inst[0] not in gVars:
        if len(arg) > 0:
            interp(inst[1:])
        else:
            return
    elif arg in gVars:
        if type(gVars[arg]) == str:
            if len(gVars[arg]) > 0:
                interp(inst[1:])
        elif type(gVars[arg]) in [int, float]:
            if gVars[arg] > 0:
                interp(inst[1:])
            else:
                return
        else:
            errors.valueError()

def ARR():
    global stack
    temp = [x for x in stack]
    stack = []
    stack.append(temp)

def SWAP():
    global stack
    stack = stack[:-2] + stack[-2:][::-1]

def TRIM():
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("TRIM")
    else:
        del stack[0]

def LESSTHAN():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('LESSTHAN')
    else:
        if stack[-2] < stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def LESSTHANEQ():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('LESSTHANEQ')
    else:
        if stack[-2] <= stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def MORETHAN():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('MORETHAN')
    else:
        if stack[-2] > stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def MORETHANEQ():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('MORETHANEQ')
    else:
        if stack[-2] >= stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def EQUALS():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('EQUALS')
    else:
        if stack[-2] == stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def NOTEQUALS():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('EQUALS')
    else:
        if stack[-2] != stack[-1]:
            del stack[-2:]
            stack.append(1)
        else:
            del stack[-2:]
            stack.append(0)

def AND():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('AND')
    else:
        if type(stack[-1]) == type(stack[-2]) == int or type(stack[-1]) == type(stack[-2]) == float:
            if stack[-1] > 0 and stack[-2] > 0:
                del stack[-2:]
                stack.append(1)
            else:
                del stack[-2:]
                stack.append(0)
        elif type(stack[-1]) == type(stack[-2]) == str:
            if len(stack[-1]) > 0 and len(stack[-2]) > 0:
                del stack[-2:]
                stack.append(1)
            else:
                del stack[-2:]
                stack.append(0)
        else:
            errors.valueError()

def OR():
    global stack
    if len(stack) < 2:
        errors.stackArgumentLenError('OR')
    else:
        if type(stack[-1]) == type(stack[-2]) == int or type(stack[-1]) == type(stack[-2]) == float:
            if stack[-1] > 0 or stack[-2] > 0:
                del stack[-2:]
                stack.append(1)
            else:
                del stack[-2:]
                stack.append(0)
        elif type(stack[-1]) == type(stack[-2]) == str:
            if len(stack[-1]) > 0 or len(stack[-2]) > 0:
                del stack[-2:]
                stack.append(1)
            else:
                del stack[-2:]
                stack.append(0)
        else:
            errors.valueError()

def NOT():
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError('NOT')
    else:
        if type(stack[-1]) == str:
            if len(stack[-1]) > 0:
                del stack[-1]
                stack.append(0)
            else:
                del stack[-1]
                stack.append(1)
        elif type(stack[-1]) in [int, float]:
            if stack[-1] > 0:
                del stack[-1]
                stack.append(0)
            else:
                del stack[-1]
                stack.append(1)

def LEN():
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("LEN")
    else:
        if type(stack[-1]) in [str, list]:
            stack.append(len(stack[-1]))
        else:
            errors.valueError()

def OUT():
    if len(stack) < 1:
        sys.stdout.write("None")
        sys.stdout.flush()
    else:
        sys.stdout.write(stack[-1])
        sys.stdout.flush()

def INSERT(index):
    global stack 
    if len(stack) < 2:
        errors.stackArgumentLenError("INSERT")
    else:
        if type(stack[-2]) != list:
            errors.valueError()
        else:
            try:
                stack[-2][index] = stack[-1]
            except IndexError:
                errors.indexError("Array index out of range")

def DEL(index):
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("DEL")
    else:
        if type(stack[-1]) != list:
            errors.valueError()
        else:
            try:
                del stack[-1][index]
            except IndexError:
                errors.indexError("Array index out of range")

def GET(index):
    global stack
    if len(stack) < 1:
        errors.stackArgumentLenError("GET")
    else:
        if type(stack[-1]) not in [list, str]:
            errors.valueError()
        else:
            try:
                stack.append(stack[-1][index])
            except IndexError:
                errors.indexError("index out of range")

def DEF(inst):
    global defs
    if inst[0] in dep.calls or inst[0] in dep.reserved or type(inst[0]) != str:
        errors.valueError()
    else:
        defs[inst[0]] = inst[1:]

def CMD():
    if len(stack) < 1:
        errors.stackArgumentLenError('CMD')
    else:
        os.system(stack[-1])

def QUIT():
    os._exit(1)


def HELP():
    print "\nFor language reference, see the documentation on the MontiLang Github repo"
    print "https://github.com/lduck11007/MontiLang\n"
    sys.exit()

def LICENSE():
    print "\nMonti v{} is open source and licensed under Mozilla Public License 2.0".format(gVars['_VERSION'])
    print "https://www.mozilla.org/en-US/MPL/2.0/\n"
    sys.exit()

if __name__ == "__main__":
    main()

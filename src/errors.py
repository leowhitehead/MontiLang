import sys

def invalidCommand(a = None):
    if a:
        print "Invalid command '{}'".format(a)
    else:
        print "Invalid Command"
    sys.exit()

def stackArgumentLenError(a = None):
    if a:
        print "invalid stack length for operation '{}'".format(a)
    else:
        print "invalid stack length for operation"
    sys.exit()

def syntaxError():
    print "Invalid Syntax"
    sys.exit()

def valueError():
    print "valueError"
    sys.exit()

def opError(a = None):
    print "Invalid types for operation"
    sys.exit()

def noClosingStatement(a = None):
    print "No closing statement for conditional/loop"
    sys.exit()

def reserved():
    print "Error: Cannot assign to reserved"
    sys.exit()

def error(a):
    print a
    sys.exit()

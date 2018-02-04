import sys
def noFile():
    print "no file specified"
    sys.exit()

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


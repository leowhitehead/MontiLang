import sys
import re

replace = [['+', 'PLUS'], 
    ['-', 'MINUS'],
    ['/', 'DIV'], 
    ['*', 'MULT'], 
    ['.', 'POP'],
    ['%', 'MOD'],
    ["CLS", "CLEAR"]]

reserved = [
    'PRINT',
    'PSTACK',
    'PLUS',
    'MINUS',
    'POP',
    'MULT',
    'MOD',
    'NEG',
    'MAX',
    'MIN',
    'DUP',
    'NIP',
    'ABS',
    'VAR',
    'DIV',
    'CLEAR',
    'SKIP',
    'INPUT',
    'ROT',
    'SWAP',
    'OUT',
    'WHILE',
    'IF',
    'ENDIF',
    'WHILE',
    'ENDWHILE',
    'FOR',
    'ENDFOR'
]

globalVs = {
    'TRUE':1,
    'FALSE':0,
    '_VERSION':"1.0",
    '_PLATFORM':sys.platform
}
def getArgs(s):
    args = []
    cur = ''
    inQuotes = 0
    for char in s.strip():
        if char == ' ' and not inQuotes:
            args.append(cur)
            cur = ''
        elif char == '|' and not inQuotes:
            inQuotes = 1
            cur += char
        elif char == '|' and inQuotes:
            inQuotes = 0
            cur += char
        else:
            cur += char
    args.append(cur)
    return args

def findLoop(t):   
  inds = [index for index, item in enumerate(t) if item in ["IF", "ENDIF", "FOR", "ENDFOR", "WHILE", "ENDWHILE"]]
  centre = inds[(len(inds)/2)-1:(len(inds)/2)+1]
  newCentre = t[centre[0]:centre[1]+1]
  return t[:centre[0]] + [newCentre] + t[centre[1]+1:]

def parse(instructions):
    instructions = re.sub(' +', ' ', instructions)
    instructions = re.sub('/#[ a-zA-Z0-9!@$%^&*()\'\",|.-_=+]*#/', '', instructions)
    instructions = getArgs(instructions)
    for index, item in enumerate(instructions):
        for i in replace:
            if item == i[0]:
                instructions[index] = i[1]
    instructions = [tryconvert(i) for i in instructions if i != '']
    return instructions

def getLoops(t):
  inds = len([index for index, item in enumerate(t) if item in ["FOR", "IF", "WHILE"]])
  for i in range(inds):
    t = findLoop(t)
  return t

def tryconvert(s, lower=False):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if '|' in s:
                return s
            else:
                if not lower:
                    return s.upper()
                else:
                    return s


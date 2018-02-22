import sys
import re
import os
from json import dumps, loads
from ast import literal_eval

replace = [['+', 'PLUS'], 
    ['-', 'MINUS'],
    ['/', 'DIV'], 
    ['*', 'MULT'], 
    ['.', 'POP'],
    ['%', 'MOD'],
    ["CLS", "CLEAR"],
    ["cls", "CLEAR"],
    ["exit", "QUIT"],
    ["EXIT", "QUIT"],
    ["<", "LESSTHAN"],
    [">", "MORETHAN"],
    ["<=", "LESSTHANEQ"],
    [">=", "MORETHANEQ"],
    ["==", "EQUALS"],
    ["!=", "NOTEQUALS"]]

calls = [
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
    'INPUT',
    'ROT',
    'SWAP',
    'OUT',
    'QUIT',
    'LESSTHAN',
    'MORETHAN',
    'LESSTHANEQ',
    'MORETHANEQ',
    'EQUALS',
    'NOTEQUALS',
    'EXIT',
    'LICENSE',
    'HELP',
]

reserved = [
    'IF',
    'ENDIF',
    'WHILE',
    'ENDWHILE'
    'ENDWHILE',
    'FOR',
    'ENDFOR',
    'TRUE',
    'FALSE',
    'TOP'
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

def parse(instructions):
    instructions = re.sub(' +', ' ', instructions)
    instructions = re.sub('/#[ a-zA-Z0-9!@$%^&*()\'\",|.\-_\[\]=\;<>?:\{\}+]*#/', '', instructions)
    instructions = getArgs(instructions)
    for index, item in enumerate(instructions):
        for i in replace:
            if item == i[0]:
                instructions[index] = i[1]
    instructions = [tryconvert(i) for i in instructions if i != '']
    return instructions

def getLoops(lst):
    start_keywords = ['FOR', 'IF', 'WHILE']
    end_keywords = ['ENDFOR', 'ENDIF', 'ENDWHILE']
    dump = dumps(lst)
    for k in start_keywords:
        dump = dump.replace('"{}"'.format(k), '["{}"'.format(k))
    for k in end_keywords:
        dump = dump.replace('"{}"'.format(k), '"{}"]'.format(k))
    loads(dump)
    return literal_eval(dump)

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
import sys
import re
import os
from json import dumps, loads
from ast import literal_eval
from itertools import chain

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
    ["!=", "NOTEQUALS"],
    [":", "TOP"]]

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
    'AND',
    'OR',
    'NOT',
    'CMD'
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

defs = {}

defined = []

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
    instructions = re.sub('/#[ a-zA-Z0-9!@$%^&*()\'\",|.\-_\[\]=\;<>?:\{\}+]*#/', '', instructions) #sorry
    instructions = getArgs(instructions)
    instructions = list(preprocess(instructions))
    defined = [i[1:] for i in [x for x in instructions if type(x) == list and x[0] == 'DEFINE']]
    included = [i[1:] for i in [x for x in instructions if type(x) == list and x[0] == 'INCLUDE']]
    instructions = [x for x in instructions if x[0] not in ['DEFINE', 'INCLUDE']]
    for index, item in enumerate(instructions):
        for i in defined:
            if item.lower() == i[0].lower():
                instructions[index] = i[1]
    for index, item in enumerate(instructions):
        for i in replace:
            if item == i[0]:
                instructions[index] = i[1]
    instructions = [tryconvert(i) for i in instructions if i != '']
    return instructions

def getLoops(lst):
    start_keywords = ['FOR', 'IF', 'WHILE', 'DEF']
    end_keywords = ['ENDFOR', 'ENDIF', 'ENDWHILE', 'ENDDEF']
    dump = dumps(lst)
    for k in start_keywords:
        dump = dump.replace('"{}"'.format(k), '["{}"'.format(k))
    for k in end_keywords:
        dump = dump.replace('"{}"'.format(k), '"{}"]'.format(k))
    loads(dump)
    return literal_eval(dump)

def tryconvert(s, lower=False):
    if type(s) == list:
        return s
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

def preprocess(elements):
    elements = iter(elements)
    for position, element in enumerate(elements):
        if element.startswith('&'):
            yield list(preprocess(chain([element[1:]], elements)))
        elif element.endswith('&'):
            element = element[:-1]
            yield element
            return
        else:
            yield element

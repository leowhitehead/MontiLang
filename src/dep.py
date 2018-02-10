import itertools

replace = [['+', 'PLUS'], 
    ['-', 'MINUS'],
    ['/', 'DIVIDE'], 
    ['*', 'MULTIPLY'], 
    ['.', 'POP'],
    ['%', 'MOD'],
    ["CLS", "CLEAR"],
    [r"\n", "ENDL"]]

reserved = [
    'PRINT',
    'PSTACK',
    'PLUS',
    'MINUS',
    'POP',
    'MULTIPLY',
    'MOD',
    'NEG',
    'ABS',
    'VAR',
    'DIVIDE',
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


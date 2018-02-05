import itertools

replace = [['+', 'PLUS'], 
    ['-', 'MINUS'],
    ['/', 'DIVIDE'], 
    ['*', 'MULTIPLY'], 
    ['.', 'POP'],
    ['%', 'MOD'],
    ["CLS", "CLEAR"]]

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
    'CLEAR'   
]

reserved2 = [
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

def findLoop(lst, start, end):
  new_data = [i for i, a in enumerate(lst) if a in [start, end]]
  groups = [new_data[i:i+2] for i in range(0, len(new_data), 2)]
  final_data = [[a, list(b)] for a, b in itertools.groupby(enumerate(lst), key=lambda (x, y):any(x in range(a, b+1) for a, b in groups))]
  return list(itertools.chain(*[[c for _, c in b] if not a else [[c for _, c in b]] for [a, b] in final_data]))
                    #idk how any of this function works

def tryconvert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if '|' in s:
                return s
            else:
                return s.upper()


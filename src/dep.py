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
    'CLEAR',
    'WHILE',
    'ENDWHILE',
    'IF',
    'ENDIF',
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

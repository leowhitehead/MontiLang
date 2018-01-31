rep = [['+', 'PLUS'], 
    ['-', 'MINUS'],
    ['/', 'DIVIDE'], 
    ['*', 'MULTIPLY'], 
    ['.', 'POP'],
    ['%', 'MOD']]

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
    True,
    False,
    
]

def tryconvert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s.upper()
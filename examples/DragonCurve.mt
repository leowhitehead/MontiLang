/# Generates first 8 iterations of the regular paperfold sequence #/

DEF reverse
    VAR list LEN VAR i CLS

    WHILE i
        i 1 - VAR i .
        list GET i NIP
    ENDWHILE ARR
ENDDEF

DEF invert
    VAR list LEN VAR count CLS
    0 VAR i .

    FOR count
        list GET i NOT NIP
        i 1 + VAR i .
    ENDFOR ARR
ENDDEF

DEF concat
    SWAP + SWAP +
ENDDEF

DEF update
    VAR t1 .
    1 ARR VAR t2 .
    t1 invert reverse VAR t3 .
    t1 t2 t3 concat 
ENDDEF

DEF printArr
    LEN 1 - VAR stLen .
    0 VAR j .
    FOR stLen
        GET j 
        TOSTR OUT .
        j 1 + VAR j .
    ENDFOR
    || PRINT .
ENDDEF

1 ARR 
FOR 8 update ENDFOR
printArr

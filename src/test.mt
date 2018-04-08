/# loops through numbers 1-100. Prints 'Fizz' if it is a multiple of 3, 'Buzz' if it is a multiple of 5,
'FizzBuzz' if it is a multiple of both, or the number if neither #/

&DEFINE LOOP 100&
1 VAR i .

FOR LOOP
    || VAR ln .
    i 5 % 0 == 
    IF : .
        ln |Buzz| + VAR ln .
    ENDIF
    i 3 % 0 ==
    IF : .
        ln |Fizz| + VAR ln .
    ENDIF
    ln || ==
    IF : .
        i PRINT .
    ENDIF
    ln || !=
    IF : .
        ln PRINT .
    ENDIF
i 1 + VAR i .
ENDFOR
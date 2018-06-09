---
layout: other
---
### Jump To:
1. [HelloWorld.mt](#helloworldmt)
2. [Count.mt](#countmt)
3. [CountDown.mt](#countdownmt)
4. [Name.mt](#namemt)
5. [Fibonacci.mt](#fibonaccimt)
6. [FizzBuzz.mt](#fizzbuzzmt)
7. [PaperFold.mt](#paperfoldmt)
8. [Rule110.mt](#rule110mt)


### HelloWorld.mt
A simple program that prints the phrase 'Hello World' to the console

```nginx
/# Prints 'Hello World' #/

|Hello World| PRINT .
```

### Count.mt
A program that takes a number as input, then counts to that number sequentially starting at 1

```nginx
/# takes a number as input, counts to number #/

|Enter a number to count to: | INPUT NIP VAR count .
1 VAR num . 
FOR count
    num print
    1 + var num .
ENDFOR
```

### CountDown.mt
A program that takes a number as an input, then counts from that number to zero.

```nginx
/# counts to 0 from given number with a while statement #/

|Enter a number to count from: | INPUT NIP
VAR num .

WHILE num
    num PRINT 
    1 - VAR num .

ENDWHILE
```

### Name.mt
A program that takes an input as a name, and then responds with that name

```nginx
/# asks for a user's name and responds with it back #/

|What is your name? | INPUT NIP
|Hello, | OUT 
SWAP PRINT .
```

### Fibonacci.mt
A program that prints the first 40 numbers in the Fibonacci sequence

```nginx
/# programming example displaying the first 20 numbers of the #/
/# fibonacci sequence with a for loop #/

0 VAR a .
1 VAR b .

FOR 20
    a b + VAR c .
    a PRINT .
    b VAR a .
    c VAR b .
ENDFOR
```

### FizzBuzz.mt
A program that loops through the numbers 1-100, prints 'Fizz' if the number is divisible by 3, 'Buzz' if it is divisible by 5, and 'FizzBuzz' if it is divisible by both 3 and 5.

```nginx
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
```

### PaperFold.mt
Gets input n as integer, prints to nth iteration in the [Regular PaperFold Series](https://en.wikipedia.org/wiki/Regular_paperfolding_sequence)

```nginx
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
    LEN VAR stLen .
    0 VAR j .
    FOR stLen
        GET j 
        TOSTR OUT .
        j 1 + VAR j .
    ENDFOR
    || PRINT .
ENDDEF

|Enter a number: | INPUT NIP TOINT VAR loop .
1 ARR 
FOR loop update printArr ENDFOR
```

### Rule110.mt
[Rule 110](https://en.wikipedia.org/wiki/Rule_110) is an elementary cellular automation. It is similar to Conway's game of life, with the difference being that it is one dimentional, while still being turing complete. It follows the rules as shown:

| Current Pattern           | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
|---------------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| New State for center cell | 0   | 1   | 1   | 0   | 1   | 1   | 1   | 0   |

This program shows an array of 100 cells being updated through 100 iterations of this simulation.

```nginx
100 VAR length .
100 VAR height .

FOR length 0 ENDFOR 1 0 ARR VAR list . 
length 1 - VAR topLen . 
FOR topLen 0 ENDFOR 1 ARR VAR topLst .  

DEF getNeighbors
    1 - VAR tempIndex . 
    GET tempIndex SWAP 
    tempIndex 1 + VAR tempIndex .
    GET tempIndex SWAP 
    tempIndex 1 + VAR tempIndex .
    GET tempIndex SWAP .
    FOR 3 TOSTR ROT ENDFOR
    FOR 2 SWAP + ENDFOR  
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

FOR height
    FOR length 0 ENDFOR ARR VAR next .
    1 VAR i .
    FOR length
        list i getNeighbors VAR last . 
        i 1 - VAR ind .
        last |111| == 
        IF : .
            next 0 INSERT ind
        ENDIF

        last |110| ==
        IF : .
            next 1 INSERT ind
        ENDIF

        last |101| ==
        IF : .
            next 1 INSERT ind
        ENDIF

        last |100| ==
        IF : .
            next 0 INSERT ind
        ENDIF

        last |011| ==
        IF : .
            next 1 INSERT ind
        ENDIF

        last |010| ==
        IF : .
            next 1 INSERT ind
        ENDIF

        last |001| ==
        IF : .
            next 1 INSERT ind
        ENDIF

        last |000| ==
        IF : .
            next 0 INSERT ind
        ENDIF
        clear
        i 1 + VAR i .
    ENDFOR 
    next printArr .
    next 0 ADD APPEND . VAR list .
ENDFOR
```

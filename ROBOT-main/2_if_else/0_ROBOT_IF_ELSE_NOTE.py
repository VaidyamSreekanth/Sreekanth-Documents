# Robot support all python comparison operations
==, !=, >, <,>=, <= 

1. In robot we can't create if block. If we want to run a block of code based on condition then we have to create a keyword with  block of code then we can run this keyword based on condition using "Run Keyword If" KEYWORD.
# Example :- Run Keyword If   2 == 2    Add    ${ONE}    5

2. In robot we can use IF and ELIF and ELSE also, like below

    Run Keyword If   2 == 4    Log    if block      WARN
    ...   ELSE IF    3 == 3    Log    first elif    WARN
    ...   ELSE IF    3 == 6    Log    Second elif   WARN
    ...   ELSE    Log   Else block is     ERROR
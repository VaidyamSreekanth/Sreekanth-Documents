1. Using regular expressions we can find a string based on pattern.
2. Using re module we can do regular expression operations

# Regular Expression Patterns
'\d  ==>  Match a digit   : [0-9]
'\D  ==>  Match a nondigit: [^0-9]
'\s  ==>  Match a whitespace character
'\S  ==>  Match a nonwhitespace character
'\w  ==>  Match a single character : [A-Za-z0-9_]
'\W  ==>  Match a single nonword character: [^A-Za-z0-9_]
'\n  ==>  Match a new line character


+   ==>  Matches 1 or more occurrence of preceding expression.
*   ==>  Matches 0 or more occurrence of preceding expression.
?   ==>  Matches 0 or 1 occurrence of preceding expression.
^   ==>  Matches beginning of line.
'$   ==>  Matches end of line.
|   ==>  To do OR operation
.   ==>  Matches any single character except newline.
'\'   ==>  Used to escape any special character and interpret it literal

()  ==>  Using parentheses we can create a groups
[]  ==>  Using square brackets "[]" Matches any single character in brackets.
{}  ==>  Matches exactly n number of occurrences of preceding expression.




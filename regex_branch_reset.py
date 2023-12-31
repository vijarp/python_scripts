"""
Task

You have a test string .
Your task is to write a regex which will match , with following condition(s):

 s consists of 8 digits.
 s must have "---", "-", "." or ":" separator such that string  gets divided in  parts, with each part having exactly two digits.
 s string must have exactly one kind of separator.
Separators must have integers on both sides.

Valid 

12-34-56-78
12:34:56:78
12---34---56---78
12.34.56.78
Invalid 

1-234-56-78
12-45.78:10

"""
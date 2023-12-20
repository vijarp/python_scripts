"""Task

You have a test string .
Your task is to write a regex that will match  with following conditions:

 must be of length: 6
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
"""

Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][\.\,]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("First Task : ")))).lower())


"""
Task

You have a test string .
Your task is to write a regex that will match  with the following conditions:

 must be of length 6.
First character should not be a digit (  or  ).
Second character should not be a lowercase vowel (  or  ).
Third character should not be b, c, D or F.
Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
Fifth character should not be a uppercase vowel (  or  ).
Sixth character should not be a . or , symbol.
"""


Regex_Pattern = r'^\D[^aeiou][^bcDF][^\s][^AEIOU][^\.\,]$'	
print(str(bool(re.search(Regex_Pattern, input("Second Task : ")))).lower())

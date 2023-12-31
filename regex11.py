"""Task

You have a test string .
Your task is to write a regex which will match , with following condition(s):

 consists of 8 digits.
 may have "" separator such that string  gets divided in  parts, with each part having exactly two digits. (Eg. 12-34-56-78)
Valid 

12345678
12-34-56-87
Invalid 

1-234-56-78
12-45-7810
"""


Regex_Pattern = r"^\d{2}(.?)\d{2}\1\d{2}\1\d{2}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
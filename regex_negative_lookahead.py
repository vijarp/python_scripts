"""Task

You have a test String S.
Write a regex which can match all characters which are not immediately followed by that same character."""

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))




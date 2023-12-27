"""
Task
You have a test string S.
Your task is to write a regex that will match S with the following conditions:
• S must be of length:
• 1St character: lowercase letter.
• 2nd character: word character.
• 3rd character: whitespace character.
• 4th character: non word character.
• 5th character: digit.
• 6th character: non digit.
• 7th character: uppercase letter.
• 8th character: letter (either lowercase or uppercase).
• 9th Character: vowel (a, e, i , o , u, A, E, l, O or U).
• 10th character: non whitespace character.
• 11th character: should be same as 1st
• 12th character: should be same as 2nd
• 13th character: should be same as 3rd
• 14th character: should be same as 4rd
• 15th character: should be same as 5th
• 16th character: should be same as 6th
• 17th character: should be same as 7th
• 18th Character: should be same as 8th
• 19th Character: should be same as 9th
• 20 character: should be same as 10th character.

"""



Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([A-Za-z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.

import re
#Sample Input - ab #1?AZa$ab #1?AZa$
print(str(bool(re.search(Regex_Pattern, input()))).lower())
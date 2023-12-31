import re
cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01','6476-579052']


for phone in cellphones:
	# Get all phone numbers not preceded by area code
	
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}?", phone)
	print(number)
	
print("*****Second part************")
for phone in cellphones:
	# Get all phone numbers not preceded by area code
	
	number2 = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number2)
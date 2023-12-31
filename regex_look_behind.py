import re
sentiment_analysis = "You need excellent python skills to be a data scientist. Must be! Excellent python"

# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)
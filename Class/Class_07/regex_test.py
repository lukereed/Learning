# Luke Reed
# regex_test.py
# 03/03/2016
# simplified matching example from new .pdf document

import re

# match will return a match as long as the first bit of the argument matches the search value
match = re.match('dog', 'dog cat dog')
print match.group(0)
# cat cannot be matched as it is not the first element

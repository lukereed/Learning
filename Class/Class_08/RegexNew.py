# Luke Reed
# RegexNew.py
# 03/10/2016

import re

match = re.match('dog', 'dog cat dog')
print match.group(0)

# This will give us an error as cat cannot be matched at the beginning of string
# match2 - re.match(r'cat', 'dog cat dog')
# print match2.group(0)

match3 = re.search(r'cat', 'dog cat dog')
print match3.group(0)		# returns the first match
print match3.start()		# returns the index of the beginning of the match
print match3.end()			# returns the idnex of the end of the match

match4 = re.search(r'dog', 'dog cat dog')
print match4.group(0)

match5 = re.findall(r'dog', 'dog cat dog')		# returns all matches in a string
print match5									# stored in a list for us

match6 = re.findall(r'cat', 'dog cat dog')
print match6


contactInfo = 'Doe, John: 555-1212'
match7 = re.search(r'(\w+), (\w+): (\S+)', contactInfo)	# \w -> word, \S -> nonwhite space
print match7.group(0)		# extracts full result
print match7.group(1)		# extracts 'Doe'
print match7.group(2)		# extracts 'John'
print match7.group(3)		# extracts '555-1212'

# we can also store the variables with tags and then reference them in the extraction
match8 = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
print match8.group('first')
print match8.group('last')
print match8.group('phone')

match9 = re.findall(r'(\w+), (\w+): (\S+)', contactInfo)
print match9



# We can also use the substitute/replace method re.sub
phone = "2004-959-559 # This is Phone Number"

# Delete python-style comments
num = re.sub(r'#.*$',"",phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num


# Regex Exercise 1
# Ask the user for the full URL of a company and extract and present just the company name
# assuming the format http://www.company_name.com

# companyURL = raw_input("What is the company URL?")
url = 'http://www.google.com'

url_match = re.search(r'(https?)://(www)*(\.)*(?P<company>[a-zA-Z0-9]+).(\D{3})', url)
# can have http or https
# uses '.' as the delimeter
# create company tag and allow it to have any character
# we know the end will be three digits so we extract just the last 3
print url_match.group(0)
print url_match.group(1)
print url_match.group(2)
print url_match.group(3)
print url_match.group(4)
print url_match.group(5)

print url_match.group('company')



# Regex Exercise 1b
# Ping the above URL and extract the 4 numbers of the IP address


# Regex Exercise 2
test = "John's SS# is 98-412-3467 and his Phone is 123-4567. Mary's SS# is 12-234-5679 and her phone is '232-4534'"
#  In the above string "delete the phone numbers but not the SS#'s for the two people

# my attempt
test_sub = re.sub(r'\s\d\d\d-\d\d\d\d\s',"",test)
print test_sub

# solution
# [ '][0-9]{3}-[0-9]{4}
test_sol = re.sub(r"[ '][0-9]{3}-[0-9]{4}","",test)
# square brackets mean one or the other
print test_sol
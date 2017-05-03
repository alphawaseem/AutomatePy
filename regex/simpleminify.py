import re

regexObj = re.compile('\s+')

text = '''Hello there     I have looot of    spacees and              too \n\
# Make a regex object
phoneNumRegex = re.compile(u'(\d{3})-?(\d{4}-\d{3})')


testString = 'This is a test string it has my number\
767-6424-299 in various formats like -6424-299, 767-6424-299,\
767 6424 299, 7676 4242 99, 7676424299, 76764 24299\
(767)-6424-299 and   so on.'

testString2 = 'This string doesn\'t have any number'

# Regex object's search method returns match object if pattern is
#  found else None

matchedObject = phoneNumRegex.findall(testString)

# matchedObject has group method which contains the result
if matchedObject:
    print(matchedObject)
else:
    print('No match found')'''

minified = regexObj.sub(' ', text)
print(text)
print(minified)

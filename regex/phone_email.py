#!/home/peace/anaconda3/bin/python
import pyperclip
import re


# Regex object for phone number
phoneRegex = re.compile(u'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})  
)''', re.VERBOSE)

# Regex Object for email address
emailRegex = re.compile(u'''(
    ([a-zA-Z0-9._%+-]+)
    @
    ([a-zA-Z0-9.-]+)
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Get String from clipboard
text = str(pyperclip.paste())
matches = []
if text:
    # Perform search
    print('Performing search.....')

    # Find phone numbers
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        print(phoneNum)
        matches.append(phoneNum)

    # Find email address
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
        print(groups[0])

    if matches:
        matches = '\n'.join(set(matches))
        pyperclip.copy(matches)
        print('Copied to clipboard')
        print(matches)
else:
    print('Please copy something to clipboard and try again.')

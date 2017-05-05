import re
import pyperclip

durationRegex = re.compile(
    u'(\d+:\d+)')
text = str(pyperclip.paste())

if text:
    matches = durationRegex.findall(text)
    if not matches:
        print('No match found')
        exit()
    matches = matches[-12:]
    for match in matches:
        print(match)
else:
    print('Please copy some text and try again')

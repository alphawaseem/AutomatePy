#! python
import pyperclip
import re

phoneRegex = re.compile(u'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})  
)''', re.VERBOSE)

emailRegex = re.compile(u'''(
    ([a-zA-Z0-9._%+-]+)
    @
    ([a-zA-Z0-9.-]+)
    (\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

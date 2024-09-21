"""
basics of regex module
"""
#pylint: disable=line-too-long
import re

phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # find a typical phone number by creating this regex object

# check = phone_regex.search("This is a long piece of text where data is going to be processed and search for a regex object. There is all kinds of data but most importantly, there is a phone number 555-555-5555 here in the text that can be searched for.")
check = phone_regex.search("This is a long piece of text where data is going to be processed and search for a regex object. There is all kinds of data but most importantly, there is a phone number (555)555-5555 here in the text that can be searched for.")

#consider the sitauation of the above lines. both are realistic scenarios. consider variance in data when trying to utilizing regex in a solution.

if check:
    print('Phone number matching regex object found: ' + check.group())
else:
    print('no phone found')

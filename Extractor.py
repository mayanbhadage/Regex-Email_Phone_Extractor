'''
This is a sample program to extract the email is and phone number from the large amount of data
'''

import re

import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(((\d\d\d-)|(\(\d\d\d\)))    # For matching XXX- or (XXX) Area Code
\d\d\d-                     # For matching next 3 digits of Phone Number with dash
\d\d\d\d)                   # For matching last four Phone Number


''',re.VERBOSE)

# Create a regex for email addresses

emailRegex = re.compile(r'''
[a-zA-z0-9._+]+      #name
@                   # at
[a-zA-z0-9._+]+
''',re.VERBOSE)

# Get the text off the clipboard

text = pyperclip.paste()

#Extract phone no and email from the text
extractedPhoneNo = phoneRegex.findall(text)
extractedEmailAddr = emailRegex.findall(text)

#Extraxting the phone number group
phone_no = []
for phone in extractedPhoneNo:
    phone_no.append(phone[0])

# Copy extracted phone no and email to the clipboard

res = zip(phone_no,extractedEmailAddr)
result = ""
for x,y in res:
    result =result + str(x) + ',' + str(y) + "\n"

print result
print len(res)
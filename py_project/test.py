print('Hello World')


import re

s = 'string hello world'
if re.search(r'lo', s):
    print('correct match!')
else:
    print('re wrong!')
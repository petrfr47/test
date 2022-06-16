import re

a='dfg456uyt99999'

if b:= re.search('d.+(56)\w?(yt)',a):

    print(b.group(2))
else:
    print('False')

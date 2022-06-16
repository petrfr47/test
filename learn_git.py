import re

a='dfg456uytvvvvvvvvvvvvvvv'

if b:= re.search('d.+(56)\w?(yt)\w+$',a):


    print(b.group(2))
else:
    print('False')

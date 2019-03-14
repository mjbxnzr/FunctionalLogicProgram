import re

arr = [1,34,56,'98abc', 'd', -1, 0, '#', 34, 56, 'sds', 'ewe',
       '34', 44, 1, 3, 'qbcd', 23, '345', '23', '-10', 10,
       -10, 345, 45, '23', 'aer', '12ac', 'anc34', 'asas']

IsInteger = [x for x in arr if type(x)==int]
IsNotInteger = str([y for y in arr if type(y)!=int])

for x in IsNotInteger:
    extract = map(int,re.findall('\d+',IsNotInteger))
#I want to add something
#no nothing new here
combine=sorted(sorted(IsInteger)+sorted(extract))
arr2=sorted(list(dict.fromkeys(combine)))

print(arr2)

This is to answer the question at https://stackoverflow.com/questions/54612255/taking-n-number-of-integer-inputs-from-a-single-line-in-python/54615493#54615493

```bash
>>> import re
>>> 
>>> s = '12 34      56     34   45'
>>> l = re.split('\s+', s)
>>> l
['12', '34', '56', '34', '45']
>>> 
>>> [int(n) for n in l]
[12, 34, 56, 34, 45]
>>> 
>>> # Using the above concept, it can be easily done without the need of explicit n (that you are taking)
... 
>>> mylist = [int(n) for n in re.split('\s+', input("Enter integers (1 by 1): ").strip())]
Enter integers (1 by 1): 12 34   56 67  99 34 4 1 0 4 1729
>>> 
>>> mylist
[12, 34, 56, 67, 99, 34, 4, 1, 0, 4, 1729]
>>> 
>>> sum(mylist)
2040
>>> 
```
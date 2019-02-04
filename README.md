# pyrandocs

<h3 id='1'>String formatting</h3>

```bash
>>> d = {
...     "complex": 5+6j,
...     "int": 1729,
...     "float": 3.14,
...     "string": "Bangalore",
...     "list": [1, 2, 3, 4, -7, 0],
...     "tuple": (4,),
...     "dictionary": {'fullname': 'Rishikesh Agrawani', 'active': True}
... }
>>>
>>> for key, value in d.items():
...     print('{0:10s} : %s'.format(key) % (value))
... 
string     : Bangalore
dictionary : {'active': True, 'fullname': 'Rishikesh Agrawani'}
tuple      : 4
int        : 1729
float      : 3.14
list       : [1, 2, 3, 4, -7, 0]
complex    : (5+6j)
>>> 
```

<h3 id='2'>Stackoverflow - a solution to a problem in a simple way / no use of advanced Python concepts </h3>

> https://stackoverflow.com/a/54500843/6615163
>
> You can try it online at https://rextester.com/ISE37337

```python
# python 3.5.2

def get_count():
    n = int(input())
    
    for i in range(n):
        s = input().strip()
        
        if not i:
            l = list(set(s))
        else:
            i = 0
            while l and i < len(l) - 1:
                ch = l[i]
                if not ch in s:
                    l.remove(ch)
                else:
                    i += 1
                    
    return len(l)
                    

count = get_count()                    
print(count) # 2
```

<h3 id='3'>List and range() based problem's solution</h3>

> https://stackoverflow.com/questions/54505461/how-to-print-out-elements-from-the-list-that-have-the-difference-of-2

```python
>>> 
>>> l = [1, 7, 12, 14, 22, 24, 29, 31, 39, 45, 77, 79, 85, 100]
>>> output = [(l[i], l[j]) for i in range(len(l) - 1) for j in range(i + 1, len(l)) if abs(l[i] - l[j]) == 2]
>>> output
[(12, 14), (22, 24), (29, 31), (77, 79)]
>>> 
```

```python
>>> 
>>> l = [1, 7, 12, 14, 22, 24, 29, 31, 39, 45, 77, 79, 85, 100]
>>> 
>>> n = len(l) - 1
>>> output = [(l[i], l[i + 1]) for i in range(0, n, 2) if abs(l[i] - l[i + 1]) == 2]
>>> output
[(12, 14), (22, 24), (29, 31), (77, 79)]
>>> 
>>> s = '\n'.join([str(output[i][0]) + ', ' + str(output[i][1]) for i in range(len(output))])
>>> print(s)
12, 14
22, 24
29, 31
77, 79
>>> 
```



<h3 id='references'>References</h3>

+ [How to get a list of class attributes in Python](https://www.blog.pythonlibrary.org/2013/01/11/how-to-get-a-list-of-class-attributes/)

+ [List attributes of an object](https://stackoverflow.com/questions/2675028/list-attributes-of-an-object)

+ [datetime, date, time](https://www.programiz.com/python-programming/datetime#example-difference-date)
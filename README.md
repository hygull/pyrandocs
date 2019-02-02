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




<h3 id='references'>References</h3>

+ [How to get a list of class attributes in Python](https://www.blog.pythonlibrary.org/2013/01/11/how-to-get-a-list-of-class-attributes/)

+ [List attributes of an object](https://stackoverflow.com/questions/2675028/list-attributes-of-an-object)

+ [datetime, date, time](https://www.programiz.com/python-programming/datetime#example-difference-date)
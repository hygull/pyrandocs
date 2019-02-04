### Problem link

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


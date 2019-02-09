[https://stackoverflow.com/questions/54604469/how-to-print-information-from-dictionary-in-format-error-messagedict-object](https://stackoverflow.com/questions/54604469/how-to-print-information-from-dictionary-in-format-error-messagedict-object)

```python
	def print_message(d):
	    print(d["name"] + ':')
	    
	    for grade, attendance in zip(d["grades"], d["attendance"]):
	        print(grade, attendance

	kayleigh = {'name':'Kayleigh',
	            'grades':[100,80,67,100,89],
	            'attendance':['True','True','True','True','True']}

	print_message(kayleigh)
```

```bash
Kayleigh:
True 100
True 80
True 67
True 100
True 89
```
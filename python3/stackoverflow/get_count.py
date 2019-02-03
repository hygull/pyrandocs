# python 3.5.2
# https://stackoverflow.com/questions/54500318/how-to-take-n-input-and-perform-operation-on-them-in-python-3
# https://rextester.com/ISE37337
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
print(count)
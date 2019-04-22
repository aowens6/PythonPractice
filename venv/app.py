names = ['name1','name2', 'name3','name4',]

for index, name in enumerate(names, start=1):
    print(index, name)

#unpacking
a,b,*c,d = [1,2,3,4,5]

print(a)
print(b)
print(c)
print(d)

#ignoring values
e,f,g,*_,h = [6,7,8,9,10,11,12,13]

print(e)
print(f)
print(g)
print(h)
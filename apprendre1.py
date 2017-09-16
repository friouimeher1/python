def bom():
    y=[i+1 for i in range(6)]
    return (y)

print(bom())

liste=[]
for i in bom():
    liste.append(i)
print(liste)



print("hello world !!!")


print('{} - {} '.format(1,2))



a=5
v=6

print('{} + {} = {} '.format(a,v,int(a+v)))

print('{} - {} = {} '.format(a,v,int(a-v)))

print('{} * {} = {} '.format(a,v,int(a*v)))

print('{} / {} = {} '.format(a,v,int(a/v)))

print('{} ** {} = {} '.format(a,v,int(a**v)))

print('{} // {} = {} '.format(a,v,int(a//v)))

def f(**t):
    print(t)


print('++++++++++++++++++++++')
f(name='meher',first_name='FRIOUI',age=26)
print('++++++++++++++++++++++')


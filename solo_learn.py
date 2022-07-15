a = [ 2,3 ]
b = [ 2,6 ]

a[1] *= 3
b[1] *= 3

print(int(a is b))


x,y = 0, True
x = x + 1
y = int(True)
print(y)

a = [ 2,4,5 ]
for i in range(1,3):
    a[i] = a[i -1]
    print(a[i])



x = 5
for x in range(10):
    x+=1
print(x)


print(('hello').upper())


i = [x for x in range(1,5)]
f = [2 if x % 2 else 5 for x in i ]
print(f)
n = [x*s for x,s in zip(i,f)]
print(n)


#def tax (n):
#    t = (n - 20000) * 20/100
#    m = 10000 * 10/100
#    n = 10000 * 0/100
#    return t + m + n
#print(tax(10000))
#
#def remove_chars(word,n):
#    print('original string: ', word)
#    x = word[n:]
#    return x
#
#print(remove_chars("pynative", 4))
#
#
#numbers_x = [10,20,30,40,10]
#
#first = numbers_x[0]
#last = numbers_x[-1]
#
#for i in range(1,11):
#    w = [i*j for j in range(1,11)]
#    print(w)
#
#for num in range(1,10):
#    for i in range(num):
#        print(num, end = ' ')
#    print('\n')

#s = 1231
#w = str(s)
#print(w[:])
#print(w[::-1])
#
#if w[:] == w[::-1]:
#    print('it is a palindrome')
#else:
#    print('it is not a palindrome')

#list1 = [10,20,25,30,35]
#list3 = []
#for i in list1:
#    if i%2 == 1:
#        list3.append(i)
#print(list3)
#
#for num in range(5,0,-1):
#    print(num * '*', end = ' ' )
#    print('\n')

#learning classes
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Pair({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

p = Pair(3,4)
print(p)

















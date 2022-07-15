a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2 } 

print(a.keys()) 
print(b.keys())

print(a.keys() & b.keys())


c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)


a = [1,5,2,1,9,1,5,10]

b = set(a)
print(b)

c = list(b)
print(c)

#problem : you have a sequence of itmes and you'd like to determine the most frequently ocurring items in the sequence
words = "into my eyes look into my eyes the eyes the eyse the eyes not around the eyes don't look around the eyes look into my eyes you're under"
word_list = words.split()
print(word_list)
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))

portfolio = [
{'name' : 'IBM', 'shares' : 100, 'price': 91.1 },
{'name' : 'APPL', 'shares' : 50, 'price': 543.22 },

{'name' : 'FB', 'shares' : 200, 'price': 21.09 },
{'name' : 'HPQ', 'shares' : 35, 'price': 31.75 },
{'name' : 'YHOO', 'shares' :45, 'price': 16.35 },
{'name' : 'APPL', 'shares' :'75', 'price' :115.65 },

]
cheap = heapq.nsmallest(3, portfolio, key = lambda s : s['price'])
print(cheap)

nums = [ 1,8,2,23,7,-4,18,23,42,37,2 ]
heap = list(nums)
print(nums.sort())
heapq.heapify(heap)
print(heap)


#defaultdict automatically intitializes the first value so you can simplify focus on adding items



print('i am here')




def countdown(n):
    print('starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print(next(c))

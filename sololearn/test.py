import numpy as np
r = int(input())
lst = [float(x) for x in input().split()]
arr = np.array(lst)

arr_new = arr.reshape(r,-1)
print(arr_new)

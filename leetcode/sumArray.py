       
import collections
import numpy as np

# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

# Array a mutates into a new array b of length n.
# For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
# Example

# For n = 5 and a = [4, 0, 1, -2, 3], the output should be solution(n, a) = [4, 5, -1, 2, 1].

# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the resulting array after the mutation will be [4, 5, -1, 2, 1].
def solution(n, a):
    b = [0]*n
    
    for i in range(0,n):
        print(i)
        temp =  0 if i-1<0 else a[i-1]
        temp2 =  a[i+1]  if i+1<n else 0  
        b[i] = temp + a[i]+ temp2      
    return b 
        


def solution2(a, b, k):
    n = len(a)
    tiny = 0
    for i in range(0, n):
        y =  b[n-1-i]#b[n-1] if i ==0 else b[n-i] 
        x = a[i]
        xy= int("{0}{1}".format(x, y))
        print(xy)
        if xy<k:
            tiny = tiny +1
    return tiny


def solution3(a):
    my_sum = 0
    n = len(a)
    for i in range(n):
        for j in range(n):
            ij = int("{0}{1}".format(a[i], a[j]))
            my_sum = my_sum + ij
    return my_sum

def solution4(a):
    my_sum = 0
    n = len(a)
    aa = np.array(a)
    b =  aa[np.transpose(np.triu_indices(len(aa), 1))]

    for i in range(n):
        for j in range(n):
            ij = int("{0}{1}".format(a[i], a[j]))
            my_sum = my_sum + ij
    return my_sum   
       
def concatenatSum(a):
    tot = 0
    dic = collections.defaultdict(int)
    for i in range(len(a)):
        _str = str(a[i])
        n = len(_str)
        dic[n]+=1
    
    for i in  range(len(a)):
        for k,v in dic.items():
            tot+=a[i]*(v*pow(10,k))
        tot+=(a[i]*len(a))
    
    return tot
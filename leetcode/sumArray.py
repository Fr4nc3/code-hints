       
import collections
import numpy as np
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
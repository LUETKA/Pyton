a=[0 for i in range(5)]
print(a)

n=5
b=[i**2 for i in range(n)]
print(b)

from random import randrange
n=10
c=[randrange(1,10) for i in range(n)]
print(c)

s='ab12c59p7dq'
digits=[int(i)for i in s if'0'<=i<='9']
print(digits)

#split
s=input('через пробел')
a=s.split()
print(a)

a=input('enter ').split()
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

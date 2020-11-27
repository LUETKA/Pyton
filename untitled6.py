#2
s=input('введите элементы списка через пробел')
a=[int(s) for s in s.split()]
for i in a:
    if int(i)%2 ==0:
        print(i, end=' ')
#3
a=[int(i) for i in input('введите элементы').split()]
for i in range(1, len(a)):
    if a[i] >a[i - 1]:
        print(a[i])
#4

a = [int(i) for i in input('введите элементы').split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
#1
a = input('введите элементы списка через пробел').split()
for i in range(0, len(a), 2):
    print(a[1])

#5
a=[int(i) for i in input('введите элементы списка через пробел').split()]
counter = 0
for i in range(1, len(a) --1):
    if a[i --1]< a[i]>a[i +1]:
        counter +=1
        print(counter)
       
#6
a=[int(i) for i in input('введите элементы').split()]
for i in range(len(a)):
    if a[i]==max(a):
        print(max(a),i)
        break


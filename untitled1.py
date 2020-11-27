i=1 #счетчик 
for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blu', 'violet' :
    print('#',i, color, sep='')
    i=i+1
    
    #
    for i in 1,2,3, 'one', 'two', 'three':
        print(i)
for i in range(4):#0,1,2,3
       print('#i',i) 
       print('i'**2,i**2)
print ('end')
   #
sum=0
n=5
for i in range(1, n +1):
      sum += i
      print(sum)
print(1,2,3)
print(4,5,6)
print(1,2,3, sep=',', end='.')
print(4,5,6, sep=',', end='.')
print()
print(1,2,3, sep='', end='--')
print(4,5,6, sep=' * ', end='.')

for i in range(1,101):
    if i%5==0:
      print(i)
      
# i=1  
# for city in 'narva', 'tallin', 'johvi':
#     print(i,city)
#     i+=1
# print()


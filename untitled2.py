
for i in range(1,11):
    print (f'таблица умножения на {i}')
    for j in range(1,11):
        print(f'{i}x{j}={i*j}',end='\t')
        
#2
for i in range(1,11):
    for j in range(1,11):
        print('{0:>3}'.format(j*i),end="")
    print()
    
#random
#import random
#random.randinet(A,B)
#random.randrange(a,b,2)
#random.random() 0...1

import random
a=random.randint(1,10)
print('a',a)

b=random.randrange(0,10,2)
print('b',b)

c=random.random()
print('c',c)


import random
numbers=random.randint(1,50)
c=True
while c:
    b=int(input('введите число'))
    if b==numbers:
        print('угадали')
        c=False
    elif b<numbers:
        print('загаданное больше')
    else:
        print('Загаданное меньше')
        break
else:
        print('Цикл завершен')

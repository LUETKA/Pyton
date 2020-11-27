a=list('lists')
print(a)

Cars=['BMW','Opel','Ford','Porsche']
print(Cars[3],'[3]') #один элемент
for i in range(len(Cars)):
    print(Cars[i]) #все элементы
    
a=[]
n=int(input('сколько элементов у нас будет'))
for i in range(n):
  e=int(input('элемент'))  
  a.append(e)
print(a)

  
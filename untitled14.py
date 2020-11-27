def bigger(a,b):
    if a>b:
        print(a)
        
        else:
            print(b)
            
bigger(a,b)

#2
def person(name, age):
    print(name,"is",age, "yers old")
    
    person(age=input('age'),name=input('name' )
           
 #3
 def space(planet_name, centet="Star"):
     print(planet_name,"is arbiting a", center)
     
     space("Mars")
#("Mars", "black Hole")

#4
def unknown(*args):
    for argument in args:
        print(argument)
        
unknown("hello", "world")
unknown(1,2,3,4,5)
unknown()

#5
#return
def bigger (a,b):
    if a > b:
        return a
    return b

num=bigger(23,42)
print(num)

#6

#lokal/global
age=44 #глобальная

def info():
    print(age)
    
def local_info():
    age = 22
    print(age)

info()
local_info()

#7
#global
age = 13 #глобальная переменная
def get_older():# функция изменяющая глобальную переменную
    global age
    age += 1
 
print (age) # напечатает 13
get_older() # увеличиваем age на 1
print (age) # напечатает 14

#8факториал числа
def fact(num):
    if num == 0:
       return 1
    else:
       return num * fact(num - 1)
print(fact(5))

#9
def rectangle_area_finder(a,b):
#коротко и ясно
    return a*b
rectangle_area_finder(15, 3)
print('a*b=',rectangle_area_finder(15,3))

#10мои контакты
def my_contacts(name,age,city,sex):
    print(name)
    print(age)
    print(city)
    print(sex)
my_contacts('Nik', 44,'London','m')
my_contacts('Lora', 24,'Narva','f')
my_contacts('Roman', 14,'Sillamae','m')


 
 
  """

 """   















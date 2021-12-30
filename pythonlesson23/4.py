a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
print(f'Отлично, теперь выберите оператор: "+","-","*","/"')
c=str(input('Введите оператор: '))
if c=="+":
    d=lambda a,b:a+b
elif c=="-":
    d=lambda a,b:a-b
elif c=="*":
    d=lambda a,b:a*b
elif c=="/":
    d=lambda a,b:a/b
else:
    print('Нет такого оператора') 
print(d(a,b))

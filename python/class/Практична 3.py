def max(x,y):
    if x>y: z = x
    else: z =y
    return z
x1 = float(input('x1= '))
x2 = float(input('x2= '))
x3 = float(input('x3= '))
x4 = float(input('x4= '))
m1 = max(x1,x2)
m2 = max(m1,x3)
m = max(m2,x4)
print('Найбільше значення ',m)

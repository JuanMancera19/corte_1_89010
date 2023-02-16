#1 suma o resta

a= float(input('ingrese el primer valor: \n'))
b= float(input('ingrese el segundo valor: \n'))
o= input('que opracion desea hacer suma o resta\n').lower()
if o == 'suma':
    print(a+b)
if o == 'resta':
    print(a-b)

#2 tipo de triangulo

l1 = float(input('ingrese el primer lado:\n'))
l2 = float(input('ingrese el segundo lado:\n'))
l3 = float(input('ingrese el trecer valor:\n'))
if l1==l2==l3:
    print('el triangolo es equilatero')
elif l1==l2 or l1==l3 or l2==l3:
    print('el triangulo es isóseles')
else:
    print('el triangulo es escaleno')

#3 promedio

n1 = float(input('ingrese la nota del corte 1: '))
n2 = float(input('ingrese la nota del corte 2: '))
n3 = float(input('ingrese la nota del corte 3: '))
nf = (n1*0.3)+(n2*0.3)+(n3*0.4)
print(f'la nota final del semestre es: {nf}')
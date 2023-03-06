from math import factorial
print('1: imprimir los numeros inpares desde el 0 al numero escogido.\n2: factorial de un numero.\n3:numeros primos.')
m=int(input('ingrese la opcion en la cual desea: '))
if m==1:
    numero = int(input('ingrese un numero: '))
    if numero <= 0 :
        print('el numero debe ser positivo.')
    else:
        impares = []
        for i in range(1, numero + 1):
            if i % 2 != 0:
                impares.append(i)
        impares_str = ", ".join(str(x) for x in impares)
        print("Los números impares desde el 1 hasta el", numero, "son:", impares_str)

if m==2:
    f= int(input('ingrese el numero para saber el factorial de dicho numero: '))
    if  f>0:
        print(f'el factoria del numero {f} es : {factorial(f)}')
    else:
        print('error el numero no es entero o no es mayor que 0')
if m==3:
    num= int(input('ingrese un numero para saber si es primo o no: '))
    primo = True
    for n in range (2,num):
        if num % n ==0:
            print(f'el numero {num} no es primo.')
            primo=False
            break
    if primo:
        print(f'el numero {num} es primo.')
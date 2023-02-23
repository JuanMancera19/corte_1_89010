#1
a= float(input('ingrese el dato 1: \n'))
b= float(input('ingrese el dato 2: \n'))
print('el residuo de la divicion es: ',a%b)
print('el cosiente de la divicion es: ',a//b)
#2
peso = int(input('ingrese su peso en kg: \n'))
altura = float(input('ingrese su estatura en metros: \n'))
imc1 = peso/(altura**2)
imc= round(imc1,2)
print(f'imc es {imc}')
#3
pp= int(input('ingrese el valor del producto: \n'))
piva= pp+(pp*0.19)
print(f'el valor del producto es {pp}, el valor del producto mas el iva es: {piva}')
#4
distancia = int(input('ingrese la distancia recorrida en km: \n'))
conbustible= int(input(' igrese el valor del conbustible: \n'))
costo_anual = int(input('ingrese el costo promedio del conbustible: \n'))
r= ((distancia*conbustible)/100)*costo_anual
print(f'el costo anual del conbustible es {r}')
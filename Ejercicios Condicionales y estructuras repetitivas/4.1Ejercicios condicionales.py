print("Ejercicio estructura condicional simple:")
print("1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.")

letra1=input("Ingrese la primera letra: ").upper()
letra2=input("Ingrese la segunda letra: ").upper()
if letra1==letra2:
    print("Ambas letras son iguales")
else: 
    print ("Ambas letras son diferentes")

print("2. Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.")

palabra1=input("Ingrese la primera palabra: ").upper()
palabra2=input("Ingrese la segunda palabra: ").upper()
if palabra1==palabra2:
    print("Ambas palabras son iguales")
else: 
    print ("Ambas palabras son diferentes")

print("3.Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.")

genero=input("Ingrese f si su género es femenino o m si es masculino: ")
genero=genero.lower()
if genero=="f":
    print("Vota en mesa femenina")
elif genero=="m":
    print("Vota en mesa masculina")
else: 
    print ("Género no válido. Por favor, ingrese 'f' o 'm'")

print("4. Realice un programa que lea dos números y diga cuál es el mayor.")
número1=float(input("Ingrese un número: "))
número2=float(input("Ingrese otro número: "))
if número1>número2:
    print(str(número1) + " es el mayor")
else: 20
print(str(número2) + " es el mayor")

print("5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.")

monto = float(input("Ingrese el monto de dinero: "))
cambio_día=float(input("Ingrese el valor del dolor al día: "))
cambio = input("Ingresa 'p' si quieres convertir a pesos o 'd' si quieres convertir a dólares: ")
cambio=cambio.lower()
if cambio == "p":
    resultado_p = monto*cambio_día
    print("El monto en pesos es de $ " + str(resultado_p))
elif cambio == "d":
    resultado_d = monto/cambio_día
    print("El monto en dólares es de $ " + str (resultado_d))
else:
    print("Ingrese un cambio válido.")

print("6. Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.")

edad=int(input("Ingrese su edad: "))
if edad>16:
    print("Puede votar")
else: 
    print ("No vota")


print("Ejercicios estructura condicional compuesto (IF anidados)")

print("1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.")

lado1=float(input("Introducir lado1: "))
lado2=float(input("Introducir lado2: "))
lado3=float(input("Introducir lado3: "))
if lado1==lado2==lado3:
  print("El triángulo es equilátero")
elif lado1==lado2 or lado1==lado3 or lado3==lado2:
    print("El triángulo es isóseles")
else:
    print("El triángulo es escaleno")

print("2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago. Mostrar el importe, el descuento o interés y el importe total.:")

importe=float(input("Ingrese el importe: "))
forma_de_pago=int(input("Ingrese la forma de pago presionando 1 si paga de contado, 2 con tarjeta o 3 con débito: "))
if forma_de_pago==1:
    print("Usted pagará $", importe-((importe*10)/100), "porque recibió un descuento del 10% en el monto de su compra por el pago de contado")
elif forma_de_pago==2:
    print("Usted pagará $", importe+((importe*5)/100), "porque se le sumó un interés del 5% en el monto de su compra por el pago con tarjeta")
elif forma_de_pago==3:
    print("Usted pagará $", importe-((importe*5)/100), "porque recibió un del 5% en el monto de su compra por el pago con débito")
else:
    print("Forma de pago inválida")


print("3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.")

número1=float(input("Introducir número1: "))
número2=float(input("Introducir número2: "))
número3=float(input("Introducir número3: "))
if número1>número2 and número1>número3:
   mayor=número1 
elif número2>número1 and número2>número3:
    mayor=número2
else:
    mayor=número3
if mayor % 2 == 0:
    frase= "es par"
else:
    frase = "es impar"

print("El", "número",  (mayor), "es el mayor", "y es", (frase))

print("4. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.")

dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
num = int(input("Ingresa un número del 1 al 7: "))
if num >= 1 and num <= 7:
    print("El día de la semana es:", dias_semana[num-1])

print("5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.")

mes=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
número=int((input("Ingrese un número del 1 al 12: ")))
if número >= 1 and número <= 12:12
print("El mes correspondiente es:", mes [número-1])
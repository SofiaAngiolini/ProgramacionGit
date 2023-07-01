print("Ejercicios estructuras repetitivas")
print ("1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.")

contador_pares = 0
contador_impares = 0
suma_pares = 0

for i in range(4):
    número = int(input("Ingrese un número: "))
    
   
    if número % 2 == 0:
        contador_pares += 1
        suma_pares += número
    else:
        contador_impares += 1

print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)
print("Suma de los números pares:", suma_pares)



print("2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.")

cantidad_mayores = 0
cantidad_menores = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

for i in range(10):
    numero = int(input("Ingrese un número: "))
    
    if numero > 100:
        cantidad_mayores += 1
    elif numero < 100:
        cantidad_menores += 1
    
    if numero > numero_maximo:
        numero_maximo = numero
    if numero < numero_minimo:
        numero_minimo = numero

print("Cantidad de números mayores a 100:", cantidad_mayores)
print("Cantidad de números menores a 100:", cantidad_menores)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)

print("3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.")


cantidad_mujeres = 0
cantidad_varones = 0
cantidad_mayores = 0
cantidad_menores = 0

for i in range(15):
    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese F para femenino o M para masculino: ").upper()

    if sexo == "F":
        cantidad_mujeres += 1
    elif sexo == "M":
        cantidad_varones += 1

    if edad >= 18:
        cantidad_mayores += 1
    else:
        cantidad_menores += 1

print("Cantidad de mujeres:", cantidad_mujeres)
print("Cantidad de varones:", cantidad_varones)
print("Cantidad de mayores de edad:", cantidad_mayores)
print("Cantidad de menores de edad:", cantidad_menores)

print("4.Leer 10 números y mostrar solamente los números positivos, y su sumatoria.")

sumatoria_positivos=0

for i in range(10):
    número = int(input("Ingrese un número: "))
  
    if número>0:
       print(número)
       sumatoria_positivos += número

print("Sumatoria de los números positivos:", sumatoria_positivos)

print("5-Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.")

for i in range(15):
    número = int(input("Ingrese un número negativo: "))
    
    if número<0:
        print(número*-1)
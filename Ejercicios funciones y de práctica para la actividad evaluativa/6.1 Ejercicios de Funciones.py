#1-Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 

def número_aula(aula):
    print("Hola aula", aula, "¿Qué tal?")

número_aula(280)

print("Buen comienzo de clases")

número_aula(280)

print("La semana que viene comenzaremos hablando de las características de Python")

número_aula(280)

print("Hasta la semana que viene")


#2-A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.

def saludo(nombre_1, nombre_2, nombre_3):
    print("Hola", nombre_1 + ",", "" "¿Qué tal?")
    print("Hola", nombre_2 + ",", "" "¿Qué tal?")
    print("Hola", nombre_3 + ",", "" "¿Qué tal?")

saludo("Ana", "Sofia", "Carla")

#3-Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.

def suma(parámetro_1,parámetro_2,parámetro_3):
    total_suma= parámetro_1 + parámetro_2 + parámetro_3

    print("El resultado de la suma de los tres parámetros es:", total_suma)

suma(25,30,40)
suma(25,30,40)

#4-Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE.

def números(número_1,número_2):
    if número_1==número_2:
        print("True")
    else:
        print("False")

números(6,6)


#5-Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(número_1, número_2):
    suma=número_1 + número_2
    resta=número_1 - número_2

    print("El resultado de la suma es:", suma)
    print("El resultado de la resta es:", resta)

sumayresta(3,4)
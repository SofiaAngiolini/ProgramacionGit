#3- Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def total_factura(total_sin_IVA,IVA=21):
    total=(total_sin_IVA*IVA/100) + total_sin_IVA

    print("El total de la factura a abonar más el IVA es de: ", total)

total_factura(2000,)

#4-Escribir una función que convierta un número decimal en los otros dos sistemas: Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.

def convertidor(decimal):
    binario= bin(decimal)[2:]
    hexadecimal= hex(decimal)[2:]

    print("El número decimal es ", decimal)
    print("El número ", decimal , "en binario es ", binario)
    print("El número ", decimal , "en hexadecimal es ", hexadecimal)

decimal=42
convertidor(decimal)

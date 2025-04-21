# Funciones

def convertir_base(numero, base_origen, base_destino):
    # Convertir el número de la base de origen a decimal
    numero_decimal = int(numero, base_origen)
    # Convertir el número decimal a la base de destino
    if base_destino == 2:
        return bin(numero_decimal)[2:]  # Conversión a binario
    elif base_destino == 8:
        return oct(numero_decimal)[2:]  # Conversión a octal
    elif base_destino == 16:
        return hex(numero_decimal)[2:]  # Conversión a hexadecimal
    else:
        # Conversión genérica a cualquier base, a cada cifra lo multiplica por la base
        resultado = ""
        while numero_decimal > 0:
            resultado = str(numero_decimal % base_destino) + resultado
            numero_decimal = numero_decimal // base_destino # division entera
        return resultado

def es_valido_en_base(numero, base):
    try:
        int(numero, base)  # Intenta convertir el número
        return True
    except ValueError:
        return False
    

# Programa principal

valido=False
# Inicio un bucle hasta que se ingrese un numero y base correcta.
while not valido:
    # Solicitar el número y su base
    numero = input("Ingrese el número: ")
    base_origen = int(input("Ingrese la base del número (2, 8, 10, 16): "))
    # Verifico que el número pertenezca a la base, si no es válido, vuelvo a pedir el número y la base 
    valido = es_valido_en_base(numero, base_origen)
    if valido:
        print(f"El número {numero} es válido en la base {base_origen}.")
    else:
        print(f"El número {numero} NO es válido en la base {base_origen}.")

valido=False
while not valido:
    try:
        base_destino = int(input("Ingrese la base a la que desea convertir (2, 8, 10, 16, etc.): "))
        if base_destino>0:
            valido=True
        else:
            print("No es una base a convertir válida")
    except ValueError:
        print("No es una base a convertir válida")
        valido=False    
    

# Realizar la conversión y mostrar el resultado
resultado = convertir_base(numero, base_origen, base_destino)
print(f"El número {numero} en base {base_origen} convertido a base {base_destino} es: {resultado}")
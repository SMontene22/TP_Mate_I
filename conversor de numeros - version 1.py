def convertir_base(numero: str, base_origen: int, base_destino: int) -> str:
    """Convierte un número de una base a otra."""
    # Convertir a base 10
    numero_decimal = int(numero, base_origen)
    
    # Si la base destino es 10, devolver directamente
    if base_destino == 10:
        return str(numero_decimal)
    
    # Convertir de decimal a la base destino
    resultado = ""
    while numero_decimal > 0:
        residuo = numero_decimal % base_destino
        resultado = str(residuo if residuo < 10 else chr(55 + residuo)) + resultado
        numero_decimal //= base_destino
    
    return resultado if resultado else "0"  # Manejo del caso de número '0'


# Ejemplo de uso
numero = input("Introduce el número: ")
base_origen = int(input("Introduce la base de origen: "))
base_destino = int(input("Introduce la base de destino: "))

resultado = convertir_base(numero, base_origen, base_destino)
print(f"El número {numero} en base {base_origen} es {resultado} en base {base_destino}.")
# Ejercicio 5

datos = {}
continuar = True

while continuar:
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in datos:
        print("El nombre ya existe en la agenda.")
    else:
        telefono = input("Ingrese el teléfono del contacto: ")
        datos[nombre] = telefono
        respuesta = input("¿Desea ingresar otro contacto? (s/n): ")
        if respuesta.lower() == "n":
            continuar = False

print("Agenda de contactos:")
print(datos)

buscar_nombre = input("Ingrese el nombre del contacto para buscar su teléfono: ")
if buscar_nombre in datos:
    print("El teléfono de", buscar_nombre, "es", datos[buscar_nombre])
else:
    print("El nombre no se encuentra en nuestros datos.")

# Ejercicio 6


numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numerosUsuario = int(input("Introduce un numero que este entre 0 y 9: "))
posicion = numeros.index(numerosUsuario)
print("El valor ingresado es", numerosUsuario, "los valores de la tupla son: ", posicion)

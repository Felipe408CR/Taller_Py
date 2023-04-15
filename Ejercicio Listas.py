# Ejericicio 1

# lista_colores ["rojo","azul","verde", 'amarillo']
# Los errores de este ejercicio es el = y las comillas de amarillo deben ser dobles y no simples

# lista_colores ["rojo","azul" "verde", 'amarillo']
# print(lista_colores(0))
# Los errores son: falta la , entre azul y verde ademas cuando se especifica una posicion debe de ir [] y no en ()

# lista_colores = ["rojo", "azul", "verde"]
# print(lista_colores[-0]
# print(lista_colores[-4]
# Los errores son en la posicion -0 no eiste dicha posicion ademas hay solo 3 valores y no 4

# Ejericicio 2

colombia = []
departamentos = int(input("Ingrese la cantidad de departamentos a ingresar: "))

for i in range(departamentos):
    departamento = input("Ingrese el nombre del departamento: ")
    colombia.append(departamento)

colombia.sort(reverse=True)

print("Lista de departamentos en orden descendente:")
print(colombia)
print("Los últimos 2 departamentos ingresados fueron:")
print(colombia[-2:])

# Ejercicio 3

numeros = []

while True:
    num = input("Ingrese un numero (o presione Enter sin digitar ningun valor para salir del ciclo): ")
    if num == "":
        break
    numeros.append(int(num))

numerosAscendente = sorted(numeros)
numerosDescendente = sorted(numeros, reverse=True)

print("Los numeros de manera ascendente son:", numerosAscendente)
print("Los numeros de manera descendente son:", numerosDescendente)

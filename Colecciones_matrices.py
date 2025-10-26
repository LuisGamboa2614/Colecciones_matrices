def promedio_lista():
    n = int(input("Ingrese la cantidad de elementos: "))
    lista = []
    for i in range(n):
        num = float(input(f"Ingrese el elemento {i+1}: "))
        lista.append(num)
    promedio = sum(lista) / n
    print("El promedio es:", promedio)


def producto_punto():
    n = int(input("Ingrese el tamaño de las listas: "))
    v = []
    w = []

    print("\nIngrese los elementos de la lista 1:")
    for i in range(n):
        v.append(float(input(f"v[{i}]: ")))

    print("\nIngrese los elementos del arreglo 2:")
    for i in range(n):
        w.append(float(input(f"w[{i}]: ")))

    producto = sum(v[i] * w[i] for i in range(n))
    print("\nEl producto punto es:", producto)


def producto_directo():
    n = int(input("Ingrese el tamaño de las listas: "))
    v = []
    w = []

    print("\nIngrese los elementos de la lista 1:")
    for i in range(n):
        v.append(float(input(f"v[{i}]: ")))

    print("\nIngrese los elementos de la lista 2:")
    for i in range(n):
        w.append(float(input(f"w[{i}]: ")))

    resultado = [v[i] * w[i] for i in range(n)]
    print("\nEl producto directo es:", resultado)


def mediana_lista():
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = []
    for i in range(n):
        num = int(input(f"Ingrese el elemento {i+1}: "))
        arreglo.append(num)

    arreglo.sort()
    print("\nArreglo ordenado:", arreglo)

    if n % 2 == 1:
        mediana = arreglo[n // 2]
    else:
        mediana = (arreglo[n // 2 - 1] + arreglo[n // 2]) / 2

    print("La mediana es:", mediana)


def mover_ceros_final():
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = []
    for i in range(n):
        num = int(input(f"Ingrese el elemento {i+1}: "))
        arreglo.append(num)

    print("\nArreglo original:", arreglo)

    sin_ceros = [x for x in arreglo if x != 0]
    cantidad_ceros = arreglo.count(0)
    resultado = sin_ceros + [0] * cantidad_ceros

    print("Arreglo con ceros al final:", resultado)


def sumar_matrices():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    print("\n--- Matriz A ---")
    A = [[float(input(f"A[{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]

    print("\n--- Matriz B ---")
    B = [[float(input(f"B[{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]

    C = [[A[i][j] + B[i][j] for j in range(columnas)] for i in range(filas)]

    print("\nMatriz resultante (A + B):")
    for fila in C:
        print(fila)


def multiplicar_matrices():
    filas_A = int(input("Ingrese el número de filas de A: "))
    columnas_A = int(input("Ingrese el número de columnas de A: "))
    filas_B = int(input("Ingrese el número de filas de B: "))
    columnas_B = int(input("Ingrese el número de columnas de B: "))

    if columnas_A != filas_B:
        print("\nError: No se pueden multiplicar, columnas de A ≠ filas de B")
        return

    print("\n Matriz A ")
    A = [[float(input(f"A[{i}][{j}]: ")) for j in range(columnas_A)] for i in range(filas_A)]

    print("\n Matriz B ")
    B = [[float(input(f"B[{i}][{j}]: ")) for j in range(columnas_B)] for i in range(filas_B)]

    C = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                C[i][j] += A[i][k] * B[k][j]

    print("\nMatriz resultante (A x B):")
    for fila in C:
        print(fila)


def sumar_columna():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    print("\n Matriz ")
    matriz = [[float(input(f"M[{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]

    col = int(input("\nIngrese el número de columna a sumar (empezando en 0): "))

    if col < 0 or col >= columnas:
        print("Columna fuera de rango.")
        return

    suma = sum(matriz[i][col] for i in range(filas))
    print(f"\nLa suma de la columna {col} es: {suma}")


def matriz_magica():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))

    print("\nIngrese los elementos de la matriz:")
    matriz = [[int(input(f"M[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    suma_magica = sum(matriz[0])

    for i in range(n):
        if sum(matriz[i]) != suma_magica:
            print("\nNo es una matriz mágica (filas no coinciden).")
            return

    for j in range(n):
        suma_columna = sum(matriz[i][j] for i in range(n))
        if suma_columna != suma_magica:
            print("\nNo es una matriz mágica (columnas no coinciden).")
            return

    diagonal1 = sum(matriz[i][i] for i in range(n))
    diagonal2 = sum(matriz[i][n - 1 - i] for i in range(n))

    if diagonal1 != suma_magica or diagonal2 != suma_magica:
        print("\nNo es una matriz mágica (diagonales no coinciden).")
        return

    print("\n La matriz ES MÁGICA.")
    print(f"Suma mágica: {suma_magica}")

def m():
    while True:
        print("\n MENÚ PRINCIPAL ")
        print("1. Calcular el promedio de una lista")
        print("2. Calcular el producto punto de dos listas")
        print("3. Calcular el producto directo de dos listas")
        print("4. Calcular la mediana de una lista")
        print("5. Mover todos los ceros al final de una lista")
        print("6. Sumar dos matrices")
        print("7. Multiplicar dos matrices")
        print("8. Sumar los elementos de una columna de una matriz")
        print("9. Determinar si una matriz es mágica")
        print("10. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            promedio_lista()
        elif opcion == '2':
            producto_punto()
        elif opcion == '3':
            producto_directo()
        elif opcion == '4':
            mediana_lista()
        elif opcion == '5':
            mover_ceros_final()
        elif opcion == '6':
            sumar_matrices()
        elif opcion == '7':
            multiplicar_matrices()
        elif opcion == '8':
            sumar_columna()
        elif opcion == '9':
            matriz_magica()
        elif opcion == '10':
            print("\nPrograma finalizado. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

m()
import os
import random
import time


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def wait_for_key() -> None:
    input("\nPresiona Enter para continuar...")


def factorial_iterativo(numero: int) -> int:
    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


def factorial_recursivo(numero: int) -> int:
    if numero <= 1:
        return 1
    return numero * factorial_recursivo(numero - 1)


def heapify_iterativo(vector: list[int], longitud: int, indice: int) -> None:
    while True:
        mayor = indice
        izquierda = 2 * indice + 1
        derecha = 2 * indice + 2

        if izquierda < longitud and vector[izquierda] > vector[mayor]:
            mayor = izquierda
        if derecha < longitud and vector[derecha] > vector[mayor]:
            mayor = derecha
        if mayor == indice:
            return

        vector[indice], vector[mayor] = vector[mayor], vector[indice]
        indice = mayor


def heap_sort_iterativo(vector: list[int]) -> list[int]:
    resultado = vector.copy()
    longitud = len(resultado)

    for indice in range(longitud // 2 - 1, -1, -1):
        heapify_iterativo(resultado, longitud, indice)

    for indice in range(longitud - 1, 0, -1):
        resultado[0], resultado[indice] = resultado[indice], resultado[0]
        heapify_iterativo(resultado, indice, 0)

    return resultado


def heapify_recursivo(vector: list[int], longitud: int, indice: int) -> None:
    mayor = indice
    izquierda = 2 * indice + 1
    derecha = 2 * indice + 2

    if izquierda < longitud and vector[izquierda] > vector[mayor]:
        mayor = izquierda
    if derecha < longitud and vector[derecha] > vector[mayor]:
        mayor = derecha
    if mayor == indice:
        return

    vector[indice], vector[mayor] = vector[mayor], vector[indice]
    heapify_recursivo(vector, longitud, mayor)


def heap_sort_recursivo(vector: list[int]) -> list[int]:
    resultado = vector.copy()
    longitud = len(resultado)

    for indice in range(longitud // 2 - 1, -1, -1):
        heapify_recursivo(resultado, longitud, indice)

    def extraer_heap(tamano: int) -> None:
        if tamano <= 1:
            return
        resultado[0], resultado[tamano - 1] = resultado[tamano - 1], resultado[0]
        heapify_recursivo(resultado, tamano - 1, 0)
        extraer_heap(tamano - 1)

    extraer_heap(longitud)
    return resultado


def solicitar_entero(mensaje: str, condicion) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if not condicion(valor):
                print("Valor fuera de rango. Intenta nuevamente.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")


def handle_factorial() -> None:
    numero = solicitar_entero(
        "Ingresa el número entero no negativo al que deseas calcular el factorial: ",
        lambda valor: valor >= 0,
    )

    inicio_iterativo = time.perf_counter()
    resultado_iterativo = factorial_iterativo(numero)
    tiempo_iterativo = time.perf_counter() - inicio_iterativo

    print("\nSolución iterativa")
    print(f"Factorial de {numero}: {resultado_iterativo}")
    print(f"Tiempo de ejecución: {tiempo_iterativo:.6f} segundos")

    inicio_recursivo = time.perf_counter()
    resultado_recursivo = factorial_recursivo(numero)
    tiempo_recursivo = time.perf_counter() - inicio_recursivo

    print("\nSolución recursiva")
    print(f"Factorial de {numero}: {resultado_recursivo}")
    print(f"Tiempo de ejecución: {tiempo_recursivo:.6f} segundos")

    wait_for_key()
    clear_screen()


def handle_heap_sort() -> None:
    cantidad = solicitar_entero(
        "Ingresa la cantidad de elementos que debe contener el vector: ",
        lambda valor: valor > 0,
    )

    vector_original = [random.randint(1, 10000) for _ in range(cantidad)]

    print("\nVector original:")
    print(vector_original)

    inicio_iterativo = time.perf_counter()
    resultado_iterativo = heap_sort_iterativo(vector_original)
    tiempo_iterativo = time.perf_counter() - inicio_iterativo

    print("\nSolución iterativa")
    print("Vector ordenado:")
    print(resultado_iterativo)
    print(f"Tiempo de ejecución: {tiempo_iterativo:.6f} segundos")

    inicio_recursivo = time.perf_counter()
    resultado_recursivo = heap_sort_recursivo(vector_original)
    tiempo_recursivo = time.perf_counter() - inicio_recursivo

    print("\nSolución recursiva")
    print("Vector ordenado:")
    print(resultado_recursivo)
    print(f"Tiempo de ejecución: {tiempo_recursivo:.6f} segundos")

    wait_for_key()
    clear_screen()


def mostrar_menu() -> None:
    print("Seleccione la opción deseada")
    print("[1] Calcular Factorial de un Número")
    print("[2] Ordenar Vector mediante Heap sort")
    print("[3] Salir")


def main() -> None:
    while True:
        clear_screen()
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            clear_screen()
            handle_factorial()
        elif opcion == "2":
            clear_screen()
            handle_heap_sort()
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")
            wait_for_key()
            clear_screen()


if __name__ == "__main__":
    main()

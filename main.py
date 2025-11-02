import os
import time

#funcion para limpiar la ventana
def clear_screen():
    # aqui se ve que sistema operativo se ejecuta
    if os.name == 'nt':
        os.system('cls')  # comando si es windows
    else:
        os.system('clear') # comando si es un sistema basado en unix

def factorial_recursivo(g):
  if g == 0 or g == 1:
    return 1
  else:
    return g * factorial_recursivo(g - 1)

# funcion para la operacion iterativa
def caso_1():
    try:
        x = 0

        while x != 2:
            clear_screen()
            num = int(input("ingresa el numero a calcular: "))
            resultado = 1
            i = 1
            #aqui incio el contador para el codifgo 1
            inicio = time.time()
            while i <= num:
                resultado *= i
                i += 1
            fin = time.time()
            print("solucion iterativa")
            print(f"el factorial de {num} es {resultado}")
            print(f"El tiempo que se tomo fue el siguiente: {fin-inicio} milisegundos")
            inicio = time.time()
            factorial_recursivo(num)
            fin = time.time()
            print("solucion recursiva")
            print(f"el factorial de {num} es {resultado}")
            print(f"El tiempo que se tomo fue el siguiente: {fin-inicio} milisegundos")
            x = int(input("si desea conocer el factorial de otro numero pulse 1, si no pulse 2 para salir..."))
    except ValueError:
        print("ingrese un numero entero")
        input("Presiona enter para continuar...")

n = 0
while n !=3:
    try:
        clear_screen()
        print("1 - Factorial de un numero")
        print("2 - ordenenar vector mediante heap sort")
        print("3 - salir")
        n = int(input("ingresa una opcion: "))
        if n == 1:
            caso_1()
        if n == 2:
            print("vectores")
        else:
            print("adios")

    except ValueError:
        print("ingrese un numero entero")
        input("Presiona enter para continuar...")








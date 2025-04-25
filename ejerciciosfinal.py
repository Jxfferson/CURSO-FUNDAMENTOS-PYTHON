#Ejercicio 1

import math
def cal():
  try:
    num1 = int(input("Ingrese el primer numero : "))
    num2 = int(input("Ingrese el segundo numeo : "))
    solicitud = input("Ingrese la operación a realizar :  \n + \n - \n / \n * \n // \n")
    if solicitud == '+':
      respuesta = num1 + num2
    elif solicitud == '-':
      respuesta = num1 - num2
    elif solicitud == '/':
      if num1 == 0 and num2 == 0:
        raise ZeroDivisionError("No se puede dividi por 0")
      respuesta = num1 / num2
    elif solicitud == '*':
      respuesta = num1 * num2
    elif solicitud == '//':
      if num1 == 0 and num2 == 0:
        raise ZeroDivisionError("No se puede dividi por 0")
      respuesta = num1 // num2
    else:
      print("operador no valido")
      return

    print(f"El resultado de la operacion de : {num1} {solicitud} {num2} es = {respuesta}")

  except ValueError:
    print("Error: Ingrese unicamente numeros porfavor.")
  except  ZeroDivisionError:
    print("Error : No se puede dividir por cero.")
  except Exception:
    print("Error: Ocurrio un error inesperado.")

cal()

#Ejercicio 2

def func():
    try:
      productos = {"Arroz":50,"Bananos":34,"Aceite":15,"Fresas":25,"Azucar":34}
      print(f"El inventario inicial es : {productos} \n ")
      del(productos["Aceite"])
      print("Eliminando aceite... \n")
      print(f"El inventario actualizado es : {productos} \n")
      productos['Salmon'] = 25
      del(productos["Arroz"])
      print("Producto Salmon agregado con 25 unidades. Eliminando Arroz. \n")
      print(f"El inventario actualizado es : {productos} \n")
      productos['Salmon'] = 35
      print("Actualizando stock de Salmon a 35 \n")
      print(f"El invetario actualizado es : {productos} \n")
    except ValueError:
      print("Error: El elemento seleccionado no se encuentra en el diccionario \n")
func()

#Ejercicio 3

def analizar_texto():
    try:
        texto = input("Ingrese un texto: ").strip()
        if not texto:
            print("No ingresaste ningún texto.")
            return

        for signo in ",.;:!?\"'":
            texto = texto.replace(signo, "")

        palabras = texto.lower().split()
        frecuencia = {}

        for palabra in palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

        print("Frecuencia de palabras:")
        for palabra, cantidad in frecuencia.items():
            print(f"{palabra}: {cantidad}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

analizar_texto()

#Ejercicio 4


def conversor():
    print("1. Centímetros a pulgadas\n2. Kilómetros a millas")
    opcion = input("Opción: ")

    try:
        valor = float(input("Cantidad a convertir: "))
        if valor < 0:
            print("Solo se permiten valores positivos.")
            return

        if opcion == "1":
            print(f"{valor} cm = {valor * 0.3937:.2f} pulgadas")
        elif opcion == "2":
            print(f"{valor} km = {valor * 0.6214:.2f} millas")
        else:
            print("Opción no válida.")

    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

conversor()

#Ejercicio 5

import random

def adivina_el_numero():
    print('¡Bienvenido al juego "Adivina el Número"!')
    print("Estoy pensando en un número entre 1 y 50.\n")

    numero_secreto = random.randint(1, 50)
    intento = 1
    print(f"{numero_secreto}")

    while True:
      try:
        entrada = int(input(f"Intento N {intento} - Ingrese un numero entre 1 y 50 : "))
        num = int(entrada)
        if num < 0 or num > 50:
          print("Error : El numero que usted ha ingresado esta fuera de rango.")
        if num > numero_secreto:
          print("El numero que has ingresado es mayor al numero secreto")
        elif num < numero_secreto:
          print("El numero que has ingresado es menor al numero secreto")
        else:
          print(f"Felicidades, encontraste el numero ganador {numero_secreto}")

        intento += 1
        break
      except ValueError:
        print("Ha ingresado un caracter mal")

adivina_el_numero()

#Ejercicio 6

def calfunc():
  while True:
    try:
      numero = int(input("Ingrese un numero ENTERO : "))

      if numero < 0:
        print("Ingrese un numero entero")
        return

      factorial = 1
      for x in(1, numero + 1):
        factorial *= x

      print(f"El factorial de {numero} es {factorial}")

    except ValueError:
      print("Error: Ha ingresado un dato incorrecto")

calfunc()


#Ejercicio 7

def calcular_dias_faltantes():
    import datetime

    fecha_ingresada = input("Ingrese una fecha (DD/MM/AAAA): ")

    try:
        # Convertimos la cadena a fecha
        fecha_objetivo = datetime.datetime.strptime(fecha_ingresada, "%d/%m/%Y").date()
        hoy = datetime.date.today()

        # Calculamos la diferencia
        diferencia = (fecha_objetivo - hoy).days

        # Mostramos el resultado según si la fecha ya pasó o está en el futuro
        if diferencia > 0:
            print(f"Faltan {diferencia} días para el {fecha_ingresada}.")
        elif diferencia == 0:
            print(f"¡La fecha {fecha_ingresada} es hoy!")
        else:
            print(f"La fecha {fecha_ingresada} ya pasó hace {-diferencia} días.")

    except ValueError:
        print("Formato de fecha incorrecto. Debes usar DD/MM/AAAA.")

#Ejercicio 8

registro_estudiantes = {'Ana': 90, 'Luis': 78, 'Carlos': 85}

def agregar_estudiante(): #Declaración de la función para agregar estudiantes
    nombre = input("Ingrese el nombre del estudiante: ") #Solicitar el nombre del estudiante
    try: #Manejo de excepciones para la calificación
        calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
        registro_estudiantes[nombre] = calificacion
        print(f"Estudiante agregado: {nombre} - {calificacion}")
    except ValueError: #Excepción para calificación no válida
        print("Error: La calificación debe ser un número válido.") # Manejo de excepciones para la calificación

def actualizar_calificacion(): #Declaración de la función para actualizar calificaciones
    nombre = input("Ingrese el nombre del estudiante: ") #Solicitar el nombre del estudiante
    if nombre in registro_estudiantes: #Verificar si el estudiante existe
        try:
            nueva_calificacion = float(input(f"Ingrese la nueva calificación para {nombre}: ")) #Solicitar nueva calificación
            registro_estudiantes[nombre] = nueva_calificacion #Actualizar la calificación
            print(f"Estudiante actualizado: {nombre} - {nueva_calificacion}") #Mostrar la nueva calificación
        except ValueError: #Excepción para calificación no válida
            print("Error: La calificación debe ser un número válido.")
    else:
        print("Error: El estudiante no existe.")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in registro_estudiantes:
        del registro_estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print("Error: El estudiante no existe.")

def listar_estudiantes():
    if registro_estudiantes:
        print("Registro de estudiantes:")
        for nombre, calificacion in registro_estudiantes.items():
            print(f"{nombre}: {calificacion}")
    else:
        print("No hay estudiantes registrados.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Actualizar calificación")
        print("3. Eliminar estudiante")
        print("4. Listar estudiantes")
        print("5. Salir")

        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                agregar_estudiante()
            elif opcion == 2:
                actualizar_calificacion()
            elif opcion == 3:
                eliminar_estudiante()
            elif opcion == 4:
                listar_estudiantes()
            elif opcion == 5:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entre 1 y 5.")

# Ejecutar el menú
menu()

#Ejercicio 9

import random
import string

def contraseña():
  while True:
    try:
      caract = int(input("Ingrese el numero de caracteres que desea que tenga su contraseña : "))
      if caract <= 0:
        print("Ingrese un numero valido.")

      caracteres = string.ascii_letters + string.digits + string.punctuation
      contraseña = ''.join(random.choice(caracteres) for _ in range(caract))

      print(f"Su contraseña es : {contraseña}")

    except ValueError:
      print("Error: Ha ingresado un dato de forma incorrecta, intentelo nuevamente.")

contraseña()
 
#Ejercicio 10

import os
def buscar_archivos():
    try:
        # Se pide la ruta del directorio y la subcadena al usuario
        ruta_directorio = input("Ingrese la ruta del directorio: ")
        subcadena = input("Ingrese la subcadena a buscar: ")

        if not os.path.isdir(ruta_directorio):
            print("Error: El directorio no existe o no es un directorio válido.")
            return

        # Se lista todos los archivos en el directorio
        archivos = os.listdir(ruta_directorio) 

        # Se filtran los archivos que contienen la subcadena
        archivos_encontrados = [archivo for archivo in archivos if subcadena in archivo]

        if archivos_encontrados:
            print(f"Archivos encontrados que contienen \"{subcadena}\":")
            for archivo in archivos_encontrados:
                print(archivo)
        else:
            print(f"No se encontraron archivos que contengan \"{subcadena}\".")

    except PermissionError:
        print("Error: No tienes permisos suficientes para acceder al directorio.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutamos la funcion la función
buscar_archivos()
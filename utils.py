import os
import datetime
import tkinter as tk
from tkinter import filedialog

def limpiar_consola():
    os.system("cls")

def imprimir_pantalla_inicio():
    limpiar_consola()
    ancho = 60  # Ancho total del marco
    mensaje_inicio = "Bienvenido a Cuentas Claras Conservan la amistad"
    padding = int((ancho - len(mensaje_inicio) - 2)/ 2) # Relleno en blanco a los costados del mensaje

    # Primeras linea en blanco
    print("\n" * 2)

    # Imprimir el marco superior
    print('*' * ancho)

    # Imprimir la línea con el mensaje centrado
    print(f'*{" " * padding}{mensaje_inicio}{" " * padding}*')

    # Imprimir la línea vacía
    print(f'*{" " * (ancho - 2)}*')

    # Imprimir el marco inferior
    print('*' * ancho)

def Solicitartxt():
    return input("SELECCIONE 1 PARA IMPRIMIR DETALLE EN TXT:")

def ArmarTXT(texto):
    root = tk.Tk()
    root.withdraw()
    direccion = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Archivos de texto", "*.txt"),
            ("Todos los archivos", "*.*")
        ]
    )
    if direccion: 
        with open(direccion, 'w') as file:
            file.write(texto)
    root.destroy() 


def esperar_enter():
    input("\nPRESIONE ENTER PARA CONTINUAR.\n")

def crear_grupo(grupos_dic):
    nombre_grupo = input("Ingrese el nombre del grupo a crear: ")
    if nombre_grupo not in grupos_dic:
        grupos_dic[nombre_grupo] = {} # Se agrega el primer elemento del diccionario con el nombre del grupo y su valor es otro diccionario vacio
        print(f"\nGrupo {nombre_grupo} creado con exito.")
    else:
        print(f"\nEl grupo ya existe.")
    esperar_enter()

def mostrar_grupos(grupos_dic):
    limpiar_consola()
    for i, nombre_grupo in enumerate(grupos_dic, 1):
        print(f"{i}. {nombre_grupo}")

def mostrar_integrantes(grupos_dic, nombre_grupo):
    if grupos_dic[nombre_grupo]:
        for i, integrante in enumerate(grupos_dic[nombre_grupo], 1):
            print(f"{i}. {integrante}")
    else:
        print("No hay integrantes en el grupo")

def seleccionar_grupo(grupos_dic):
    if not grupos_dic:
        print("\nNo hay ningun grupo creado")
        esperar_enter()
    else:
        mostrar_grupos(grupos_dic)
        eleccion = int(input("\nIngrese el numero del grupo a elegir: ")) - 1
        if eleccion < 0 or eleccion > len(grupos_dic): # Se revisa que el numero ingresado este dentro del rango de grupo existente
            print("\nSELECCION INVALIDA\n")
            return None
        else:
            nombre_grupo = list(grupos_dic.keys())[eleccion] # Se debe castear a lista para acceder al indice numerico
            return nombre_grupo
        
def ingresar_gasto(nombre_grupo, nombre_integrante, grupos_dic):
    try:
        gasto = float(input(f"Ingrese el gasto de {nombre_integrante}: "))
        concepto = input(f"Concepto del gasto: ")
        grupos_dic[nombre_grupo][nombre_integrante].append((gasto, concepto)) # Se guarda una tupla con el gasto y el concepto del mismo
        print(f"\nGasto de ${gasto} por {concepto} agregado a {nombre_integrante}")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")
    finally:
        esperar_enter()

def integrante_nuevo(nombre_grupo, grupos_dic):
    nombre_integrante = input("Ingrese el nombre del integrante: ")
    if nombre_integrante in grupos_dic[nombre_grupo]:
        print(f"\nEl integrante {nombre_integrante} ya existe en el grupo {nombre_grupo}")
    else:
        grupos_dic[nombre_grupo][nombre_integrante] = [] # Se agrega la key al segundo diccionario y su valor sera una lista vacia a llenar con los gastos realizados
        print(f"\nIntegrante {nombre_integrante} agregado al grupo {nombre_grupo}.")
    esperar_enter()

def calcular_deudas(diccionario):
    # Calcular los totales de cada persona
    totales = {persona: sum(gasto[0] for gasto in lista_gastos) for persona, lista_gastos in diccionario.items()}
    
    # Calcular el total gastado por el grupo y el promedio por persona
    total_gastado = sum(totales.values())
    num_personas = len(diccionario)
    promedio = total_gastado / num_personas

    print(f"\nTotal gastado por el grupo: {total_gastado:.2f}\n")
    print(f"Promedio de gasto por persona: {promedio:.2f}")
    
    # Determinar quiénes pagaron menos y quiénes pagaron más que el promedio
    deudores = []
    acreedores = []

    print("\nTotales de cada persona:\n")        
    for persona, total in totales.items():
        print(f"{persona} ha puesto un total de: {total:.2f}")
        diferencia = total - promedio
        if diferencia < 0:  # Pagó menos de lo que debería
            deudores.append((persona, -diferencia))  # La cantidad que debe (se guarda en positivo)
        elif diferencia > 0:  # Pagó más de lo que debería
            acreedores.append((persona, diferencia))  # La cantidad que se le debe
    
    # Procesar los pagos
    print("\nDeudas entre participantes:\n")
    while deudores and acreedores:
        deudor, deuda = deudores.pop(0)
        acreedor, credito = acreedores.pop(0)
        
        if deuda > credito:
            # El deudor debe más de lo que el acreedor tiene que recibir
            print(f"{deudor} le debe a {acreedor} {credito:.2f}")
            deudores.insert(0, (deudor, deuda - credito))  # El deudor sigue debiendo la diferencia
        elif deuda < credito:
            # El acreedor tiene que recibir más de lo que el deudor debe
            print(f"{deudor} le debe a {acreedor} {deuda:.2f}")
            acreedores.insert(0, (acreedor, credito - deuda))  # El acreedor sigue con saldo positivo
        else:
            # La deuda es exactamente igual al crédito
            print(f"{deudor} le debe a {acreedor} {deuda:.2f}")
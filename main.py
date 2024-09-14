def imprimir_pantalla_inicio():
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

    print("\nOpciones:")
    print("1. Crear un nuevo grupo")
    print("2. Seleccionar grupo")
    print("3. Salir\n")

def esperar_enter():
    input("\nPRESIONE ENTER PARA CONTINUAR.\n")

def crear_grupo(grupos_dic):
    nombre_grupo = input("Ingrese el nombre del grupo a crear: ")
    if nombre_grupo not in grupos_dic:
        grupos_dic[nombre_grupo] = {}
        print(f"\nGrupo {nombre_grupo} creado con exito.")
    else:
        print(f"\nEl grupo ya existe.")
    esperar_enter()

def mostrar__grupos(grupos_dic):
    for i, nombre_grupo in enumerate(grupos_dic, 1):
        print(f"{i}. {nombre_grupo}")

def seleccionar_grupo(grupos_dic):
    if not grupos_dic:
        print("\nNo hay ningun grupo creado")
        esperar_enter()
    else:
        mostrar__grupos(grupos_dic)
        eleccion = int(input("\nIngrese el numero del grupo a elegir: ")) - 1
        # Se revisa que el numero ingresado este dentro del rango de grupo existente
        if eleccion < 0 or eleccion > len(grupos_dic):
            print("\nSELECCION INVALIDA\n")
            return None
        else:
            nombre_grupo = list(grupos_dic.keys())[eleccion]
            print(f"SE SELECCIONO: {nombre_grupo}")
            return nombre_grupo
        
def ingresar_gasto(nombre_grupo, nombre_integrante, grupos_dic):
    try:
        gasto = float(input(f"Ingrese el gasto de {nombre_integrante}: "))
        grupos_dic[nombre_grupo][nombre_integrante].append(gasto)
        print(f"Gasto de ${gasto} agregado a {nombre_integrante}")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

def integrante_nuevo(nombre_grupo, grupos_dic):
    nombre_integrante = input("Ingrese el nombre del integrante: ")
    if nombre_integrante in grupos_dic[nombre_grupo]:
        print(f"\nEl integrante {nombre_integrante} ya existe en el grupo {nombre_grupo}")
    else:
        grupos_dic[nombre_grupo][integrante_nuevo] = [] # se agrega lista vacia que serian los gastos
        print(f"\nIntegrante {nombre_integrante} agregado al grupo {nombre_grupo}.")

    ingresar_gasto(nombre_grupo, nombre_integrante, grupos_dic)
    esperar_enter()
 
def administrar_grupo(nombre_grupo, grupos_dic):
    mostrar_pantalla_administrar = True
    while mostrar_pantalla_administrar:
        print("\n1. Ingresar integrante  y gasto")
        print("2. Ver gastos del grupo")
        print("3. Atras")
        eleccion = int(input("\nSeleccione una opcion (1, 2 o 3): "))
        if eleccion == 1:
            integrante_nuevo(nombre_grupo, grupos_dic)
        else:
            print("\nOpción invalida.")
            esperar_enter()

def main():
    mostrar_pantalla_inicio = True # Bandera para controlar el While
    grupos = {} # Diccionario vacio con los grupos que se van a crear. El nombre del grupo sera la key

    while mostrar_pantalla_inicio:
        imprimir_pantalla_inicio()

        try:
            opcion_elegida = int(input("Seleccione una opción (1, 2 o 3): "))
            if opcion_elegida == 1:
                crear_grupo(grupos)
            elif opcion_elegida == 2:
                nombre_grupo = seleccionar_grupo(grupos)
                if nombre_grupo:
                    administrar_grupo(nombre_grupo, grupos)
            elif opcion_elegida == 3:
                print(grupos)
                #mostrar_pantalla_inicio = False
            else:
                print("\nOpción invalida. Por favor, selecciona 1 o 2.")
                esperar_enter()
        except Exception as e:
            print("\nEntrada invalida. Por favor ingrese un numero entero.")
            print(e)
            esperar_enter()
            
if __name__ == "__main__":
    main()  
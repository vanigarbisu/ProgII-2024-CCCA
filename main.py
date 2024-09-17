from utils import *

def administrar_grupo(nombre_grupo, grupos_dic):
    mostrar_pantalla_administrar = True

    while mostrar_pantalla_administrar:
        limpiar_consola()
        print(f"{nombre_grupo} - Integrantes: ")
        mostrar_integrantes(grupos_dic, nombre_grupo)

        print(f"\nOpciones:")
        print("\n1. Integrante nuevo")
        print("2. Gasto nuevo")
        print("3. Ver gastos del grupo")
        print("4. Atras")

        eleccion = int(input("\nSeleccione una opcion (1, 2 o 3): "))

        if eleccion == 1:
            integrante_nuevo(nombre_grupo, grupos_dic)
        elif eleccion == 2:
            if not grupos_dic[nombre_grupo]:
                print("No hay integrantes a quienes agregar gastos.")
                esperar_enter()
            else:
                limpiar_consola()
                mostrar_integrantes(grupos_dic, nombre_grupo)
                eleccion_integrante = int(input("\nIngrese el numero del integrante para agregar gasto: ")) - 1
                if eleccion_integrante < 0 or eleccion_integrante > len(grupos_dic[nombre_grupo]): # Se revisa que el numero ingresado este dentro del rango de grupo existente
                    print("\nSELECCION INVALIDA\n")
                    esperar_enter()
                else:
                    nombre_integrante = list(grupos_dic[nombre_grupo])[eleccion_integrante]
                    ingresar_gasto(nombre_grupo, nombre_integrante, grupos_dic)
        elif eleccion == 3: # Se ve el diccionario completo, hay que meterle logica de total, division, etc
            print()
            print("Detalle de gastos:\n")
            print(grupos_dic[nombre_grupo])
            calcular_deudas(grupos_dic[nombre_grupo])
            esperar_enter()
        elif eleccion == 4:
            mostrar_pantalla_administrar = False
        else:
            print("\nOpción invalida.")
            esperar_enter()

def main():
    mostrar_pantalla_inicio = True # Bandera para controlar el While
    grupos = {} # Diccionario vacio con los grupos que se van a crear. El nombre del grupo sera la primera key

    while mostrar_pantalla_inicio:
        imprimir_pantalla_inicio()

        print("\nOpciones:")
        print("1. Crear un nuevo grupo")
        print("2. Seleccionar grupo")
        print("3. Salir\n")
        
        try:
            opcion_elegida = int(input("Seleccione una opción (1, 2 o 3): "))
            if opcion_elegida == 1:
                crear_grupo(grupos)
            elif opcion_elegida == 2:
                nombre_grupo = seleccionar_grupo(grupos)
                if nombre_grupo:
                    print(f"SE SELECCIONO: {nombre_grupo}")
                    administrar_grupo(nombre_grupo, grupos)
            elif opcion_elegida == 3:
                print(grupos) # para chequear, sacar despues
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
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_archivo(nombre_archivo, sufijo, desde, hasta):
    print(f"\nGenerando archivo: {nombre_archivo}")
    with open(nombre_archivo, "a") as archivo:
        for i in range(desde, hasta):
            archivo.write(f"{sufijo}{i}\n")
    print("Archivo generado exitosamente.\n")

def opcion_hombre():
    archivo = "PersoFiber_hombre.txt"
    if not os.path.exists(archivo):
        print("Archivo para hombres no encontrado. Creando...")
        generar_archivo(archivo, "004", 1000000, 6000000)
    else:
        print(f"El archivo '{archivo}' ya existe. No se generó uno nuevo.")
    volver_al_menu()

def opcion_mujer():
    archivo = "PersoFiber_mujer.txt"
    if not os.path.exists(archivo):
        print("Archivo para mujeres no encontrado. Creando...")
        generar_archivo(archivo, "014", 1000000, 6000000)
    else:
        print(f"El archivo '{archivo}' ya existe. No se generó uno nuevo.")
    volver_al_menu()

def opcion_personalizada():
    print("\n--- Generador Personalizado ---")

    while True:
        sufijo = input("Ingrese un sufijo de 3 dígitos (ej: 123): ").strip()
        if sufijo.isdigit() and len(sufijo) == 3:
            break
        print("Sufijo inválido. Debe contener exactamente 3 números.")

    try:
        desde = int(input("Número desde donde comenzar: "))
        hasta = int(input("Número hasta donde finalizar: "))
        if desde >= hasta:
            print("El número final debe ser mayor que el inicial.")
            return volver_al_menu()
    except ValueError:
        print("Debe ingresar valores numéricos válidos.")
        return volver_al_menu()

    nombre_archivo = input("Nombre del archivo de salida (vacío para 'PersoFiber-default.txt'): ").strip()
    if nombre_archivo == "":
        nombre_archivo = "PersoFiber-default.txt"

    if os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' ya existe. No se generó uno nuevo.")
    else:
        generar_archivo(nombre_archivo, sufijo, desde, hasta)

    volver_al_menu()

def volver_al_menu():
    input("\nPresione Enter para volver al menú principal...")
    main()

def main():
    limpiar_pantalla()

    print("================================================")
    print("                 PersoFiber")
    print(" Generador de diccionarios Fibertel/Personal")
    print("================================================\n")

    print("Seleccione una opción:")
    print("  1 - Generar diccionario para Hombres")
    print("  2 - Generar diccionario para Mujeres")
    print("  3 - Crear diccionario personalizado")
    print("  0 - Salir")

    try:
        seleccion = int(input("\nIngrese su elección: "))
        if seleccion == 1:
            opcion_hombre()
        elif seleccion == 2:
            opcion_mujer()
        elif seleccion == 3:
            opcion_personalizada()
        elif seleccion == 0:
            print("\nGracias por usar PersoFiber. Hasta luego.")
            input("Presione Enter para cerrar el programa...")
        else:
            print("Opción inválida. Intente nuevamente.")
            volver_al_menu()
    except ValueError:
        print("Debe ingresar un número válido.")
        volver_al_menu()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nSe produjo un error inesperado: {e}")
        input("Presione Enter para cerrar el programa...")

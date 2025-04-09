
# PersoFiber

**PersoFiber** es una herramienta interactiva en Python para generar diccionarios de texto con patrones personalizados, especialmente diseñados para simular contraseñas comunes utilizadas por clientes de servicios como Fibertel o Personal.

## Características

- Generación rápida de diccionarios con sufijos predeterminados para hombres (`004`) y mujeres (`014`).
- Opción para crear diccionarios personalizados con sufijos y rangos definidos por el usuario.
- Comprobación de existencia de archivos para evitar sobrescritura accidental.
- Interfaz de consola intuitiva.

## Uso

Al ejecutar el script, se presenta un menú con las siguientes opciones:

1. **Generar diccionario para Hombres:** Crea un archivo llamado `PersoFiber_hombre.txt` con entradas desde `0041000000` hasta `0045999999`.
2. **Generar diccionario para Mujeres:** Crea un archivo llamado `PersoFiber_mujer.txt` con entradas desde `0141000000` hasta `0145999999`.
3. **Crear diccionario personalizado:** El usuario puede elegir un sufijo de 3 dígitos y definir el rango numérico.
0. **Salir:** Cierra el programa.

## Requisitos

- Python 3.x
- Sistema operativo compatible con `os.system('cls'/'clear')` (Windows/Linux/macOS)

## Ejecución

```bash
python3 perso_fiber.py
```

## Notas

- Los archivos generados se guardan en el mismo directorio donde se ejecuta el script.
- Si el archivo ya existe, no se sobrescribirá.

## Licencia

Este script es de uso libre para propósitos educativos.

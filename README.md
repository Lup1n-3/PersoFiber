# PersoFiber

**PersoFiber** es una herramienta interactiva escrita en Python que permite generar diccionarios de texto con patrones personalizados, ideal para escenarios donde se simulan contraseñas o identificadores similares a los usados por clientes de Fibertel o Personal.

## Características

- Generación de diccionario para hombres con el sufijo `004`.
- Generación de diccionario para mujeres con el sufijo `014`.
- Modo personalizado: el usuario define su propio sufijo y rango numérico.
- Opción para crear un archivo combinado (hombres + mujeres).

## Uso

Al ejecutar el script, se presenta un menú con las siguientes opciones:

1. Generar diccionario para Hombres  
   Crea `PersoFiber_hombre.txt` con combinaciones desde `0041000000` hasta `0045999999`.

2. Generar diccionario para Mujeres  
   Crea `PersoFiber_mujer.txt` con combinaciones desde `0141000000` hasta `0145999999`.

3. Crear diccionario personalizado  
   El usuario define un sufijo de 3 dígitos y el rango numérico de inicio y fin.

4. Generar diccionario combinado  
   Crea `PersoFiber_combinado.txt` con sufijos `004` y `014` en el mismo archivo.

0. Salir  
   Cierra el programa.

## Requisitos

- Python 3.x
- Compatible con Windows, Linux o macOS  
  (el script usa `os.system('cls'/'clear')` dependiendo del sistema operativo)

## Ejecución

```bash
python3 PersoFiber.py

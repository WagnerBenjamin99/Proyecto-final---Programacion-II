import requests
import json
from os import system


with open("directores.json", encoding='utf-8') as json_:
    directores = json.load(json_)
generos = ["Drama", "Terror", "Accion", "Psicologico", "Aventura", "Ficcion"]

while True:
    menu_principal="""
[1] Iniciar sesion
[2] Continuar sin inicar sesion
[3] Salir
    """
    print(menu_principal)

    opcion = int(input('Ingrese opcion: '))

    if opcion == 3:
        break
    elif opcion == 2:
        resp = requests.get('http://127.0.0.1:5000/')
        respuesta = resp.json()

        for pelicula in respuesta:
            for i, j in pelicula.items():
                print(i.upper(), ' : ', j)
            print('\n\n')
    elif opcion == 1:
        nombre = input('Ingrese su nombre de usuario: ')
        contraseña=input('Ingrese su contraseña: ')
        data = {'nombre_usuario':nombre,'contraseña':contraseña}

        respuesta1 = requests.post('http://127.0.0.1:5000/login', json=data)

      
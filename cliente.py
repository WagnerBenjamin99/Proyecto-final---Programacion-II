import json
from os import system
import requests
from colorama import init, Fore, Back

init(autoreset=True)

menu_principal="""
[1] Iniciar sesion
[2] Continuar sin inicar sesion
[3] Salir
"""

menu_registrado="""
[1] Eliminar pelicula
[2] Editar pelicula
[3] Agregar pelicula
[4] Cerrar sesion
"""

menu_edicion="""
[1] Editar titulo
[2] Editar genero
[3] Editar fecha
[4] Editar portada
[5] Editar sinopsis
"""


while True:

    print(Fore.GREEN + menu_principal)

    opcion = int(input(Fore.MAGENTA +'Ingrese opcion: '))

    if opcion == 3:
        break
    elif opcion == 2:
        resp = requests.get('http://127.0.0.1:5000/')
        print(resp)
        
        respuesta = resp.json()
        for pelicula in respuesta:
            for i, j in pelicula.items():
                if i =='id_genero':
                    generos = requests.get('http://127.0.0.1:5000/generos').json()
                    for genero in generos:
                        if j == genero['id_genero']:
                            print(Back.WHITE + Fore.BLUE+  'GENERO', ' : ' , Fore.BLUE + genero['genero'])
                else:       
                    print(Back.WHITE + Fore.BLUE+  i.upper(), ' : ' , Fore.BLUE + str(j))
            print('\n\n')
        Back.RESET
        
    elif opcion == 1:
        nombre = input(Fore.MAGENTA + 'Ingrese su nombre de usuario: ')
        contraseña=input(Fore.MAGENTA + 'Ingrese su contraseña: ')
        data = {'nombre_usuario':nombre,'contraseña':contraseña}

        respuesta1 = requests.post('http://127.0.0.1:5000/login', json=data)

        if respuesta1.status_code != 200:
            system('cls')
            print(Fore.RED + 'Usuario no registrado')
            continue
      

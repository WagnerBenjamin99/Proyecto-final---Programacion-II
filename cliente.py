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
        else:
            system('cls')
            id_sesion = respuesta1.json()['id_usuario']
            print(Fore.YELLOW + 'Bienvenido ' + nombre + '!!')
            while(True):
                print(Fore.GREEN + menu_registrado)
                
                opcion1=0
                opcion1 = int(input(Fore.MAGENTA + 'Ingrese opcion: '))
                if opcion1 == 4:
                    system('cls')
                    break
                elif opcion1 == 1:
                    system('cls')
                    print('Peliculas disponibles:\n')
                    
                    respuesta = requests.get('http://127.0.0.1:5000/').json()
                    for pelicula in respuesta:
                        print(Fore.GREEN + str(pelicula['id_pelicula']), '-', Fore.BLUE + pelicula['titulo'])
                        
                    id = int(input('Seleccione la pelicula que desea elimiar: '))
                    datos_delete={"id_pelicula": id, "id_sesion":id_sesion}
                    respuesta3 = requests.delete('http://127.0.0.1:5000/eliminar', json=datos_delete)
                    if respuesta3.status_code != 200:
                        system('cls')
                        print(Fore.RED + 'No puede eliminar esta pelicula porque contiene comentario de otros usuarios')
                    else:
                        system('cls')
                        print(Fore.GREEN + 'Pelicula eliminada con exito')
                elif opcion1 == 2:
                    system('cls')
                    print('Peliculas disponibles:\n')
                    
                    respuesta = requests.get('http://127.0.0.1:5000/').json()
                    for pelicula in respuesta:
                        print(Fore.GREEN + str(pelicula['id_pelicula']), '-', Fore.BLUE + pelicula['titulo'])
                    id = int(input('Seleccione la pelicula que desea editar: '))
                    
                    datos_edicion={}
                    
                    print(Fore.GREEN + menu_edicion)
                    
                    edicion= int(input(Fore.MAGENTA + 'Seleccione campo a editar: '))
                    if edicion == 1:
                        system('cls')
                        actualizado=input(Fore.MAGENTA + 'Ingrese el titulo: ')
                        datos_edicion={"id_pelicula":id, "titulo":actualizado}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    elif edicion == 2:
                        system('cls')
                        generos = requests.get('http://127.0.0.1:5000/generos').json()
                        for genero in generos:
                            print(Fore.RED + str(genero['id_genero']), Fore.GREEN + genero['genero'])
                        actualizado = int(input(Fore.MAGENTA + 'Seleccione el genero: '))

                        for genero in generos:
                            if genero['id_genero'] == actualizado:
                                datos_edicion={"id_pelicula":id, "id_genero": genero['id_genero']}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    elif edicion == 3:
                        system('cls')
                        actualizado=input(Fore.MAGENTA + 'Ingrese el año: ')
                        datos_edicion={"id_pelicula":id, "año":actualizado}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    elif edicion == 4:
                        system('cls')
                        actualizado=input(Fore.MAGENTA + 'Ingrese la portada: ')
                        datos_edicion={"id_pelicula":id, "portada":actualizado}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    elif edicion == 5:
                        system('cls')
                        actualizado=input(Fore.MAGENTA + 'Ingrese la sinopsis: ')
                        datos_edicion={"id_pelicula":id, "sinopsis":actualizado}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    elif edicion == 6:
                        directores=requests.get('http://127.0.0.1:5000/directores')
                        for director in directores:
                            print(director["id_director"], " - ", director["nombre"])

                        director_seleccionado = int(input(Fore.MAGENTA + 'Seleccione el genero: '))
                        datos_edicion={'id_director':director_seleccionado}
                        respuesta = requests.put('http://127.0.0.1:5000/editar', json=datos_edicion).json()
                    else:
                        system('cls')
                        print(Fore.RED + 'Opcion incorrecta')
                        continue 

                elif opcion1 == 3:
                    datos={}

                    directores=requests.get('http://127.0.0.1:5000/directores').json()

                    datos['titulo'] = input("Ingrese el titulo: ")        
                    datos['año'] = input('Ingrese el año: ')
                    
                    generos = requests.get('http://127.0.0.1:5000/generos').json()
                    for genero in generos:
                            print(Fore.RED + str(genero['id_genero']), Fore.GREEN + genero['genero'])

                    genero_seleccionado = int(input(Fore.MAGENTA + 'Seleccione el genero: '))

                    for genero in generos:
                        if genero['id_genero'] == genero_seleccionado:
                            datos['id_genero'] = genero['id_genero']

                    datos['sinopsis']=input(Fore.MAGENTA + 'Ingrese la sinopsis: ')
                    
                    for director in directores:
                        print(director["id_director"], " - ", director["nombre"])
                    
                    director= int(input(Fore.MAGENTA + 'Seleccione el director: '))
                    datos["id_director"] = director 
                    portada = input(Fore.MAGENTA + 'Ingrese la portada: ')
                    datos['portada'] = portada
                    comentario=int(input(Fore.GREEN + 'Si desea agregar una opinion personal ingrese [1] de lo contrario ingrese [2]: '))
                    if comentario == 2:
                        respuesta = requests.post('http://127.0.0.1:5000/agregar', json=datos).json()
                    else:
                        comentario=input(Fore.MAGENTA + 'Ingrese su opinion sobre esta pelicula: ')
                        datos['comentario']=comentario
                        respuesta = requests.post('http://127.0.0.1:5000/agregar', json=datos).json()
                else:
                    print(Fore.RED +'Opcion incorrecta')
                    continue
    else:
        system('cls')
        print(Fore.RED + 'Opcion incorrecta')
        continue

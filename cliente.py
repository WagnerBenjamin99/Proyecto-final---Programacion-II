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
      
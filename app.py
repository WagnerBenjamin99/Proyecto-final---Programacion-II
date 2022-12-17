from flask import Flask, request, jsonify, Response
from http import HTTPStatus
import json
import requests
from os import system
import requests
import socket


app=Flask(__name__)

with open("usuarios.json", encoding='utf-8') as json_:
    usuarios = json.load(json_)
with open("directores.json", encoding='utf-8') as json_:
    directores = json.load(json_)
with open("peliculas.json", encoding='utf-8') as json_:
    peliculas = json.load(json_)
with open("comentarios.json", encoding='utf-8') as json_:
    comentarios = json.load(json_)
with open("generos.json", encoding='utf-8') as json_:
    generos = json.load(json_)

sesion={}


@app.route('/')
def home():
    print('aaaa')
    return jsonify(peliculas)

@app.route('/login', methods=["POST"])
def iniciar_sesion():
    
    datos=request.get_json()
    print(type(datos))

    if "nombre_usuario" in datos and "contraseña" in datos:
        for usuario in usuarios:
            if usuario["nombre_usuario"] == datos["nombre_usuario"] and usuario["contraseña"] == datos["contraseña"]:
                return Response("{}", status=HTTPStatus.OK)
        return Response("{}", HTTPStatus.BAD_REQUEST)
    return Response("{}", HTTPStatus.BAD_REQUEST)

@app.route("/eliminar", methods=["DELETE"])
def eliminar_pelicula():
    contador = 0
    datos = request.get_json()
    
    if "id_pelicula" in datos:
        for comentario in comentarios:
            if comentario["id_pelicula"] == datos["id_pelicula"]:
                if comentario["id_usuario"] != datos['id_sesion']:
                    contador = contador + 1
        if contador != 0:
            return Response("{}", HTTPStatus.BAD_REQUEST)
        else:
            for pelicula in peliculas:
                if pelicula["id_pelicula"] == datos["id_pelicula"]:
                    peliculas.remove(pelicula)
                    print(peliculas)
            return Response("{}", HTTPStatus.OK)

    return Response("{}", HTTPStatus.BAD_REQUEST)

@app.route("/editar", methods=["PUT"])
def editar_pelicula():
    datos = request.get_json()
    for pelicula in peliculas:
        if pelicula["id_pelicula"]== datos["id_pelicula"]:
            if 'titulo' in datos:
                for pelicula in peliculas:
                    if datos["id_pelicula"]==pelicula["id_pelicula"]:
                        pelicula["titulo"]=datos["titulo"]
                        Response("{}", HTTPStatus.OK)
            elif 'portada' in datos:
                for pelicula in peliculas:
                    if datos["id_pelicula"]==pelicula["id_pelicula"]:
                        pelicula["postada"]=datos["portada"]
                        Response("{}", HTTPStatus.OK)
            elif 'sinopsis' in datos:
                for pelicula in peliculas:
                    if datos["id_pelicula"]==pelicula["id_pelicula"]:
                        pelicula["sinopsis"]=datos["sinopsis"]
                        Response("{}", HTTPStatus.OK)
            elif 'año' in datos:
                for pelicula in peliculas:
                    if datos["id_pelicula"]==pelicula["id_pelicula"]:
                        pelicula["año"]=datos["año"]
                        Response("{}", HTTPStatus.OK)
            elif 'id_genero' in datos:
                for pelicula in peliculas:
                    if datos["id_pelicula"]==pelicula["id_pelicula"]:
                        pelicula["id_genero"]=datos["id_genero"]
                        return Response("{}", HTTPStatus.OK)
            else:
                return Response("{}", HTTPStatus.BAD_REQUEST)
    return Response("{}", HTTPStatus.BAD_REQUEST) 

@app.route('/agregar', methods=["POST"])
def agregar_pelicula():
    id = peliculas[-1]['id_pelicula'] + 1
    datos = request.get_json()
    if "titulo" in datos and "id_director" in datos and "portada" in datos:
        if "sinopsis" in datos and "año" in datos and "id_genero" in datos:
            peliculas.append({
            "titulo":datos['titulo'],
            "id_pelicula":id,
            "sinopsis":datos['sinopsis'],
            "id_genero":datos["id_genero"],
            "año":datos["año"],
            "id_director":datos["id_director"],
            "portada":datos["portada"]
            })
            if 'comentario' in datos:
                comentarios.append(
                    {
                        'id_usuario':sesion,
                        'id_pelicula':id,
                        'cuerpo':datos['comentario']
                    }
                )
            return Response("{}", HTTPStatus.OK)
        return Response("{}", HTTPStatus.BAD_REQUEST) 
    return Response("{}", HTTPStatus.BAD_REQUEST) 



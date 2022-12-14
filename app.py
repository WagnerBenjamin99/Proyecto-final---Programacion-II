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
                sesion["id"]=usuario["id_usuario"]
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
                if comentario["id_usuario"] != sesion["id"]:
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

    



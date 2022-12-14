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





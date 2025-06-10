from flask import Blueprint, request, jsonify
from services.usuarios_services import *
from utils.msg_erro import ERROS

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["POST"])
def criar():
    dados_body = request.json
    novo_usuario = criar_usuario(dados_body)
    return jsonify(novo_usuario.to_dict()), 201

@usuarios_bp.route("/usuarios", methods=["GET"])
def lista_usuarios():
    lista = listar_usuarios()
    return jsonify(lista)

@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario = lista_um_usuario(id)
    if usuario:
        return jsonify(usuario.to_dict()), 200
   
@usuarios_bp.route("/usuarios/<int:id>", methods=["PATCH", "PUT"])
def atualizar(id):
    usuario = atualizar_usuario(id, request.json)
    return jsonify 

@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete0(id):
    sucesso = deletar_usuario(id)
    if sucesso:
        return "", 204
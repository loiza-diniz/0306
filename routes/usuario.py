from flask import Blueprint, request, jsonify
from services.usuarios_services import *

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
        return jsonify(usuario)
    else:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404
     
from flask import Blueprint, request, jsonify
from services.usuarios_services import *

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["POST"])
def criar():
    dados_body = request.json
    novo_usuario = criar_usuario(dados_body)
    return jsonify(novo_usuario.to_dict(    )), 201
     
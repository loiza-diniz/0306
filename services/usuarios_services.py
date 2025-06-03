from models.usuario import Usuario

usuarios = []
#variavel controle dos ids dos usuarios
id_usuario = 0


#função de atualização dos ids
def gerar_id():
    global id_usuario
    id_usuario += 1
    return id_usuario

def criar_usuario(dados):
    novo_usuario = Usuario(gerar_id(), dados["nome"], dados["email"], dados["senha"])
    usuarios.append(novo_usuario)
    return novo_usuario
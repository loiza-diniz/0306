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

def listar_usuarios():
    # lista = []
    #for u in usuarios:
        #lista.append(u.to_dict())
    #return lista
    lista = [u.to_dict() for u in usuarios]
    return lista

def lista_um_usuario(id):
    for u in usuarios:
        if u.id == id:
            return u.to_dict()
    return None

def atualizar_usuario(id):
    usuario_encontrado = lista_um_usuario(id)
    if usuario_encontrado:
        usuario_encontrado["nome"] = novos_dados.get("nome", usuario_encontrado["nome"])
        usuario_encontrado["email"] = novos_dados["email"]
        usuario_encontrado["senha"] = novos_dados["senha"]
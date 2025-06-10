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
    # Verifica se já existe um usuário com o mesmo email
    for u in usuarios:
        if u.email == dados["email"]:
            return None, "EMAIL DUPLICADO"

    novo_usuario = Usuario(gerar_id(), dados["nome"], dados["email"], dados["senha"])
    usuarios.append(novo_usuario)
    return novo_usuario

def listar_usuarios():
    # lista = []
    for u in usuarios:
         if u.id == id:
              return u
         return None
        
    lista = [u.to_dict() for u in usuarios]
    return lista

def lista_um_usuario(id):
    for u in usuarios:
        if u.id == id:
            return u.to_dict()
    return None

def atualizar_usuario(id, novos_dados):
    usuario_encontrado = lista_um_usuario(id)
    if usuario_encontrado:
        usuario_encontrado["nome"] = novos_dados.get("nome", usuario_encontrado["nome"])
        usuario_encontrado["email"] = novos_dados.get("email", usuario_encontrado["email"])
        usuario_encontrado["senha"] = novos_dados.get("senha", usuario_encontrado["senha"])
        return usuario_encontrado
    
def deletar_usuario(id):
    global usuarios
    for u in usuarios:
        if u.id == id:
            usuarios.remove(u)
            return True
    return False

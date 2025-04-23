import tkinter as tk
from tkinter import messagebox, simpledialog

usuarios = {"admin": "admin123"}
usuario_logado = None

def nome_valido(nome):
    return nome.isalnum()

def senha_valida(senha):
    return senha.isalnum() and len(senha) >= 3 and senha.strip()

def atualizar_interface():
    if usuario_logado:
        login_frame.pack_forget()
        logado_label.config(text=f"Logado como: {usuario_logado}")
        logado_frame.pack(pady=20)
    else:
        logado_frame.pack_forget()
        login_frame.pack(pady=20)

# Função de login
def fazer_login():
    global usuario_logado
    nome = login_entry.get().strip().lower()
    senha = senha_entry.get().strip()
    if nome not in usuarios:
        messagebox.showerror("Erro", "Usuário não encontrado.")
    elif usuarios[nome] != senha:
        messagebox.showerror("Erro", "Senha incorreta.")
    else:
        usuario_logado = nome
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        atualizar_interface()

# Função de cadastro
def cadastrar_usuario():
    nome = simpledialog.askstring("Cadastro", "Digite o nome de usuário:").strip().lower()
    if not nome_valido(nome) or nome in usuarios:
        messagebox.showerror("Erro", "Nome inválido ou já existe.")
        return
    senha = simpledialog.askstring("Cadastro", "Digite a senha:").strip()
    if not senha_valida(senha):
        messagebox.showerror("Erro", "Senha inválida! Use apenas letras ou números com pelo menos 3 caracteres.")
        return
    usuarios[nome] = senha
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

# Função de logout
def fazer_logout():
    global usuario_logado
    usuario_logado = None
    messagebox.showinfo("Logout", "Você saiu da conta.")
    atualizar_interface()

# Função de exibir usuários
def exibir_usuarios():
    lista = "\n".join(usuarios.keys())
    messagebox.showinfo("Usuários cadastrados", lista if lista else "Nenhum usuário cadastrado.")

# Função de edição
def editar_usuario():
    global usuario_logado
    if usuario_logado == "admin":
        alvo = simpledialog.askstring("Editar", "Digite o nome do usuário a editar:").strip().lower()
        if alvo == "admin":
            messagebox.showerror("Erro", "O administrador não pode editar a si mesmo.")
            return
        if alvo not in usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado.")
            return
    else:
        alvo = usuario_logado

    novo_nome = simpledialog.askstring("Editar", "Novo nome (Enter para manter):").strip().lower()
    nova_senha = simpledialog.askstring("Editar", "Nova senha (Enter para manter):").strip()

    if novo_nome and (not nome_valido(novo_nome) or novo_nome in usuarios):
        messagebox.showerror("Erro", "Nome inválido ou já existe.")
        return
    if nova_senha and not senha_valida(nova_senha):
        messagebox.showerror("Erro", "Senha inválida! Use apenas letras ou números com pelo menos 3 caracteres.")
        return

    nome_final = novo_nome if novo_nome else alvo
    senha_final = nova_senha if nova_senha else usuarios[alvo]
    usuarios[nome_final] = senha_final

    if novo_nome and novo_nome != alvo:
        del usuarios[alvo]
        if alvo == usuario_logado:
            usuario_logado = nome_final

    messagebox.showinfo("Sucesso", "Dados atualizados.")
    atualizar_interface()

# Função de exclusão
def excluir_usuario():
    global usuario_logado
    if usuario_logado == "admin":
        nome = simpledialog.askstring("Excluir", "Digite o nome do usuário a excluir:").strip().lower()
        if nome == "admin":
            messagebox.showerror("Erro", "O administrador não pode excluir a si mesmo.")
            return
        if nome not in usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado.")
            return
    else:
        nome = usuario_logado

    if messagebox.askyesno("Confirmar", f"Deseja realmente excluir '{nome}'?"):
        del usuarios[nome]
        if nome == usuario_logado:
            usuario_logado = None
        messagebox.showinfo("Sucesso", f"Usuário '{nome}' excluído.")
        atualizar_interface()

# Interface Tkinter
janela = tk.Tk()
janela.title("Sistema de Extravio de Bagagem")
janela.geometry("400x300")

# Frame inicial (login e cadastro)
login_frame = tk.Frame(janela)
tk.Label(login_frame, text="Usuário:").pack()
login_entry = tk.Entry(login_frame)
login_entry.pack()
tk.Label(login_frame, text="Senha:").pack()
senha_entry = tk.Entry(login_frame, show="*")
senha_entry.pack()
tk.Button(login_frame, text="Login", command=fazer_login).pack(pady=5)
tk.Button(login_frame, text="Cadastrar", command=cadastrar_usuario).pack()

# Frame logado
logado_frame = tk.Frame(janela)
logado_label = tk.Label(logado_frame, text="")
logado_label.pack()
tk.Button(logado_frame, text="Exibir Usuários", command=exibir_usuarios).pack(pady=2)
tk.Button(logado_frame, text="Editar Usuário", command=editar_usuario).pack(pady=2)
tk.Button(logado_frame, text="Excluir Usuário", command=excluir_usuario).pack(pady=2)
tk.Button(logado_frame, text="Logout", command=fazer_logout).pack(pady=5)

atualizar_interface()
janela.mainloop()

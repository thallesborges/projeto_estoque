import sqlite3
import customtkinter as ctk

def teste_ctk():
    print('Botão pressionado com sucesso!')

app = ctk.CTk()
app.title("Testando o CustomTkinter")
app.geometry("400x150")

botao = ctk.CTkButton(app, text="Botão", command=teste_ctk)
botao.grid(row=0, column=0, padx=20, pady=20)




'''
conexao = sqlite3.connect('estoque.db')

print('=== Menu do Estoque ===')
print('1. Visualizar Estoque')
print('2. Cadastrar Produto')



def listar_produtos(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM PRODUTOS')
    produtos = cursor.fetchall()
    for produto in produtos:
        print(produto)

print('Cadastro de Produtos')
nome_produto = input('Nome: ')
categoria_produto = input('Categoria: ')
quantidade_produto = int(input('Quantidade: '))
valor_produto = float(input('Valor: '))
local_produto = input('Local: ')

cursor.execute(
    '
    INSERT INTO PRODUTOS (NOME, CATEGORIA, QUANTIDADE, VALOR, LOCAL)
    VALUES (?, ?, ?, ?, ?)
    ', 
    (nome_produto, categoria_produto, quantidade_produto, valor_produto, local_produto)
) 

print('Produto cadastrado com sucesso!')

conexao.commit()'''

app.mainloop()
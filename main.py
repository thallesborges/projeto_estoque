import sqlite3

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
    '''
    INSERT INTO PRODUTOS (NOME, CATEGORIA, QUANTIDADE, VALOR, LOCAL)
    VALUES (?, ?, ?, ?, ?)
    ''', 
    (nome_produto, categoria_produto, quantidade_produto, valor_produto, local_produto)
) 

print('Produto cadastrado com sucesso!')

conexao.commit()
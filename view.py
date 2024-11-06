# Código do segundo vídeo do moço com relação a  biblioteca 2/12

import  sqlite3

#Conectar ao banco de dados 
def connect():
    con = sqlite3.connect('dados.db')
    return con

# Função para inserir um novo livro
def insert_book (titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) \
                VALUES (?, ?, ?, ?, ?)",(titulo, autor, editora, ano_publicacao, isbn))  
    
    # Função para inserir usuários
    def insert_user(nome, sobrenome, endereco, email,telefone):
        conn = connect()
        conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email,telefone) \
                    VALUES(?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email,telefone))
        
    # Exemplo das funções
    insert_book("Dom Quixote", "Miguel", "Editora 1", 1605, "123456" )
    insert_user ("André", " Alcântara", "Maracanaú", "andre@gmail.com", "1123456")

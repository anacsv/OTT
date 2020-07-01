from util import formatacao

def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo!')
    else:
        print(f'O arquivo {nome} foi criado.')    
#lista arquivos
def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!') 
    else: 
        formatacao('Produtos cadastrados:')
        print(a.read()) 
    finally:    
        a.close()    

#cadastra novos itens
def cadastrar(arq,nome,tipo):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir arquivo!')
    else:
        try:
            a.write(f'{nome};{tipo}\n')  
        except:
            print(f'O {nome} foi adicionado.')
            a.close()

def deletar(arq,nome):
    a = open(arq, "r")

    lines = a.readlines()
    a.close()
    new_file = open(arq, "w")
    encontrado = False
    for line in lines:
        if not line.startswith(nome+';'):
            new_file.write(line)
        else:    
            encontrado = True
            
    new_file.close()       
    if not encontrado:
        print('Item nao encontrado.')
        return False
    else:
        print('Item deletado.')
        return True   
     

def alterar(arq, nome, novo_nome, novo_tipo):
    deletado = deletar(arq, nome)
    if deletado:
        cadastrar(arq,novo_nome,novo_tipo)
        print('Item alterado.')

    

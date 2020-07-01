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

def deletar():
    pass
def alterar():
    pass

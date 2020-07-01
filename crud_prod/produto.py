from crud_prod import *

while True:
    resp = menu(['Cadastrar Produto','Listar Produtos','Deletar Produtos','Sair'])
    if resp == 1:
        print('opc1')
    elif resp == 2:
        print('opc2')
    elif resp == 3:
        print('opc3')
    elif resp == 4:
        print('Saindo do sistema...')    
        break            
    else:
        print('Erro! digite uma opçao válida conforme a lista!')



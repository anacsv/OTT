from util import formatacao, menu
from arquivo import ler_arq, arqexiste, criar_arq, cadastrar


def main():
    arq = 'arq.txt'
    #cria arquivo txt 
    if not arqexiste(arq):
        criar_arq(arq)

    while True:
        resp = menu(['Listar Produtos','Cadastrar Produto','Deletar Produtos','Sair'])
        if resp == 1:
            #listar produtos cadastrados de um arquivo
            ler_arq(arq)
        elif resp == 2:
            #cadastrar novo produto
            formatacao('Novo cadastro')
            nome = str(input('Nome: '))
            tipo = str(input('Tipo: '))
            cadastrar(arq, nome, tipo)
        elif resp == 3:
            print('opc3')
        elif resp == 4:
            print('Saindo do sistema...')    
            break            
        else:
            print('Erro! digite uma opçao válida conforme a lista!')

if __name__ == '__main__':
    main()


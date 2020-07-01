from util import formatacao, menu
from arquivo import ler_arq, arqexiste, criar_arq, cadastrar, deletar, alterar


def main():
    arq = 'arq.txt'
    #cria arquivo txt 
    if not arqexiste(arq):
        criar_arq(arq)

    while True:
        resp = menu(['Listar Produtos','Cadastrar Produto','Deletar Produtos','Alterar Produto','Sair'])
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
            deletar(arq,input('Informe o nome do item para deletar: '))
        elif resp == 4:
            #altera item
            nome = str(input('Informe o nome do item que será alterado: '))
            novo_nome = str(input('Novo nome: '))
            novo_tipo = str(input('Novo tipo: '))
            alterar(arq,nome,novo_nome,novo_tipo)    
        elif resp == 5:
            break              
        else:
            print('Erro! digite uma opçao válida conforme a lista!')

if __name__ == '__main__':
    main()


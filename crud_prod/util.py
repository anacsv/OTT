def entrada(msg):
    while True:
        try:
            m = int(input(msg))
        except(ValueError, TypeError):
            print('\n\033[32mERRO:Digite um numero válido conforme a lista.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu nao digitar esse numero.\033[m')   
            return 0 
        else:
            return m      

def linha(tam=30):
    return '-' * tam

#formata textos de menu
def formatacao(txt):
    print(linha())
    print(txt.center(30))
    print(linha())

#menu inicial 
def menu(lista):
    formatacao('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
        print(linha())
    opc = entrada('Sua opçao: ')
    return opc


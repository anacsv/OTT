# Exemplo de Polimorfismo seria uma classe Animal, onde ela pode ser gato ou cachorro, 
# é a mesma classe porém em cada subclasse terá funçoes bem diferentes.

# Exemplo de abstraçao é quando vc chama uma funçao,por exemplo print, len, str, etc, voce sabe o que ele vai te retornar 
# mas nao sabe como, nem qual o processo ele usou/passou para te dar aquela resposta.


# Exemplo de encapsulamento no Python
class Gato:
   # atributo publico
   frajola = 1 
   # atributo privado a classe gato
   __tricolor = 2 

class Cachorro(Gato):
    # atributo privado a classe cachorro
   __pitbull = 3 
   
   def __init__(self):
       # imprime o numero 1
     print(self.frajola)  
     # imprime o numero 3
     print(self.__pitbull)

animal = Cachorro()
# ocorre um erro, pois frajola é privado, pode ser acessado somente pela classe Gato
print(animal.__frajola) 


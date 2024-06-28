import click
class Pessoa:
    def __init__(self,nome,idade,cpf):
        self._nome = nome.title()
        self.idade = idade
        self.cpf = cpf
        

    def __str__(self):
        return f'nome: {self.nome}, idade: {self.idade}, cpf: {self.cpf}, nacionalidade: {self.nacionalidade}'
     
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()



# nome_input = input("Digite o nome da pessoa1: ")
# idade_input = input("Digite a idade da pessoa1: ")
# cpf_input = input("Digite o CPF da pessoa1: ")
# nacionalidade_input = input("Digite a nacionalidade da pessoa1: ")
# pessoa1 = Pessoa(nome_input,idade_input,cpf_input,nacionalidade_input)
    
# print(pessoa1)

class Estudante(Pessoa):
    def __init__(self,nome,idade,cpf, nota, situacao):
        super().__init__(nome,idade,cpf)
        self._nota = nota
        self. _situacao = situacao
    def __str__(self):
       return f'nome: {self.nome}, idade: {self.idade}, cpf: {self.cpf},  Nota: {self.nota}, Situação: {self.situacao}'
    @property    
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self,nova_nota):
        self._nota = nova_nota

    @property    
    def situacao(self):
        if self._nota >= '6':
            return 'Aprovado'
        else:
            return 'Reprovado'
        
lista_estudantes =[]
while True:
    print('CADASTRO DE ALUNOS\n')
    

    nome_input = input("Digite o nome aluno ou digite sair: ")
    if nome_input == 'sair':
        break
    else:
        idade_input = input("Digite a idade do aluno: ")
        cpf_input = input("Digite o CPF do aluno: ")
        nota_input = input("Digite a nota do aluno: ")
        situacao_input = ''

        estudante =Estudante(nome_input,idade_input,cpf_input,nota_input,situacao_input)
        lista_estudantes.append(estudante)

        print(f'O estudante {nome_input}, foi adicionado com sucesso!')
        print("")

click.clear()                      
print('Lista de estudante')
for aluno in lista_estudantes:
    print(aluno)
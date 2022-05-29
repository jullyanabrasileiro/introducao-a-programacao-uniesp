''' Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
1 - Cadastrar um funcionário
2 - Alterar um funcionário
3 - Listar (imprimir) todos os funcionários
4 - Excluir um funcionário
5 - Adicionar um aumento de salário


Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, E-mail, Data de Admissão e Salário. '''

''' Lista = []
dic = {}
tupla =()
'''



lista_de_cadastro = []
opcao = 1

print ('CONTROLE DE FUNCIONÁRIOS')

while opcao !=0:

    print('''O que você deseja fazer?\n
    1 - Incluir funcionário
    2 - Alterar funcionário
    3 - Listar funcionários
    4 - Remover funcionário
    5 - Aumento de salário
    6 - Sair''')

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        print('INCLUSÃO DE FUNCIONÁRIO:')

        pessoa = []

        nome = (input('Nome do funcionário: '))
        pessoa.append(nome)

        email = (input('E-mail:'))
        pessoa.append(email)

        datainicio = str(input('Digite a data de admissão (00/00/00)'))
        pessoa.append(datainicio)

        salario = float(input('Salário do funcionário em R$: '))
        pessoa.append(salario)

        lista_de_cadastro.append(pessoa)
    
    if opcao == 3:

        if lista_de_cadastro is None:
            print('Nenhum funcionário cadastrado!')   

        if lista_de_cadastro is not None: 
            print('LISTAGEM DE FUNCIONÁRIOS \n')
            for funcionario in lista_de_cadastro:
                print(lista_de_cadastro, end=', ')
    

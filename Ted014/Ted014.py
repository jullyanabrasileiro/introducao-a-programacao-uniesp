''' Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
1 - Cadastrar um funcionário
2 - Alterar um funcionário
3 - Listar (imprimir) todos os funcionários
4 - Excluir um funcionário
5 - Adicionar um aumento de salário


Sabendo que todos os funcionários cadastrados precisam ter no mínimo os dados: Código do Funcionário, Nome, E-mail, Data de Admissão e Salário. '''

print ('CONTROLE DE FUNCIONÁRIOS')

lista_de_funcionarios = list()
funcionario = dict()

print(''''O que você deseja fazer?

[ 1 ] - Incluir funcionário
[ 2 ] - Alterar funcionário
[ 3 ] - Listar funcionários
[ 4 ] - Remover funcionário
[ 5 ] - Listar todos os funcionários
[ 6 ] - Sair''')

opcao = input("Escolha uma opção:")

if opcao == "1":
    print('INCLUSÃO DE FUNCIONÁRIO:')
    funcionario['nome'] = str(input('Nome: '))
    funcionario['CPF'] = int(input('CPF: '))
    funcionario['email'] = str(input('Email: '))
    funcionario['admissão'] = str(input('Data de admissão (dd/mm/aa/): '))
    funcionario['salário'] = float(input('Salário: '))

    funcionario ['nome', 'CPF', 'email', 'admissão', 'salário'] = lista_de_funcionarios[:]
    lista_de_funcionarios.append(funcionario)
    
elif opcao == 2:

elif opcao == 3:
    for k, v in funcionario.items():
        print(f'{k}:{v}')   



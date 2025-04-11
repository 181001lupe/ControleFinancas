from classes.controle import Controle
from time import sleep


def exibirMenu():
    """
       Exibe o menu principal com as opções disponíveis para o usuário.
       """
    print('~' * 10, 'MENU', '~' * 10)
    print('[1] Adicionar nova despesa\n[2] Listar todas as despesas\n[3] Remover uma despesa\n[4] Editar uma despesa\n[5] Gerar relatório\n[6] Sair')


def menu():
    """
      Controla o fluxo do programa, permitindo ao usuário interagir com as opções do menu.
      Executa ações com base na escolha do usuário, como adicionar, listar, editar ou remover despesas.
      """
    controle = Controle()
    while True:
        exibirMenu()
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite um número válido!')
        if opcao == 1:
            descricao = str(input('Descrição da despesa: '))
            valor = float(input('Valor: R$').replace('.', '.'))
            data = str(input('Data: [dd/mm] '))
            categoria = str(input('Categoria: '))
            controle.adicionarDespesa(descricao, valor, data, categoria)
        elif opcao == 2:
            print('=' * 4, 'Despesas', '=' * 4)
            controle.listarDespesas()
        elif opcao == 3:
            controle.listarDespesas()
            controle.removerDespesa()
            controle.salvarDespesa()
        elif opcao == 4:
            controle.editarDespesa()
            controle.salvarDespesa()
            controle.listarDespesas()
        elif opcao == 5:
            controle.relatorio()
        elif opcao == 6:
            print('Encerrando...Volte sempre!')
            break
        else:
            print('Escolha uma opção válida!')
        sleep(1)
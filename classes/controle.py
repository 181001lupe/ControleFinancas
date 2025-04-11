from classes.despesa import Despesa
class Controle():
    """
        Classe responsável por gerenciar o controle de despesas, incluindo funcionalidades
        como adicionar, editar, remover, listar e gerar relatórios de despesas.
        """
    def __init__(self):
        """Inicializa o controle e carrega as despesas do arquivo."""
        self.controle = []
        self.carregarControle()

    def adicionarDespesa(self, descricao, valor, data, categoria):
        """
                Adiciona uma nova despesa ao controle.

                Parâmetros:
                descricao (str): Descrição da despesa.
                valor (float): Valor da despesa.
                data (str): Data da despesa.
                categoria (str): Categoria da despesa.
                """
        id =len(self.controle) + 1
        novaDespesa = Despesa(id, descricao, valor, data, categoria)
        self.controle.append(novaDespesa)
        self.salvarDespesa()
        print('Despesa adicionada com sucesso!')

    def salvarDespesa(self):
        """Salva todas as despesas no arquivo texto."""
        arquivo= open('despesa.txt', 'w', encoding='UTF-8')
        for despesa in self.controle:
            arquivo.write(f'{despesa.id} | {despesa.descricao} | {despesa.valor} | {despesa.data} | {despesa.categoria}\n')
    def carregarControle(self):
        """Carrega as despesas do arquivo texto para a memória."""
        import os
        if os.path.exists('despesa.txt'):
            arquivo = open('despesa.txt', 'r')
            linhas = arquivo.readlines()
            for linha in linhas:
                linha_formatada = linha.strip()
                lista = list(linha_formatada.split('|'))
                try:
                    id = int(lista[0])
                    valor = float(lista[2])
                except (ValueError, IndexError):
                    print(f'Erro ao carregar a linha: {linha}')
                    continue
                descricao = str(lista[1])
                data = str(lista[3])
                categoria = str(lista[4])
                controle = Despesa(id, descricao, valor, data, categoria)
                self.controle.append(controle)
    def listarDespesas(self):
        """Exibe todas as despesas cadastradas."""
        for despesa in self.controle:
            print(f'ID: {despesa.id} |Nome: {despesa.descricao} |Valor: R${despesa.valor} |Data da compra: {despesa.data} |Categoria: {despesa.categoria}')
    def removerDespesa(self):
        """
               Remove uma despesa pelo ID.

               Parâmetros:
               id (int): ID da despesa a ser removida.
               """
        if not self.controle:
            print('Nenhuma despesa cadastrada!')
        for despesa in self.controle:
                try:
                    id = int(input('Qual o ID do item que você deseja remover? '))
                    if id <=0 or id >len(self.controle):
                        print('ID inválido!')
                except ValueError:
                    print('Digite um número válido')
                    return
                if id == despesa.id:
                    self.controle.remove(despesa)
                    print('Despesa removida com sucesso!')
                    break
    def editarDespesa(self):
        """
                Edita uma despesa existente com base no ID informado.

                Parâmetros:
                id (int): ID da despesa a ser editada.
                """
        if not self.controle:
            print('Nenhuma despesa cadastrada!')
        for despesa in self.controle:
                if id == despesa.id:
                    print('O que você deseja editar?')
                    print('[1] Nome\n[2] Valor\n[3] Data\n[4] Categoria')
                    try:
                        id = int(input('Qual o ID do item que você deseja editar? '))
                        opc = int(input('Selecione uma opção: '))
                        if opc <= 0 or opc >= 5:
                            print('Digite uma opção válida!')
                    except ValueError:
                        print('Digite um valor válido!')
                        return
                    else:
                        if opc == 1:
                            print(f'Nome atual: {despesa.descricao}')
                            novoNome = input('Nova descrição: ')
                            despesa.descricao = novoNome
                            print('Descrição alterada com sucesso!')
                            break
                        if opc == 2:
                            print(f'Valor atual: {despesa.valor}')
                            try:
                                novoValor = float(input('Novo valor: ').replace('.', '.'))
                                despesa.valor = novoValor
                                print('Valor alterado com sucesso!')
                            except ValueError:
                                print('Digite um valor numérico válido')
                            break
                        if opc == 3:
                            print(f'Data atual: {despesa.data}')
                            novaData = input('Nova data: ')
                            despesa.data = novaData
                            print('Data alterada com sucesso!')
                            break
                        if opc == 4:
                            print(f'Categoria atual: {despesa.categoria}')
                            novaCategoria = input('Nova categoria: ')
                            despesa.categoria = novaCategoria
                            print('Categoria alterada com sucesso!')
                            break

    def relatorio(self):
        """Gera e exibe um relatório com estatísticas das despesas."""
        if not self.controle:
            print('Nenhuma despesa cadastrada')
            return
        soma = media = cont = 0
        maior = menor = self.controle[0].valor
        nomeMaior = nomeMenor = self.controle[0].descricao
        gastosCategoria = {}
        for despesa in self.controle:
            if despesa.categoria in gastosCategoria:
                gastosCategoria[despesa.categoria] += despesa.valor
            else:
                gastosCategoria[despesa.categoria] = despesa.valor
            cont += 1
            soma += despesa.valor
            if despesa.valor > maior:
                maior = despesa.valor
                nomeMaior = despesa.descricao
            if despesa.valor < menor:
                menor = despesa.valor
                nomeMenor = despesa.descricao
        media = soma / len(self.controle)
        print(f'Soma das despesas: R${soma:.2f}')
        print(f'Produto mais caro: {nomeMaior} | R${maior:.2f}')
        print(f'Produto mais barato: {nomeMenor} | R${menor:.2f}')
        print(f'Média de gasto: R${media:.2f}')
        print('Gastos por categoria:')
        for categoria, total in gastosCategoria.items():
            print(f'{categoria.strip()}: R${total:.2f}')




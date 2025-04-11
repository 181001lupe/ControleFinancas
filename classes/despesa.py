class Despesa():
    """
       Representa uma despesa individual.

       Atributos:
           id (int): Identificador único da despesa.
           descricao (str): Descrição da despesa.
           valor (float): Valor gasto.
           data (str): Data da despesa no formato 'dd/mm'.
           categoria (str): Categoria associada à despesa.
       """
    def __init__(self, id, descricao, valor, data, categoria):
        """
               Inicializa uma nova instância de Despesa.

               Args:
                   id (int): Identificador único da despesa.
                   descricao (str): Descrição da despesa.
                   valor (float): Valor gasto.
                   data (str): Data da despesa.
                   categoria (str): Categoria da despesa.
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria

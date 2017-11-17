from Pessoa import pessoa


class PessoaFisica(pessoa):
    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.CNPJ = CNPJ

    def getCPF(self, CNPJ):
        self.CNPJ = CNPJ

    def setCPF(self, CNPJ):
        self.CNPJ = CNPJ


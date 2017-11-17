from Pessoa import pessoa

class PessoaFisica(pessoa):

    def __init__(self, CPF, nome, idade):
        super().__init__(nome,idade)
        self.CPF = CPF


    def getCPF(self,CPF):
        self.CPF = CPF

    def setCPF(self,CPF):
        self.CPF = CPF


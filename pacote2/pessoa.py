
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrarDados(self):
        return self.nome, self.idade
    
    def seApresentar(self):
        return "Meu nome é " + self.nome
    
    def dizerOi(self):
        return "OI"

        
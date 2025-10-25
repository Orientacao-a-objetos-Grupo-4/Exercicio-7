class Funcionario():
    def __init__(self, nome, salarioBruto, totalAcrescimos, totalDescontos):
        self.nome = nome
        self.salarioBruto = salarioBruto
        self.totalAcrescimos = totalAcrescimos
        self.totalDescontos = totalDescontos

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setSalarioBruto(self, salarioBruto):
        self.salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.salarioBruto

    def setTotalAcrescimos(self, totalAcrescimos):
        self.totalAcrescimos = totalAcrescimos

    def getTotalAcrescimos(self):
        return self.totalAcrescimos

    def setTotalDescontos(self, totalDescontos):
        self.totalDescontos = totalDescontos

    def getTotalDescontos(self):
        return self.totalDescontos

    def calcularSalarioLiquido(self):
        return self.salarioBruto + self.totalAcrescimos - self.totalDescontos
class Colaborador:
    def __init__(self, nome, salario, idade, sexo, edv, baterPonto = False):
        self.__nome = nome
        self.__salario = salario
        self.__idade = idade
        self.__sexo = sexo
        self.__edv = edv
        self.baterPonto = baterPonto

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def get_idade(self):
        return self.__idade

    def get_sexo(self):
        return self.__sexo

    def get_edv(self):
        return self.__edv

    def set_nome(self, novoNome):
        self.__nome = novoNome
        return self.__nome

    def set_salario(self, novosalario):
        self.__salario = novosalario
        return self.__salario

    def set_idade(self, idadeNova):
        self.__idade = idadeNova
        return self.__idade

    def set_sexo(self, sexoNovo):
        self.__sexo = sexoNovo
        return self.__sexo

    def set_edv(self, novoEdv):
        self.__edv = novoEdv
        return self.__edv

    def bater_ponto(self):
        if self.baterPonto  == True:
            print(self.__nome + " já bateu o ponto")
            return
        print(self.__nome + " bateu o ponto")
        self.baterPonto = True

    def trabalhar(self):
        if self.baterPonto == True:
            print(self.__nome + " está trabalhando")
            return
        else:
            print(self.__nome + " ainda não bateu o ponto ")

    def aumento(self, aumento):
        self.__salario += aumento
        return self.__salario

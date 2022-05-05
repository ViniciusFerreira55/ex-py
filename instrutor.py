import Colaborador
class instrutor:
    def __init__(self, nome, salario, idade, sexo, edv, materia, linguas):
        super().__init__(nome, salario, idade, sexo, edv)
        self.__materia = materia
        self.__linguas = linguas

    def get_materia(self):
        return self.__materia

    def get_linguas(self):
        return self.__linguas

    def set_materia(self, materiaNova):
        self.__materia = materiaNova
        return self.__materia

    def aprendeLingua(self, novaLingua):
        self.__linguas = novaLingua
        return self.__linguas

    def darAula(self, aula):
        return True

    def montarAula(self, material):
        return True

    def chamarAtencao(self):
        print(Colaborador.Colaborador.get_nome()+" chamou atenção da aula")

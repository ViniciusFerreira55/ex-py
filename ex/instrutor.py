import Colaborador
class instrutor(Colaborador):
    def __init__(self, nome, salario, idade, sexo, edv, materia, darAula = False, montarAula = False):
        super().__init__(nome, salario, idade, sexo, edv)
        self.__materia = materia
        self.darAula = darAula
        self.montarAula = montarAula

    def get_materia(self):
        return self.__materia

    def set_materia(self, materiaNova):
        self.__materia = materiaNova
        return self.__materia

    def darAula(self, aula):
        if self.montarAula == True:
          print(Colaborador.Colaborador.get_nome() + "deu aula de " + aula)
        else:
          print(Colaborador.Colaborador.get_nome() + "ainda não montou a aula")

    def set_montarAula(self):
        if self.montarAula:
            print(Colaborador.Colaborador.get_nome() + " já montou a aula")
            self.darAula = True
        else:
            print(Colaborador.Colaborador.get_nome() + " montou a aula")


    def chamarAtencao(self):
        if self.darAula == True:
            print(Colaborador.Colaborador.get_nome()+" chamou atenção da aula")
        else:
            print(Colaborador.Colaborador.get_nome() + "não está dando aula")

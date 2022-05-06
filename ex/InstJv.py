import instrutor
from Colaborador import Colaborador


class InstJv(instrutor):
    def darAula(self, aula):
        if self.montarAula == True:
          print(Colaborador.get_nome() + "deu aula de " + aula)
        else:
          print(Colaborador.get_nome() + "ainda não montou a aula")

    def set_montarAula(self):
        if self.montarAula:
            print(Colaborador.get_nome() + " já montou a aula")
            self.darAula = True
        else:
            print(Colaborador.get_nome() + " montou a aula")


    def chamarAtencao(self):
        if self.darAula == True:
            print(Colaborador.get_nome()+" chamou atenção da aula")
        else:
            print(Colaborador.get_nome() + "não está dando aula")
import Colaborador
class Aprendiz:
    def __init__(self, nome, salario, idade, sexo, edv, grade, nota, curso, area):
        super().__init__(nome, salario, idade, sexo, edv)
        self.__grade = grade
        self.__nota = nota
        self.__curso = curso
        self.__area = area

    def get_area(self):
        return self.__area

    def get_curso(self):
        return self.__curso

    def get_nota(self):
        return self.__nota

    def get_grade(self):
        return self.__grade

    def set_area(self, areaNova):
        self.__area = areaNova
        return self.__area

    def set_curso(self, cursoNovo):
        self.__curso = cursoNovo
        return self.__curso

    def set_nota(self, notaNova):
        self.__nota = notaNova
        return self.__nota

    def set_grade(self, gradeNova):
        self.__grade = gradeNova
        return self.__grade

    def irAula(self):
        print(Colaborador.Colaborador.get_nome()+" foi a aula")

    def fazerAtv(self, materia):
        print(Colaborador.Colaborador.get_nome()+" fez a atividade de" + materia)

    def projeto(self):
        print(Colaborador.Colaborador.get_nome()+ "progrediu no projeto da "+ self.__area)
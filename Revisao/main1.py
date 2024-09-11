from quiz1 import *

if __name__ == '__main__':
    q1 = Quiz(10, 2)
    q2 = Quiz2A(5,7)
    q3 = Quiz3A(11,1)

    print(q1) # QUIZ
    print(q2) # QUIZ2A
    print(q3) # QUIZ3A

    print('Testando metodos separados')
    print(q1.get_acertos())
    print(q1.get_erros())
    print(q1.calcular_pontos())

    lista_qs = [q1,q2,q3]
    a1 = Aluno(1, 'Raphael', lista_qs)
    a2 = Aluno(2, 'Thalyta', lista_qs)
    print(a1)

    d = Disciplina("POO", "Ferauche", 2024, 4)
    d.add_aluno(a1)
    d.add_aluno(a2)
    print(d)
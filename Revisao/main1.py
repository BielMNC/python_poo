from quiz1 import *

if __name__ == '__main__':
    q1 = Quiz('POO','Rapahel', 10, 2)
    q2 = Quiz2A('POO','Thalyta',5,7)
    q3 = Quiz3A('POO', 'Thais',11,1)

    print(q1) # QUIZ
    print(q2) # QUIZ2A
    print(q3) # QUIZ3A

    print('Testando metodos separados')
    print(q1.get_acertos())
    print(q1.get_erros())
    print(q1.calcular_pontos())
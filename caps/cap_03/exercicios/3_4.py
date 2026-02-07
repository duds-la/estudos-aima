objetivo = [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

def contar_inversoes(estado):
    """
    Conta o número de inversões em um estado do 8-puzzle.
    O zero (espaço vazio) é ignorado.
    """
    inversoes = 0
    estado_sem_zero = [x for x in estado if x != 0]

    for i in range(len(estado_sem_zero)):
        for j in range(i + 1, len(estado_sem_zero)):
            if estado_sem_zero[i] > estado_sem_zero[j]:
                inversoes += 1

    return inversoes


def conjunto_do_estado(estado):
    inversoes = contar_inversoes(estado)

    if inversoes % 2 == 0:
        return "conjunto_par"
    else:
        return "conjunto_impar"


def eh_solucionavel(estado, objetivo):
    return conjunto_do_estado(estado) == conjunto_do_estado(objetivo)


estado1 = [1, 2, 3,
           4, 5, 6,
           7, 8, 0]

estado2 = [1, 2, 3,
           4, 5, 6,
           8, 7, 0]

print(contar_inversoes(estado1))  # 0
print(contar_inversoes(estado2))  # 1

print(eh_solucionavel(estado1, objetivo))  # True
print(eh_solucionavel(estado2, objetivo))  # False

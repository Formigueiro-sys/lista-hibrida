
import random


def gerar_regiao_ordenada(seed=42):
    gerador = random.Random(seed)

    numeros = gerador.sample(
        range(1, 1000001),
        1024
    )

    numeros.sort()

    return numeros


def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1

        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio, iteracoes

        elif lista[meio] < chave:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1, iteracoes


def busca_sequencial(lista, chave):
    iteracoes = 0

    for i in range(len(lista)):
        iteracoes += 1

        if lista[i] == chave:
            return i, iteracoes

    return -1, iteracoes


def buscar(chave, ordenada, cauda):
    posicao, iter_binaria = busca_binaria(
        ordenada, chave
    )

    iter_sequencial = 0

    if posicao != -1:
        local = "Região ordenada"

    else:
        posicao, iter_sequencial = busca_sequencial(
            cauda, chave
        )

        if posicao != -1:
            local = "Cauda não ordenada"
        else:
            local = "Não encontrada"

    total = iter_binaria + iter_sequencial

    return {
        "local": local,
        "iteracoes_binarias": iter_binaria,
        "iteracoes_sequenciais": iter_sequencial,
        "total": total,
        "posicao": posicao
    }


def intercalar(lista_a, lista_b):
    resultado = []

    i = 0
    j = 0

    while i < len(lista_a) and j < len(lista_b):

        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            i += 1

        else:
            resultado.append(lista_b[j])
            j += 1

    resultado.extend(lista_a[i:])
    resultado.extend(lista_b[j:])

    return resultado


def reorganizar(ordenada, cauda):
    cauda.sort()

    nova_lista = intercalar(ordenada, cauda)

    ordenada[:] = nova_lista

    cauda.clear()


def inserir_chave(chave, ordenada, cauda):

    if chave in ordenada or chave in cauda:
        return False

    cauda.append(chave)

    if len(cauda) == 10:
        reorganizar(ordenada, cauda)

    return True

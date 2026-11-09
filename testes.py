
import unittest

from main import (
    gerar_regiao_ordenada,
    busca_binaria,
    busca_sequencial,
    buscar,
    inserir_chave
)


class TestesListaHibrida(unittest.TestCase):

    def setUp(self):
        self.ordenada = [10, 20, 30, 40, 50]
        self.cauda = [90, 7, 63]

    def test_geracao_1024_numeros(self):
        lista = gerar_regiao_ordenada()

        self.assertEqual(len(lista), 1024)
        self.assertEqual(len(set(lista)), 1024)
        self.assertEqual(lista, sorted(lista))

    def test_semente_reprodutivel(self):
        lista1 = gerar_regiao_ordenada(42)
        lista2 = gerar_regiao_ordenada(42)

        self.assertEqual(lista1, lista2)

    def test_busca_binaria(self):
        posicao, iteracoes = busca_binaria(
            self.ordenada, 30
        )

        self.assertEqual(posicao, 2)
        self.assertGreater(iteracoes, 0)

    def test_busca_sequencial(self):
        posicao, iteracoes = busca_sequencial(
            self.cauda, 63
        )

        self.assertEqual(posicao, 2)
        self.assertEqual(iteracoes, 3)

    def test_busca_nao_encontrada(self):
        resultado = buscar(
            100, self.ordenada, self.cauda
        )

        self.assertEqual(
            resultado["local"],
            "Não encontrada"
        )

        self.assertEqual(
            resultado["iteracoes_sequenciais"],
            3
        )

    def test_busca_na_regiao_ordenada(self):
        resultado = buscar(
            30, self.ordenada, self.cauda
        )

        self.assertEqual(
            resultado["local"],
            "Região ordenada"
        )

        self.assertEqual(
            resultado["iteracoes_sequenciais"],
            0
        )

    def test_rejeitar_duplicado(self):
        resultado = inserir_chave(
            30, self.ordenada, self.cauda
        )

        self.assertFalse(resultado)

    def test_insercao_na_cauda(self):
        resultado = inserir_chave(
            100, self.ordenada, self.cauda
        )

        self.assertTrue(resultado)
        self.assertEqual(self.cauda[-1], 100)

    def test_reorganizacao_automatica(self):
        ordenada = [10, 20, 30]
        cauda = []

        for numero in range(100, 110):
            inserir_chave(numero, ordenada, cauda)

        self.assertEqual(cauda, [])

        self.assertEqual(len(ordenada), 13)

        self.assertEqual(
            ordenada,
            sorted(ordenada)
        )

    def test_novas_insercoes_apos_reorganizacao(self):
        ordenada = [10, 20, 30]
        cauda = []

        for numero in range(100, 110):
            inserir_chave(numero, ordenada, cauda)

        resultado = inserir_chave(
            200, ordenada, cauda
        )

        self.assertTrue(resultado)
        self.assertEqual(cauda, [200])


if __name__ == "__main__":
    unittest.main()

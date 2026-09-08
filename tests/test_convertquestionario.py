import unittest

from convertquestionario import converter_questionario


class ConverterQuestionarioTest(unittest.TestCase):
    def test_converte_perguntas_e_remove_marca_de_linha_legada(self):
        texto = """
        1. Como você está?/ 
        a) Bem/
        b) Preciso de uma pausa/

        2. Deseja continuar?
        a) Sim
        b) Não
        """

        self.assertEqual(
            converter_questionario(texto),
            [
                {
                    "id": 1,
                    "numero_original": 1,
                    "pergunta": "Como você está?",
                    "opcoes": [
                        {"id": "a", "texto": "Bem"},
                        {"id": "b", "texto": "Preciso de uma pausa"},
                    ],
                },
                {
                    "id": 2,
                    "numero_original": 2,
                    "pergunta": "Deseja continuar?",
                    "opcoes": [
                        {"id": "a", "texto": "Sim"},
                        {"id": "b", "texto": "Não"},
                    ],
                },
            ],
        )

    def test_rejeita_pergunta_incompleta(self):
        with self.assertRaisesRegex(ValueError, "ao menos duas opções"):
            converter_questionario("1. Pergunta?\na) Única opção")

    def test_rejeita_opcao_sem_pergunta(self):
        with self.assertRaisesRegex(ValueError, "antes da primeira pergunta"):
            converter_questionario("a) Opção perdida")


if __name__ == "__main__":
    unittest.main()

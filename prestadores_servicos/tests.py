import unittest
from app import create_app


class PrestadoresServicosIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_listar_prestadores_sucesso(self):
        response = self.client.get("/prestadores-servicos/")
        self.assertEqual(response.status_code, 200)

    def test_criar_prestador_sucesso(self):
        payload = {
            "cnpj": "88.777.666/0001-55",
            "razao_social": "Serviços Especiais LTDA",
            "telefone": "(83) 3222-1111",
            "email": "contato@servicos.com",
            "endereco": "Rua do Sol, 40",
            "status": "Ativo",
            "chave_pix": "88777666000155",
        }
        response = self.client.post(
            "/prestadores-servicos/novo", data=payload, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Prestador de serviços cadastrado com sucesso".encode("utf-8"),
            response.data,
        )

    def test_consultar_historico_ordens_servico(self):
        response = self.client.get("/prestadores-servicos/1/historico-os")
        self.assertEqual(response.status_code, 200)

    def test_alterar_status_prestador(self):
        payload = {"status": "Inativo"}
        response = self.client.post(
            "/prestadores-servicos/1/editar-status",
            data=payload,
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Status atualizado com sucesso".encode("utf-8"), response.data
        )


if __name__ == "__main__":
    unittest.main()
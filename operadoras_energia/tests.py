import unittest
from app import create_app


class OperadorasEnergiaIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_listar_operadoras_sucesso(self):
        response = self.client.get("/operadoras-energia/")
        self.assertEqual(response.status_code, 200)

    def test_criar_operadora_sucesso(self):
        payload = {
            "cnpj": "99.888.777/0001-00",
            "razao_social": "Operadora Nova Energia",
            "telefone": "(83) 3000-0000",
            "email": "contato@novaenergia.com",
            "status": "Ativo",
            "endereco": "Rua Central, 10",
            "site": "www.novaenergia.com",
        }
        response = self.client.post(
            "/operadoras-energia/novo", data=payload, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Operadora de energia cadastrada com sucesso".encode("utf-8"),
            response.data,
        )

    def test_criar_operadora_duplicidade_cnpj(self):
        payload = {
            "cnpj": "08.823.111/0001-90",
            "razao_social": "Empresa Duplicada",
            "telefone": "(83) 3218-0000",
            "email": "teste@duplicada.com",
            "status": "Ativo",
        }
        response = self.client.post("/operadoras-energia/novo", data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "O sistema deve impedir duplicidade de CNPJ".encode("utf-8"),
            response.data,
        )

    def test_alterar_status_operadora(self):
        payload = {"status": "Inativo"}
        response = self.client.post(
            "/operadoras-energia/1/editar-status",
            data=payload,
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Status atualizado com sucesso".encode("utf-8"), response.data
        )


if __name__ == "__main__":
    unittest.main()
import unittest
from app import create_app


class UnidadesConsumidorasIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_listar_ucs_sucesso(self):
        response = self.client.get("/unidades-consumidoras/")
        self.assertEqual(response.status_code, 200)

    def test_filtrar_uc_por_status(self):
        response = self.client.get("/unidades-consumidoras/?status=Ativo")
        self.assertEqual(response.status_code, 200)

    def test_criar_uc_sucesso(self):
        payload = {
            "codigo_conta": "UC-999000",
            "nome": "UC Nova Teste",
            "endereco": "Rua Teste, 100",
            "cooperado_id": 1,
            "status": "Ativo",
        }
        response = self.client.post(
            "/unidades-consumidoras/novo", data=payload, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Unidade consumidora cadastrada com sucesso", response.data)

    def test_criar_uc_erro_cooperado_inativo(self):
        payload = {
            "codigo_conta": "UC-888000",
            "nome": "UC Invalida",
            "endereco": "Rua Erro, 50",
            "cooperado_id": 3,
            "status": "Ativo",
        }
        response = self.client.post("/unidades-consumidoras/novo", data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "O cooperado selecionado precisa estar ativo".encode("utf-8"),
            response.data,
        )

    def test_editar_uc_cooperado_inativo_rejeicao(self):
        payload = {
            "nome": "UC Sul Alterada",
            "endereco": "Av Epitacio Pessoa",
            "cooperado_id": 3,
        }
        response = self.client.post("/unidades-consumidoras/2/editar", data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "O sistema deve impedir a associação com cooperados que estejam com status inativo".encode(
                "utf-8"
            ),
            response.data,
        )

    def test_alterar_status_uc(self):
        payload = {"status": "Inativo"}
        response = self.client.post(
            "/unidades-consumidoras/1/editar-status",
            data=payload,
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Status da unidade consumidora atualizado com sucesso".encode("utf-8"),
            response.data,
        )


if __name__ == "__main__":
    unittest.main()
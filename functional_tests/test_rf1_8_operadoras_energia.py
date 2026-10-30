import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class OperadorasEnergiaFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.base_url = "http://127.0.0.1:5000/operadoras-energia"

    def tearDown(self):
        self.browser.quit()

    def test_ct005_acesso_e_elementos_formulario_operadora(self):
        self.browser.get(f"{self.base_url}/novo")

        titulo = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(titulo.text, "Cadastro de Operadora de Energia")

        cnpj_input = self.browser.find_element(By.NAME, "cnpj")
        razao_social_input = self.browser.find_element(
            By.NAME, "razao_social"
        )
        telefone_input = self.browser.find_element(By.NAME, "telefone")
        email_input = self.browser.find_element(By.NAME, "email")
        status_select = self.browser.find_element(By.NAME, "status")

        endereco_input = self.browser.find_element(By.NAME, "endereco")
        site_input = self.browser.find_element(By.NAME, "site")

        self.assertTrue(cnpj_input.is_displayed())
        self.assertTrue(razao_social_input.is_displayed())
        self.assertTrue(telefone_input.is_displayed())
        self.assertTrue(email_input.is_displayed())
        self.assertTrue(status_select.is_displayed())
        self.assertTrue(endereco_input.is_displayed())
        self.assertTrue(site_input.is_displayed())

    def test_ct006_validacao_campos_obrigatorios_operadora(self):
        self.browser.get(f"{self.base_url}/novo")
        btn_salvar = self.browser.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        btn_salvar.click()

        mensagem_erro = self.browser.find_element(By.CLASS_NAME, "alert-danger")
        self.assertTrue(mensagem_erro.is_displayed())
        self.assertIn("Campos obrigatórios não preenchidos", mensagem_erro.text)

    def test_ct007_pesquisa_e_filtragem_operadoras(self):
        self.browser.get(self.base_url)

        campo_pesquisa = self.browser.find_element(By.NAME, "termo")
        select_status = self.browser.find_element(By.NAME, "status")
        btn_consultar = self.browser.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        campo_pesquisa.send_keys("Energisa")
        select_status.send_keys("Ativo")
        btn_consultar.click()

        tabela = self.browser.find_element(By.ID, "tabela-operadoras")
        self.assertTrue(tabela.is_displayed())

    def test_ct008_alteracao_status_operadora(self):
        self.browser.get(f"{self.base_url}/1/editar-status")

        select_status = self.browser.find_element(By.NAME, "status")
        btn_salvar = self.browser.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )

        select_status.send_keys("Inativo")
        btn_salvar.click()

        mensagem_sucesso = self.browser.find_element(
            By.CLASS_NAME, "alert-success"
        )
        self.assertTrue(mensagem_sucesso.is_displayed())
        self.assertIn("Status atualizado com sucesso", mensagem_sucesso.text)


if __name__ == "__main__":
    unittest.main()
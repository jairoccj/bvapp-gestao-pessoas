import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PrestadoresServicosFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self.base_url = "http://127.0.0.1:5000/prestadores-servicos"

    def tearDown(self):
        self.browser.quit()

    def test_ct009_acesso_e_elementos_formulario_prestador(self):
        self.browser.get(f"{self.base_url}/novo")
        titulo = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(titulo.text, "Cadastro de Prestador de Serviços")

        self.assertTrue(self.browser.find_element(By.NAME, "cnpj").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "razao_social").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "telefone").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "email").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "endereco").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "status").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "site").is_displayed())
        self.assertTrue(self.browser.find_element(By.NAME, "chave_pix").is_displayed())

    def test_ct010_validacao_cadastro_prestador_com_chave_pix(self):
        self.browser.get(f"{self.base_url}/novo")

        # Usando CNPJ único não presente no banco inicial
        self.browser.find_element(By.NAME, "cnpj").send_keys("77.888.999/0001-11")
        self.browser.find_element(By.NAME, "razao_social").send_keys("Manutenção Solar LTDA")
        self.browser.find_element(By.NAME, "telefone").send_keys("(83) 3333-1111")
        self.browser.find_element(By.NAME, "email").send_keys("atendimento@solarmaint.com")
        self.browser.find_element(By.NAME, "endereco").send_keys("Av. Brasil, 500")
        self.browser.find_element(By.NAME, "chave_pix").send_keys("77888999000111")

        btn_salvar = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn_salvar.click()

        mensagem_sucesso = self.browser.find_element(By.CLASS_NAME, "alert-success")
        self.assertTrue(mensagem_sucesso.is_displayed())
        self.assertIn("Prestador de serviços cadastrado com sucesso", mensagem_sucesso.text)

    def test_ct011_consulta_e_historico_ordens_servico(self):
        self.browser.get(self.base_url)

        campo_pesquisa = self.browser.find_element(By.NAME, "termo")
        campo_pesquisa.send_keys("Solar Manutenções")
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Aguarda o re-carregamento da página e garante a captura do elemento no novo DOM
        link_historico = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "link-historico-os"))
        )
        link_historico.click()

        titulo_historico = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        self.assertIn("Histórico de Ordens de Serviço", titulo_historico.text)

    def test_ct012_atualizacao_dados_prestador(self):
        self.browser.get(f"{self.base_url}/1/editar")

        campo_email = self.browser.find_element(By.NAME, "email")
        campo_email.clear()
        campo_email.send_keys("novo_email@solarmaint.com")

        btn_salvar = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn_salvar.click()

        mensagem_sucesso = self.browser.find_element(By.CLASS_NAME, "alert-success")
        self.assertTrue(mensagem_sucesso.is_displayed())
        self.assertIn("Dados do prestador atualizados com sucesso", mensagem_sucesso.text)


if __name__ == "__main__":
    unittest.main()
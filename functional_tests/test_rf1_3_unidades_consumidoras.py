import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class UnidadesConsumidorasFunctionalTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000/unidades-consumidoras"

    def tearDown(self):
        self.browser.quit()

    def test_ct001_acesso_pagina_cadastro_uc(self):
        self.browser.get(f"{self.base_url}/novo")
        
        titulo = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(titulo.text, "Cadastro de Unidade Consumidora")

        nome_input = self.browser.find_element(By.NAME, "nome")
        cooperado_select = self.browser.find_element(By.NAME, "cooperado_id")
        
        self.assertTrue(nome_input.is_displayed())
        self.assertTrue(cooperado_select.is_displayed())

if __name__ == '__main__':
    unittest.main()
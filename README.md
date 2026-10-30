# BVapp — Especificação e Organização de Cenários de Teste (Gestão de Pessoas)

Este repositório contém o mini projeto individual de organização dos cenários de teste para verificação e validação dos Requisitos Funcionais do módulo **Gestão de Pessoas** da plataforma **BVapp** (Gerenciamento Replicável de Cooperativas de Energia Solar).

A arquitetura do projeto utiliza **Python** e **Flask**, estruturada com **Blueprints** por domínio funcional e gerenciamento de dependências via **`uv`**, seguindo o modelo de TDD e testes funcionais apresentado na Aula 06.

---

## 📌 Módulos Cobertos
1. **1.3. Cadastro de Unidades Consumidoras (UCs)**
2. **1.8. Cadastro de Operadoras de Energia**
3. **1.9. Cadastro de Prestadores de Serviços**

---

## 📂 Organização das Pastas
* `functional_tests/`: Testes funcionais e de aceitação externos utilizando Selenium / Webdriver, simulando a navegação do usuário final.
* `unidades_consumidoras/`: Blueprint Flask do Módulo 1.3 (Rotas, Testes Internos e Especificação dos Cenários CT001 a CT004).
* `operadoras_energia/`: Blueprint Flask do Módulo 1.8 (Rotas, Testes Internos e Especificação dos Cenários CT005 a CT008).
* `prestadores_servicos/`: Blueprint Flask do Módulo 1.9 (Rotas, Testes Internos e Especificação dos Cenários CT009 a CT012).

---

## 👤 Autoria e Responsabilidade
* **Integrante**: Jairo Costa da Cunha Junior
* **Curso/Instituição**: Engenharia de Software / IFPB
* **Disciplina**: Validação e Verificação de Testes de Software (VVTS)
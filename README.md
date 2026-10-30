# BVapp - Especificação e Organização de Cenários de Teste (Gestão de Pessoas)

Este repositório contém o mini projeto individual de organização dos cenários de teste para verificação e validação dos Requisitos Funcionais do módulo **Gestão de Pessoas** da plataforma **BVapp** (Gerenciamento Replicável de Cooperativas de Energia Solar).

A arquitetura do projeto utiliza **Python** e **Flask**, estruturada com **Blueprints** por domínio funcional e gerenciamento de dependências via **`uv`**, seguindo o modelo de TDD e testes funcionais e de aceitação externos.

---

## 📌 Módulos Cobertos

1. **1.3. Cadastro de Unidades Consumidoras (UCs)** — Cenários CT001 a CT004
2. **1.8. Cadastro de Operadoras de Energia** — Cenários CT005 a CT008
3. **1.9. Cadastro de Prestadores de Serviços** — Cenários CT009 a CT012

---

## 📁 Organização do Projeto

```text
├── app.py                            # Application Factory e registro dos Blueprints
├── pyproject.toml / uv.lock          # Gerenciamento de projeto e dependências (uv)
├── .gitignore                        # Arquivos ignorados pelo Git
│
├── unidades_consumidoras/            # Módulo 1.3 (Rotas, testes e cenários BDD CT001-CT004)
├── operadoras_energia/               # Módulo 1.8 (Rotas, testes e cenários BDD CT005-CT008)
├── prestadores_servicos/             # Módulo 1.9 (Rotas, testes e cenários BDD CT009-CT012)
│
├── functional_tests/                 # Testes funcionais E2E com Selenium WebDriver
└── templates/                        # Templates HTML (Jinja2) organizados por módulo
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* **Python 3.11+**
* **uv** (Gerenciador de pacotes rápido para Python)
* **Google Chrome** e **ChromeDriver** instalados (necessário para os testes funcionais do Selenium)

---

### 1. Instalar Dependências

No diretório raiz do projeto, execute o comando abaixo para sincronizar o ambiente e instalar todas as dependências do `pyproject.toml`:

```bash
uv sync
```

---

### 2. Executar a Aplicação Flask

Para iniciar a aplicação em modo de desenvolvimento na porta `5000`:

```bash
uv run python app.py
```

Acesse no navegador: `http://127.0.0.1:5000/`

---

## 🧪 Como Executar os Testes

### Executar Todos os Testes

Para rodar todos os testes do repositório (Integração + Funcionais):

> **Atenção:** Certifique-se de que o servidor Flask esteja em execução no primeiro terminal (`uv run python app.py`) antes de rodar os testes funcionais em segundo plano.

```bash
uv run pytest
```

---

### Executar Testes de Integração (Internos)

Os testes de integração validam as rotas Flask e as respostas do servidor sem abrir o navegador:

```bash
# Testar todos os módulos internos
uv run pytest unidades_consumidoras/ operadoras_energia/ prestadores_servicos/

# Ou testar um módulo específico (ex: Operadoras de Energia)
uv run pytest operadoras_energia/tests.py
```

---

### Executar Testes Funcionais / E2E (Selenium)

1. **Inicie o servidor Flask em um terminal:**

```bash
uv run python app.py
```

2. **Em outro terminal, execute a suíte funcional:**

```bash
uv run pytest functional_tests/
```

Para rodar apenas o arquivo de teste funcional de um módulo específico:

```bash
# Exemplo: Testes funcionais de Prestadores de Serviços
uv run pytest functional_tests/test_rf1_9_prestadores_servicos.py
```

---

## 👤 Autoria e Responsabilidade

* **Integrante**: Jairo Costa da Cunha Junior
* **Curso/Instituição**: Engenharia de Software / IFPB
* **Disciplina**: Validação e Verificação de Testes de Software (VVTS)
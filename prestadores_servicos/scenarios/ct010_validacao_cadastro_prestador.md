# CT010 — Validação de Campos Obrigatórios, PIX e Unicidade no Prestador de Serviços

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.9.1 (CA01 ID 24375, CA02 ID 24376, CA03 ID 24377, CA04 ID 24380)
* **Ator**: Operador de Compras / Serviços
* **Objetivo**: Validar as regras de preenchimento obrigatório e a aceitação dos campos opcionais (Chave PIX e Site).

## Pré-condições e Preparação
* Acesso à tela de cadastro de prestadores.

## Fluxo Principal (Obrigatoriedade de Endereço e Campos Principais)
1. O ator acessa "Cadastrar Prestador de Serviços".
2. O ator preenche CNPJ, Razão Social, Telefone, Email e Status, mas deixa o campo "Endereço" em branco.
3. O ator clica em "Salvar".
4. O sistema impede o salvamento, destaca o campo Endereço e exibe: *"Campos obrigatórios não preenchidos"*.

## Fluxos Alternativos
* **FA01 - Cadastro Válido com Chave PIX**:
  1. O ator preenche todos os campos obrigatórios.
  2. O ator preenche o campo opcional "Chave PIX" com "financeiro@solarmaint.com".
  3. O ator clica em "Salvar".
  4. O sistema grava o registro e exibe: *"Prestador de serviços cadastrado com sucesso"*.

## Regras de Negócio
* RN01: CNPJ, Razão Social, Telefone, Email, Endereço e Status são obrigatórios.
* RN02: Site Institucional e Chave PIX são campos opcionais.

## Dados e Resultados Esperados
* Validação correta dos campos e armazenamento adequado das informações opcionais quando informadas.
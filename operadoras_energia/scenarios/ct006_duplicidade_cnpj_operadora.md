# CT006 — Validação de Unicidade de CNPJ e Campos Obrigatórios em Operadoras

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.8.1 (CA01 ID 24012, CA02 ID 24013, CA03 ID 24014, CA04 ID 24015)
* **Ator**: Operador de Cadastro
* **Objetivo**: Testar o bloqueio de duplicidade de CNPJ e a obrigatoriedade dos campos cadastrais.

## Pré-condições e Preparação
* Operadora "Neoenergia Borborema" previamente cadastrada com o CNPJ "08.823.555/0001-10".

## Fluxo Principal (Tentativa de Duplicidade de CNPJ)
1. O ator acessa "Cadastrar Operadora de Energia".
2. O ator preenche o CNPJ com "08.823.555/0001-10" (CNPJ existente).
3. O ator preenche os demais campos obrigatórios (Razão Social, Telefone, Email e Status).
4. O ator clica em "Salvar".
5. O sistema identifica a duplicidade, impede a gravação e exibe o alerta: *"O sistema deve impedir duplicidade de CNPJ"*.

## Fluxos Alternativos
* **FA01 - Ausência de Campo Obrigatório**:
  1. O ator preenche um CNPJ válido e não cadastrado, mas deixa o campo "Email" em branco.
  2. O ator clica em "Salvar".
  3. O sistema destaca o campo Email e exibe: *"Campos obrigatórios não preenchidos"*.

## Regras de Negócio
* RN01: CNPJ, Razão Social, Telefone, Email e Status são campos de preenchimento obrigatório.
* RN02: Não é permitido mais de um registro com o mesmo CNPJ.

## Dados e Resultados Esperados
* Exibição das mensagens de erro correspondentes e rejeição da inclusão no banco de dados.
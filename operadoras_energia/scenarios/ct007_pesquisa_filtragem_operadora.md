# CT007 — Consulta, Pesquisa e Filtragem por Status de Operadoras de Energia

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.8.2 (CA01 ID 24026, CA02 ID 24027, CA03 ID 24028, CA04)
* **Ator**: Consulta / Gestor de Contratos
* **Objetivo**: Verificar a filtragem da listagem de operadoras por termo de busca (Razão Social / CNPJ) e filtro de status.

## Pré-condições e Preparação
* Existência de operadoras cadastradas com status Ativo e Inativo.

## Fluxo Principal (Pesquisa por Razão Social e Filtro de Status)
1. O ator acessa a tela de "Consulta de Operadoras de Energia".
2. O ator digita "Energisa" no campo "Pesquisa".
3. O ator seleciona o filtro "Status" = "Ativo".
4. O ator clica em "Consultar".
5. O sistema retorna a lista filtrada contendo apenas as operadoras ativas que possuem "Energisa" na Razão Social.

## Fluxos Alternativos
* **FA01 - Pesquisa por CNPJ**:
  1. O ator digita "08.823.111" no campo de busca.
  2. O sistema exibe a operadora correspondente na tabela.
* **FA02 - Busca sem Resultados**:
  1. O ator pesquisa por um CNPJ não cadastrado.
  2. O sistema exibe a mensagem: *"Nenhuma operadora de energia encontrada"*.

## Regras de Negócio
* RN01: A listagem deve apresentar as colunas: Razão Social, CNPJ, Telefone, Email e Status.

## Dados e Resultados Esperados
* Filtros aplicados corretamente com apresentação dos registros esperados na interface.
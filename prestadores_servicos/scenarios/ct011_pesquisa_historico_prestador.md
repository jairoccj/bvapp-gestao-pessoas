# CT011 — Pesquisa, Filtro por Status e Consulta de Histórico de Ordens de Serviço

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.9.2 (CA01 ID 24394, CA02 ID 24395, CA03 ID 24396, CA04)
* **Ator**: Gestor de Manutenção
* **Objetivo**: Testar a pesquisa de prestadores por termo/status e a visualização do histórico de Ordens de Serviço (OS).

## Pré-condições e Preparação
* Prestadores cadastrados e com Ordens de Serviço associadas no sistema.

## Fluxo Principal (Pesquisa e Filtro de Prestadores)
1. O ator acessa "Consulta de Prestadores de Serviços".
2. O ator informa "Solar" no campo de pesquisa.
3. O ator seleciona Status = "Ativo" e clica em "Consultar".
4. O sistema lista os prestadores ativos que correspondem à pesquisa.

## Fluxos Alternativos
* **FA01 - Visualizar Histórico de Ordens de Serviço**:
  1. Na listagem de resultados, o ator seleciona um prestador de serviços.
  2. O ator clica na opção "Ver Histórico de Ordens de Serviço".
  3. O sistema exibe a lista de OS vinculadas ao prestador com seus respectivos status e datas.

## Regras de Negócio
* RN01: A listagem deve apresentar as colunas: Razão Social, CNPJ, Telefone, Email e Status.

## Dúvidas e Conflitos para Stakeholders
* **Dúvida 01**: Um prestador de serviços com status "Inativo" pode ter novas Ordens de Serviço abertas para ele ou o sistema deve bloquear novas associações?

## Dados e Resultados Esperados
* Exibição dos resultados filtrados e carregamento das Ordens de Serviço vinculadas ao prestador.
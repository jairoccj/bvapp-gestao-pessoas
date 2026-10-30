# CT003 — Pesquisa e Filtragem Combinada de Unidades Consumidoras

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.3.2 (CA01 ID 23654, CA02 ID 23655, CA03 ID 23656, CA04 ID 23657, CA05 ID 23658)
* **Ator**: Administrador / Cooperado
* **Objetivo**: Testar a funcionalidade de consulta por palavra-chave e a aplicação dos filtros combinados de cooperado e status.

## Pré-condições e Preparação
* Cadastros prévios de UCs com diferentes cooperados e status (Ativo e Inativo).

## Fluxo Principal (Filtros Combinados de Cooperado e Status)
1. O ator acessa a tela "Consulta de Unidades Consumidoras".
2. O ator seleciona o filtro "Cooperado Responsável" com o valor "Nadja Nóbrega".
3. O ator seleciona o filtro "Status" com o valor "Ativo".
4. O ator clica no botão "Consultar".
5. O sistema atualiza a listagem exibindo exclusivamente as UCs ativas vinculadas a "Nadja Nóbrega".

## Fluxos Alternativos
* **FA01 - Pesquisa por Endereço ou Nome**:
  1. O ator informa "Rua Ivete" no campo de busca textual.
  2. O ator clica em "Pesquisar".
  3. O sistema exibe apenas as UCs cujo endereço ou nome contenham o termo.
* **FA02 - Nenhum Registro Encontrado**:
  1. O ator busca por um termo sem correspondência (ex.: "UC Inexistente").
  2. O sistema exibe a mensagem: *"Nenhuma unidade consumidora encontrada"*.

## Regras de Negócio
* RN01: A grade de resultados deve apresentar as colunas: Código da Conta Contrato, Nome/Apelido, Endereço, Cooperado Responsável e Status.

## Dúvidas e Conflitos para Stakeholders
* **Dúvida 01**: Um perfil com papel "Cooperado" deve ter permissão de filtrar e visualizar apenas as suas próprias UCs ou pode visualizar o catálogo geral da cooperativa?

## Dados e Resultados Esperados
* Exibição exata dos dados correspondentes aos filtros aplicados e mensagem adequada em caso de busca vazia.
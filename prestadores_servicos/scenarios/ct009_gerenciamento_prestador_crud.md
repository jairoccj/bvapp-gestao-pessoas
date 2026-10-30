# CT009 — Gerenciamento Completo de Prestadores de Serviços (CRUD)

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.9.1 (Inclusão), RF 1.9.2 (Consulta), RF 1.9.3 (Atualização), RF 1.9.4 (Atribuição de Status)
* **Ator**: Gestor de Manutenção e Serviços
* **Objetivo**: Testar o ciclo de vida completo de um Prestador de Serviços (Criar, Consultar, Atualizar e Inativar).

## Pré-condições e Preparação
* Usuário autenticado com perfil autorizado.
* CNPJ "12.345.678/0001-00" não cadastrado.

## Fluxo Principal (Fluxo CRUD Completo)
1. **[Criar]**: O ator navega até "Cadastrar Prestador de Serviços", preenche os campos obrigatórios (CNPJ: "12.345.678/0001-00", Razão Social: "Solar Manutenções LTDA", Telefone: "(83) 3333-1111", Email: "atendimento@solarmaint.com", Endereço: "Av. Brasil, 500", Status: "Ativo") e opcionais (Site: "www.solarmaint.com", Chave PIX: "12345678000100") e clica em "Salvar".
2. **[Consultar]**: O ator acessa "Consulta de Prestadores de Serviços", busca por "Solar Manutenções" e verifica a exibição dos dados na tabela.
3. **[Atualizar]**: O ator clica em "Editar", altera a Razão Social para "Solar Manutenções e Engenharia LTDA", altera o Telefone para "(83) 3333-2222" e clica em "Salvar".
4. **[Excluir / Inativar]**: O ator acessa a alteração de status, modifica de "Ativo" para "Inativo" e clica em "Salvar".

## Fluxos Alternativos
* **FA01 - Cadastro de CNPJ Duplicado**: Se no passo 1 o ator inserir um CNPJ existente, o sistema impede o salvamento com a mensagem: *"CNPJ já cadastrado para outro prestador"*.

## Regras de Negócio
* RN01: O CNPJ deve ser único no cadastro de prestadores.
* RN02: A alteração de status deve registrar a data e o usuário responsável.

## Dados e Resultados Esperados
* **Criação**: Mensagem "Prestador de serviços cadastrado com sucesso".
* **Consulta**: Exibição exata de Razão Social, CNPJ, Telefone, Email e Status.
* **Atualização**: Mensagem "Dados do prestador atualizados com sucesso".
* **Inativação**: Mensagem "Status atualizado com sucesso". Status gravado como Inativo.
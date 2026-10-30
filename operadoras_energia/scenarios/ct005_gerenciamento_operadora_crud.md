# CT005 — Gerenciamento Completo de Operadoras de Energia (CRUD)

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.8.1 (Inclusão), RF 1.8.2 (Consulta), RF 1.8.3 (Atualização), RF 1.8.4 (Atribuição de Status)
* **Ator**: Administrador do Sistema
* **Objetivo**: Verificar o ciclo de vida completo de uma Operadora de Energia (Criar, Consultar, Atualizar e Inativar) em um fluxo integrado.

## Pré-condições e Preparação
* Usuário autenticado com perfil de Administrador.
* CNPJ "08.823.111/0001-90" livre para cadastro.

## Fluxo Principal (Fluxo CRUD Completo)
1. **[Criar]**: O ator acessa "Cadastrar Operadora de Energia", preenche os campos obrigatórios (CNPJ: "08.823.111/0001-90", Razão Social: "Energisa PB Distribuidora", Telefone: "(83) 3218-0000", Email: "contato@energisa.com.br", Status: "Ativo") e opcionais (Endereço: "BR 230 KM 12", Site: "www.energisa.com.br") e clica em "Salvar".
2. **[Consultar]**: O ator acessa a tela de "Consulta de Operadoras de Energia", digita o CNPJ "08.823.111/0001-90" no campo de busca e confirma a exibição dos dados na listagem.
3. **[Atualizar]**: O ator clica em "Editar", altera a Razão Social para "Energisa Paraíba Distribuidora S.A.", atualiza o Telefone para "(83) 3218-9999" e clica em "Salvar".
4. **[Excluir / Inativar]**: O ator acessa a edição de status, altera o valor para "Inativo", confirma e salva.

## Fluxos Alternativos
* **FA01 - Cadastro de CNPJ Duplicado**: No passo 1, se o ator tentar cadastrar um CNPJ já existente no banco de dados, o sistema impede o salvamento e exibe: *"CNPJ já cadastrado no sistema"*.

## Regras de Negócio
* RN01: O CNPJ deve ser único no cadastro de operadoras de energia.
* RN02: Alterações de status devem registrar a data da alteração e o usuário responsável.

## Dados e Resultados Esperados
* **Criação**: Mensagem "Operadora de energia cadastrada com sucesso".
* **Consulta**: Listagem exata contendo Razão Social, CNPJ, Telefone, Email e Status.
* **Atualização**: Mensagem "Dados da operadora atualizados com sucesso".
* **Inativação**: Mensagem "Status atualizado com sucesso". Registro atualizado para Inativo no banco.
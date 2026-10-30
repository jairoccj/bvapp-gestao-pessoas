# CT001 — Gerenciamento Completo de Unidades Consumidoras (CRUD)

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.3.1 (Inclusão), RF 1.3.2 (Consulta), RF 1.3.3 (Atualização), RF 1.3.4 (Atribuição de Status)
* **Ator**: Gestor de Unidades Consumidoras / Administrador do Sistema
* **Objetivo**: Verificar o fluxo completo de vida de uma Unidade Consumidora (Criar, Consultar, Atualizar e Inativar) em uma sequência contínua de operações.

## Pré-condições e Preparação
* Usuário autenticado e autorizado no sistema.
* Cooperado "Walmeran Trindade" cadastrado com status "Ativo".
* Cooperado "Nadja Nóbrega" cadastrado com status "Ativo".

## Fluxo Principal (Fluxo CRUD Completo)
1. **[Criar]**: O ator navega até "Cadastrar Unidade Consumidora", preenche os campos obrigatórios (Nome/Apelido: "UC Sede Centro", Código Conta Contrato: "UC-100239", Endereço: "Rua das Trincheiras, 156", Cooperado Responsável: "Walmeran Trindade", Status: "Ativo") e clica em "Salvar".
2. **[Consultar]**: O ator acessa a tela de "Consulta de Unidades Consumidoras", pesquisa pelo código "UC-100239" e seleciona o registro para visualizar os detalhes exibidos na tabela.
3. **[Atualizar]**: O ator clica em "Editar", altera o Nome/Apelido para "UC Sede Centro Expandida", altera o Cooperado Responsável para "Nadja Nóbrega" e clica em "Salvar Alterações".
4. **[Excluir / Inativar]**: O ator aciona a opção de alterar status, seleciona "Inativo", confirma a operação e salva o registro.

## Fluxos Alternativos
* **FA01 - Erro ao criar com cooperado inativo**: No passo 1, se o ator selecionar um cooperado inativo, o sistema impede o salvamento e exibe a mensagem: *"O cooperado selecionado precisa estar ativo"*.
* **FA02 - Tentativa de salvar edição sem campos obrigatórios**: No passo 3, se o ator apagar o campo Endereço, o sistema destaca o campo em vermelho e exibe: *"Campos obrigatórios não preenchidos"*.

## Regras de Negócio
* RN01: Uma Unidade Consumidora deve possuir obrigatoriamente um único cooperado responsável com status ativo.
* RN02: Toda atualização e alteração de status deve registrar automaticamente no histórico a data da alteração e o usuário responsável.

## Dúvidas e Conflitos para Stakeholders
* **Dúvida 01**: UCs com status "Inativo" devem continuar sendo listadas para seleção em processos de rateio mensal de energia ou devem ser filtradas e ocultadas?

## Dados e Resultados Esperados
* **Criação**: Exibição da mensagem "Unidade consumidora cadastrada com sucesso". Registro armazenado no banco com status Ativo.
* **Consulta**: Apresentação correta de código, nome, endereço, cooperado responsável e status na grade de consulta.
* **Atualização**: Exibição da mensagem "Dados da unidade consumidora UC Sede Centro Expandida atualizados com sucesso". Registro de auditoria atualizado.
* **Inativação**: Exibição da mensagem "Status da unidade consumidora atualizado com sucesso". Status do registro alterado para "Inativo".
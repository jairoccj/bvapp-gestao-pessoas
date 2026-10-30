# CT008 — Alteração de Status e Auditoria de Operadora de Energia

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.8.4 (CA01 ID 24346, CA02 ID 24347, CA03)
* **Ator**: Gestor de Operadoras
* **Objetivo**: Validar a alteração do status da operadora entre Ativo e Inativo e a gravação de histórico de auditoria.

## Pré-condições e Preparação
* Operadora "Energisa Paraíba" cadastrada com status "Ativo".
* Usuário "jairo_admin" autenticado.

## Fluxo Principal (Inativação da Operadora)
1. O ator acessa a tela de edição da operadora "Energisa Paraíba".
2. O ator altera o campo Status para "Inativo".
3. O ator clica no botão "Salvar".
4. O sistema salva o novo status, grava a data/hora da alteração e o usuário "jairo_admin" na tabela de auditoria.
5. O sistema exibe a mensagem: *"Status atualizado com sucesso"*.

## Regras de Negócio
* RN01: A alteração de status deve registrar obrigatoriamente a data/hora e o usuário responsável.

## Dúvidas e Conflitos para Stakeholders
* **Dúvida 01**: Ao inativar uma operadora de energia, as Usinas e Unidades Consumidoras associadas a ela devem ser alertadas ou inativadas automaticamente em cascata?

## Dados e Resultados Esperados
* Atualização do status para Inativo na interface e no banco de dados, acompanhado do log de auditoria.
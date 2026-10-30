# CT004 — Restrições e Auditoria na Atualização de Unidade Consumidora

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.3.3 (CA01 ID 23665, CA02 ID 23666, CA03 ID 23667, CA04 ID 23669, CA05 ID 23670, CA06 ID 23671)
* **Ator**: Gestor de Cadastro
* **Objetivo**: Validar as regras de integridade cadastral e a gravação de auditoria durante a edição de uma UC.

## Pré-condições e Preparação
* UC "UC Sul - 2004" cadastrada previamente.
* Usuário "jairo_gestor" logado no sistema.

## Fluxo Principal (Atualização Válida)
1. O ator acessa a consulta e clica na opção "Editar" da UC "UC Sul - 2004".
2. O ator altera o campo Endereço para "Avenida Epitácio Pessoa, 1200".
3. O ator clica no botão "Salvar".
4. O sistema grava as alterações, registra a data/hora atual e o usuário "jairo_gestor" no log de auditoria.
5. O sistema exibe a mensagem: *"Dados da unidade consumidora UC Sul - 2004 atualizados com sucesso"*.

## Fluxos Alternativos
* **FA01 - Tentativa de Alterar para Cooperado Inativo**:
  1. Na tela de edição, o ator seleciona um cooperado com status "Inativo".
  2. O ator clica em "Salvar".
  3. O sistema impede a gravação e exibe a mensagem: *"O sistema deve impedir a associação com cooperados que estejam com status inativo"*.

## Regras de Negócio
* RN01: Atualizações de dados cadastrais devem obrigatoriamente armazenar a data da última atualização e a identificação do usuário responsável.

## Dados e Resultados Esperados
* Persistência dos dados atualizados com os metadados de auditoria devidamente preenchidos.
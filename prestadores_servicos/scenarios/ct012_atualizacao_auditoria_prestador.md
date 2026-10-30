# CT012 — Atualização Cadastral e Registro de Auditoria do Prestador de Serviços

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.9.3 (CA01 ID 24415, CA02 ID 24419, CA03 ID 24422), RF 1.9.4 (CA01 ID 24450, CA02 ID 24452, CA03)
* **Ator**: Gestor do Sistema
* **Objetivo**: Verificar as restrições de integridade na edição e a gravação de dados de auditoria do prestador.

## Pré-condições e Preparação
* Prestador "Solar Manutenções" cadastrado.
* Usuário "jairo_gestor" logado na sessão.

## Fluxo Principal (Edição e Registro de Auditoria)
1. O ator acessa a edição do prestador "Solar Manutenções".
2. O ator atualiza o Email para "novo_email@solarmaint.com".
3. O ator clica em "Salvar".
4. O sistema salva os novos dados e atualiza o histórico de auditoria com a data/hora atual e o usuário "jairo_gestor".
5. O sistema exibe: *"Dados do prestador atualizados com sucesso"*.

## Fluxos Alternativos
* **FA01 - Tentativa de Alterar CNPJ para Valor em Uso**:
  1. Na edição, o ator altera o CNPJ para o CNPJ de outro prestador já cadastrado.
  2. O ator clica em "Salvar".
  3. O sistema impede o salvamento e exibe a mensagem de erro de duplicidade.

## Regras de Negócio
* RN01: O sistema deve impedir a alteração de CNPJ para um valor utilizado por outro prestador.
* RN02: A atualização cadastral e a alteração de status devem registrar a data da alteração e o usuário responsável.

## Dados e Resultados Esperados
* Dados cadastrais atualizados com sucesso e log de auditoria preenchido corretamente.
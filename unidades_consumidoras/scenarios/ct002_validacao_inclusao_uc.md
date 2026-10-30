# CT002 — Validação de Campos Obrigatórios e Status na Inclusão de UC

* **Elaborado por**: Jairo Costa da Cunha Junior
* **Requisitos Relacionados**: RF 1.3.1 (CA01 ID 23643, CA02 ID 23644, CA03 ID 23645, CA05 ID 23647, CA06 ID 23648)
* **Ator**: Operador de Cadastro
* **Objetivo**: Validar a obrigatoriedade dos campos cadastrais e o bloqueio de seleção de cooperados inativos na inclusão de UC.

## Pré-condições e Preparação
* Existência de pelo menos um cooperado inativo na base de dados ("Carlos Eduardo - Status: Inativo").

## Fluxo Principal (Tentativa com Campos Incompletos)
1. O ator acessa a tela de "Cadastro de Unidade Consumidora".
2. O ator preenche o Nome ("UC Parque") e o Código da Conta Contrato ("UC-8821"), deixando o campo "Endereço" em branco.
3. O ator seleciona um cooperado ativo no campo "Cooperado Responsável".
4. O ator clica em "Salvar".
5. O sistema impede o cadastro e exibe o alerta: *"Campos obrigatórios não preenchidos"*, destacando o campo Endereço.

## Fluxos Alternativos
* **FA01 - Seleção de Cooperado Inativo**:
  1. O ator preenche todos os campos obrigatórios (Nome, Conta Contrato e Endereço).
  2. No campo "Cooperado Responsável", seleciona "Carlos Eduardo" (Status: Inativo).
  3. O ator clica em "Salvar".
  4. O sistema exibe o alerta: *"O cooperado selecionado precisa estar ativo"* e impede a gravação.

## Regras de Negócio
* RN01: São campos obrigatórios na inclusão: Nome/Apelido, Código da Conta Contrato, Endereço, Cooperado Responsável e Status (padrão: Ativo).
* RN02: O sistema deve impedir a associação de UCs a cooperados com status inativo.

## Dados e Resultados Esperados
* Bloqueio da submissão do formulário, mensagens de erro visíveis e nenhum registro gravado no banco de dados.
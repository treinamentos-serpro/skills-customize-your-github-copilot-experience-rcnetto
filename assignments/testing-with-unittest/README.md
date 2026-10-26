# 📘 Assignment: Testing Python with unittest

## 🎯 Objective

Aprenda a verificar funções Python usando `unittest`, a biblioteca de testes incluída na linguagem. Você vai escrever testes para resultados esperados, casos-limite e erros, sem instalar dependências externas.

## 📝 Tasks

### 🛠️ Testar Resultados com assertEqual

#### Descrição
Execute o starter code e examine o teste inicial de `add_numbers()`. Amplie os testes dessa função para conferir diferentes entradas.

#### Requisitos
O programa concluído deve:

- Usar uma classe derivada de `unittest.TestCase` para agrupar os testes.
- Verificar com `assertEqual` a soma de números positivos, negativos e de uma soma com zero.
- Executar os testes com `python starter-code.py` e confirmar que todos passam.

### 🛠️ Testar Condições com assertTrue e assertFalse

#### Descrição
Escreva testes para `is_even()` e confirme que os resultados estão corretos para números pares e ímpares.

#### Requisitos
O programa concluído deve:

- Criar métodos de teste cujos nomes comecem com `test_`.
- Usar `assertTrue` para verificar números pares e `assertFalse` para verificar números ímpares.
- Incluir pelo menos um teste para zero.

### 🛠️ Testar Casos-Limite e Exceções

#### Descrição
Teste `calculate_average()` com uma lista comum, uma lista com um único valor e uma lista vazia. A função deve rejeitar a lista vazia lançando `ValueError`.

#### Requisitos
O programa concluído deve:

- Verificar a média de uma lista com vários valores e de uma lista com um único valor.
- Usar `assertRaises` para confirmar que uma lista vazia causa `ValueError`.
- Executar `python starter-code.py` e confirmar que todos os testes passam.

# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI para praticar endpoints HTTP, parâmetros de rota, validação de dados com Pydantic e operações CRUD em uma coleção de livros.

## 📝 Tasks

### 🛠️ Consultar Livros

#### Descrição
Implemente endpoints para consultar todos os livros e buscar um livro pelo ID. Execute a aplicação com `uvicorn main:app --reload` e use a interface interativa em `http://127.0.0.1:8000/docs` para testar as rotas.

#### Requisitos
O programa concluído deve:

- Disponibilizar `GET /books` e retornar a lista de livros em memória.
- Disponibilizar `GET /books/{book_id}` e retornar o livro correspondente ao ID.
- Responder com HTTP 404 quando o ID solicitado não existir.

### 🛠️ Cadastrar Livros

#### Descrição
Adicione um endpoint para cadastrar livros. Receba os dados no corpo da requisição e use o modelo Pydantic fornecido para validar os campos.

#### Requisitos
O programa concluído deve:

- Disponibilizar `POST /books` e receber `title` e `author` no corpo da requisição.
- Validar os dados recebidos com o modelo Pydantic.
- Criar um ID único, armazenar o novo livro e retornar o livro criado com status HTTP 201.

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as operações CRUD adicionando rotas para atualizar e remover um livro existente pelo ID.

#### Requisitos
O programa concluído deve:

- Disponibilizar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Disponibilizar `DELETE /books/{book_id}` para remover um livro existente.
- Responder com HTTP 404 se uma atualização ou remoção solicitar um ID inexistente.
- Retornar HTTP 204 ao remover um livro com sucesso.

Para começar, instale as dependências com `python -m pip install fastapi uvicorn` e complete o arquivo `starter-code.py`.

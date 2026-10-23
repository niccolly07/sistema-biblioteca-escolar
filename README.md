# Sistema de Biblioteca Escolar

## Ideia do projeto
O Sistema de Biblioteca Escolar será uma API para ajudar a organizar os livros, os alunos e os empréstimos da biblioteca. A proposta é facilitar o registro de livros, acompanhar empréstimos e devoluções e, futuramente, identificar atrasos.

## Objetivo desta etapa
Nesta primeira versão, o projeto contém apenas uma aplicação inicial em FastAPI com a rota principal (`/`) que retorna a mensagem `Olá Mundo!`, além de um teste automatizado para verificar sua resposta.

## Tecnologias
- Python
- FastAPI
- Uvicorn (servidor de desenvolvimento)
- Pytest (testes automatizados)
- Ruff (análise e formatação de código)
- Poe the Poet (atalhos para comandos)

## Como executar
Com Python e Poetry instalados, na pasta do projeto execute:

```bash
poetry install
poetry run fastapi dev app.py
```

A aplicação ficará disponível em `http://127.0.0.1:8000`. A documentação interativa da API fica em `http://127.0.0.1:8000/docs`.

## Como executar os testes

```bash
poetry run pytest
```

Ou use o atalho configurado:

```bash
poetry run poe test
```

## Próximas etapas
- Cadastrar e listar livros.
- Registrar alunos.
- Registrar empréstimos e devoluções.
- Verificar empréstimos atrasados.

# Estudos de FastAPI

Projeto de aprendizado de backend com Python e FastAPI. A API de tarefas explora rotas HTTP, modelos Pydantic e operações CRUD, com testes manuais pelo Postman.

Os dados ficam em memória e são apagados quando o servidor reinicia, inclusive ao salvar alterações com `--reload`. Ainda não há banco de dados nem frontend.

## Tecnologias

- Python, FastAPI e Pydantic
- Uvicorn para executar a API
- Postman para testar as requisições

## Executar no Windows

Com Python e Git instalados:

```powershell
git clone https://github.com/Murilo-Nep0muceno/minha-api.git
cd minha-api
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload --port 8888
```

Se já possui o projeto, comece dentro da pasta `minha-api`, sem cloná-lo novamente. Se a `.venv` já existe, não precisa recriá-la.

- API: http://127.0.0.1:8888
- Documentação interativa: http://127.0.0.1:8888/docs
- Para encerrar o servidor: `Ctrl + C`.

## Rotas

| Método | Rota | Objetivo |
|---|---|---|
| POST | `/tarefas` | Cadastrar uma tarefa e gerar seu ID |
| GET | `/tarefas` | Listar tarefas |
| GET | `/tarefas/{tarefa_id}` | Buscar uma tarefa |
| PUT | `/tarefas/{tarefa_id}` | Atualizar uma tarefa |
| DELETE | `/tarefas/{tarefa_id}` | Excluir uma tarefa |

O cadastro retorna `201`. As operações sobre IDs inexistentes retornam `404`. Veja as pendências de implementação abaixo.

## Testar no Postman

Envie `POST http://127.0.0.1:8888/tarefas`. Em **Body → raw → JSON**, use:

```json
{
  "titulo": "Aprender FastAPI",
  "concluida": false
}
```

O título é obrigatório. Se `concluida` for omitido, assume `false`. O ID é gerado pela API.

Depois, consulte `GET /tarefas` ou use o ID retornado em `GET /tarefas/{tarefa_id}`. GET e DELETE não precisam de Body. No PUT, envie título e situação da tarefa.

## Organização

```text
minha-api/
├── main.py             # API de tarefas e rotas de estudo
├── requirements.txt    # Dependências
├── .gitignore
├── README.md
└── lojinha_api/
    └── descricao.md    # Enunciado do próximo exercício
```

## Pendências atuais

- Corrigir a atualização de `concluida` no PUT: usar `=` em vez de `==`.
- Remover o GET por ID duplicado que retorna dados fixos, mantendo a busca na lista.

## Próximos passos

O próximo exercício é um CRUD de produtos com nome, preço, quantidade e situação de ativo. O enunciado está em [lojinha_api/descricao.md](lojinha_api/descricao.md). A API de produtos ainda não foi implementada.

Depois: validação de dados, filtros, PATCH, banco de dados, testes automatizados e autenticação.

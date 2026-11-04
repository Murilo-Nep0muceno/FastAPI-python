# Exercício: API da lojinha

Crie um CRUD de produtos com FastAPI. Use uma lista em memória e teste pelo Postman. Sem frontend e sem banco por enquanto.

## Produto
- `id`: inteiro, gerado pela API sem repetir após exclusões.
- `nome`: texto.
- `preco`: número decimal.
- `quantidade`: inteiro.
- `ativo`: booleano, padrão `true`.

Use um modelo Pydantic para receber os campos, sem incluir o ID.

## Rotas
| Método | Caminho | Ação |
|---|---|---|
| POST | `/produtos` | Cadastrar e retornar o produto com status 201 |
| GET | `/produtos` | Listar todos os produtos |
| GET | `/produtos/{produto_id}` | Buscar pelo ID |
| PUT | `/produtos/{produto_id}` | Atualizar os campos, mantendo o ID |
| DELETE | `/produtos/{produto_id}` | Excluir e retornar confirmação |

Retorne 404 ao buscar, atualizar ou excluir um ID inexistente. No PUT, envie todos os campos do produto, exceto o ID.

## Checklist no Postman
- [ ] Cadastrar dois produtos com IDs diferentes.
- [ ] Listar e consultar um produto pelo ID.
- [ ] Alterar preço e quantidade; conferir com GET.
- [ ] Excluir um produto e conferir a lista.
- [ ] Cadastrar outro produto sem repetir IDs existentes.
- [ ] Testar os erros 404.

Os dados serão apagados ao reiniciar o servidor. Não edite o arquivo entre os testes se estiver usando `--reload`.

Próxima etapa: validar nome vazio, preço maior que zero e quantidade não negativa. Não precisa implementar essas regras agora.

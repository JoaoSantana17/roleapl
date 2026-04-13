- João Vitor Lopes Santana RM560781

- Adão Yuri Ferreira da Silva RM559223


# Rolé API

API REST do aplicativo **Rolé** — construída com **FastAPI**, **SQLAlchemy** e **PostgreSQL**, com deploy na plataforma **Railway**.

---

## Deploy Online

A API está disponível em:

```
https://roleapl-production-3c2c.up.railway.app
```

Documentação interativa (Swagger):

```
https://roleapl-production-3c2c.up.railway.app/docs
```

---

## Tecnologias Utilizadas

- **Python 3.13**
- **FastAPI** — framework web
- **SQLAlchemy** — ORM
- **PostgreSQL** — banco de dados em nuvem (Railway)
- **psycopg (v3)** — driver PostgreSQL
- **Uvicorn** — servidor ASGI
- **Railway** — plataforma de deploy e banco de dados em nuvem

---

## Estrutura do Projeto

```
/devapi
├── main.py          # Rotas e endpoints da API
├── database.py      # Configuração do banco de dados
├── models.py        # Modelos SQLAlchemy (tabelas)
├── schemas.py       # Schemas Pydantic (validação)
├── crud.py          # Operações de banco de dados
└── requirements.txt # Dependências
```

---

## Entidades e Endpoints

| Entidade | Endpoints |
|---|---|
| Usuários | `GET/POST /usuarios/` · `GET/PUT/DELETE /usuarios/{id}` |
| Roles | `GET/POST /roles/` · `GET/PUT/DELETE /roles/{id}` |
| Participações | `GET/POST /participacoes/` · `GET/PUT/DELETE /participacoes/{id}` |
| Publicações | `GET/POST /publicacoes/` · `GET/PUT/DELETE /publicacoes/{id}` |
| Comentários | `GET/POST /comentarios/` · `GET/PUT/DELETE /comentarios/{id}` |
| Amizades | `GET/POST /amizades/` · `GET/PUT/DELETE /amizades/{id}` |
| Notificações | `GET/POST /notificacoes/` · `DELETE /notificacoes/{id}` |
| Localizações | `GET/POST /localizacoes/` · `GET /localizacoes/{id}/ultima` |
| Auditoria | `GET /auditoria/` |

---

---

## Resumo do que foi testado em vídeo

- Link video: https://www.youtube.com/watch?v=fq-ZIFnzgJM

### CREATE
Foram criados dois usuários, um rolê do tipo churrasco, uma participação, uma publicação, um comentário, uma amizade entre os usuários e uma notificação — todos persistidos no banco PostgreSQL em nuvem no Railway.

### READ
Listagem de todos os registros via `GET /entidade/` e busca individual via `GET /entidade/{id}`, confirmando que os dados foram salvos corretamente no banco.

### UPDATE
Atualização do nome do rolê via `PUT /roles/1` e dos dados do usuário via `PUT /usuarios/1`, refletindo as mudanças em tempo real no banco de dados.

### DELETE
Deleção da usuária Maria via `DELETE /usuarios/2` seguida de um `GET /usuarios/` confirmando que o registro foi removido com sucesso — **CRUD completo funcionando em produção**.

## Constraints do Banco de Dados

| Tabela | Campo | Valores Aceitos |
|---|---|---|
| usuario | privacidade | `público`, `amigos`, `privado` |
| role | tipo | `churrasco`, `bar`, `show`, `reunião`, `outro` |
| role | status | `ativo`, `finalizado` |
| participacao | meio_transporte | `carro`, `uber`, `metrô`, `ônibus`, `a pé` |
| participacao | status | `em_deslocamento`, `presente`, `ausente`, `finalizado` |
| notificacao | tipo | `saiu`, `chegou`, `rolê finalizado` |
| amizade | status | `pendente`, `aceito`, `bloqueado` |

---


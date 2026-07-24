# Agenda Médica

Aplicação web de agenda médica desenvolvida como desafio técnico. Permite login de usuário e, após autenticação, exibe os agendamentos médicos disponíveis em uma tabela interativa, com busca por paciente, CPF ou médico.

## Descrição da solução

A aplicação segue uma arquitetura em camadas dentro de um único serviço Flask:

- **Autenticação**: tela de login que valida credenciais contra um banco SQLite. Em caso de sucesso, gera um token JWT e o armazena em um cookie `httponly`, redirecionando o usuário para a tela principal.
- **Proteção de rotas**: um decorator (`@jwt_required`) lê e valida o JWT do cookie antes de liberar acesso à tela de agendamentos.
- **Integração com API**: a tela principal consome uma API de agendamentos via requisição HTTP real (usando a biblioteca `requests`). Essa API é simulada por um Blueprint separado (`mock_api`) dentro do mesmo processo Flask, retornando dados mockados em JSON.
- **Exibição dos dados**: os agendamentos são renderizados no navegador usando a biblioteca [Tabulator](https://tabulator.info/), com busca em tempo real por paciente, CPF ou médico.
- **Tratamento de falhas**: timeouts, indisponibilidade da API, respostas vazias/inválidas e campos obrigatórios ausentes são tratados de forma explícita, sem expor erros técnicos ao usuário final.

## Tecnologias utilizadas

- **Python 3.12** + **Flask 3** (framework web)
- **SQLite** (banco de dados)
- **PyJWT** (geração e validação de tokens JWT)
- **Werkzeug Security** (hash de senha com `generate_password_hash`/`check_password_hash`)
- **Requests** (cliente HTTP para consumo da API mockada)
- **Tabulator** (biblioteca JS para exibição/busca da tabela de agendamentos, via CDN)
- **Docker** e **Docker Compose** (empacotamento e execução)
- **python-dotenv** (variáveis de ambiente)

## Como executar com Docker

Pré-requisitos: Docker e Docker Compose instalados.

1. Crie um arquivo `.env` na raiz do projeto com base no `.env.exemple`:

```
TEST_USER_EMAIL=teste@timesaver.com
TEST_USER_PASSWORD=senha123
JWT_SECRET_KEY=uma-chave-secreta-qualquer
DATABASE_PATH=agenda.db
MOCK_API_URL=http://localhost:5000/mock-api/agendamentos
```

2. Suba a aplicação:

```bash
docker compose up --build
```

3. Acesse no navegador:

```
http://localhost:5000/login
```

> O banco é recriado (seed) toda vez que o container inicia, garantindo um ambiente de teste conhecido e reproduzível a cada execução — não é adequado para persistência de dados entre reinícios, apenas para fins de avaliação/teste deste desafio.

## Credenciais do usuário de teste

| Campo | Valor |
|---|---|
| Usuário/e-mail | `teste@timesaver.com` |
| Senha | `senha123` |

(valores definidos via variáveis de ambiente no `.env`, não hardcoded no código)

## Exemplos de uso

1. Acesse `/login` e informe as credenciais de teste acima.
2. Após o login, você será redirecionado para `/agenda`, onde a tabela de agendamentos é carregada a partir da API mockada.
3. Use o campo de busca acima da tabela para filtrar por nome do paciente, CPF ou nome do médico — a busca é feita em tempo real, sem recarregar a página.
4. Tentando acessar `/agenda` diretamente sem estar autenticado, o sistema redireciona automaticamente para `/login`.
5. Em caso de credenciais inválidas, uma mensagem genérica é exibida, sem indicar se o erro foi no usuário ou na senha (evita enumeração de contas).

## Decisões técnicas

- **SQLite ao invés de um banco cliente-servidor**: por ser um arquivo único, não exige um serviço/container de banco separado no `docker-compose.yml` — o volume mapeia apenas o arquivo `.db` para persistência do artefato entre builds.
- **API mockada como Blueprint interno, não como serviço externo**: simplifica o `docker-compose.yml` (não é necessário orquestrar dois serviços), mas ainda assim a aplicação principal faz uma requisição HTTP real (via `requests`) para consumi-la, preservando o comportamento de integração via rede — incluindo timeout e tratamento de falhas de conexão.
- **JWT em cookie `httponly` (em vez de bearer token via JavaScript)**: escolhido porque o fluxo do desafio pede redirecionamento tradicional pós-login (característica de aplicação renderizada no servidor), o que se encaixa melhor com sessão/cookie do que com um fluxo de SPA baseado em `Authorization` header.
- **Mensagem de erro genérica no login**: por segurança, não se diferencia "usuário não encontrado" de "senha incorreta" na mensagem exibida ao usuário.

## Limitações conhecidas

- A tabela `login_attempts`, criada no schema para fins de auditoria, ainda não está sendo populada pela aplicação — é uma melhoria pendente.
- A conexão com o banco SQLite no fluxo de login não possui tratamento explícito de exceção para falha de conexão (ex.: arquivo corrompido ou inacessível); esse cenário específico ainda não está coberto.
- A aplicação roda em modo debug mesmo dentro do container Docker; em um ambiente de produção real, isso seria desativado.
- Não há paginação na tabela de agendamentos — para o volume de dados mockado, não foi considerado necessário.

## Testes

Testes automatizados cobrindo login (válido/inválido), acesso não autenticado à rota protegida e falha na comunicação com a API mockada estão disponíveis na pasta `tests/`. Para rodar:

```bash
pip install -r requirements.txt
pytest
```

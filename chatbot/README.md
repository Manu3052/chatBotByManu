O código abaixo está incompleto devido a problemas pessoais especificados através do chat de Mariana, peço desculpas pelo inconveniente.


# Checklist do Desafio Técnico - Weni

## Configuração Inicial
- [ x] Criar repositório privado no GitHub/Bitbucket.
- [ x] Configurar `.gitignore` (primeiro commit).
- [ x] Configurar o ambiente com **Poetry** (diferencial).
- [x ] Configurar linting seguindo o PEP8.

## Desenvolvimento da Aplicação

### Camada de Abstração
- [ x] Implementar camada para facilitar a adição/substituição de canais.

### Integração de Canais
- [x ] Integrar com o Telegram (canal real).
- [ ] Implementar um canal mock (para testes).

### Persistência de Dados
- [ x] Criar modelo para **Contato**.
- [ x] Criar modelo para **Canal**.
- [x ] Criar modelo para **Atendente Humano**.
- [ x] Criar modelo para **Mensagem**.

### APIs REST
- [x ] API para configurar canais de comunicação.
- [ ] API para envio de mensagens (atendente → contato).
- [x ] API Webhook para recebimento de mensagens (canal → sistema).Configurar ot para resposta
- [ x] API para listar mensagens:
  - [x ] Implementar paginação.
  - [ x] Adicionar filtros por contato e atendente.

## Diferenciais 
- [x] Poetry
- [x] Integrar com uma plataforma real de atendimento humano


## Passo

É necessário ter Poetry instalado ou siga a documentação oficial para instalar.
https://python-poetry.org/docs/cli/#options-2
## Poetry

`cd chatbot`
`poetry install`
`poetry shell`
`poetry run python manage.py runserver`

## Sobre o projeto

A documentação do projeto engloba documentação técnica com docstrings (Funções, classes e outros), bem como documentação de rotas com swagger: localhost:8000/docs/

## Integração

Esse projeto possui interação com o bot do telegram.






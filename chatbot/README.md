O código abaixo está incompleto devido a problemas pessoais especificados através do chat de Mariana, peço desculpas pelo inconveniente.



Tabela Atendentes
id: Identificador único do atendente (Primary Key).
first_name: Primeiro nome do atendente (não nulo).
last_name: Sobrenome do atendente (não nulo).
password: Senha do atendente, armazenada com hash seguro (não nulo).

Tabela Contatos
id: Identificador único do contato (Primary Key).
cpf: CPF do contato (opcional).
telephone: Telefone do contato (opcional).
email: Endereço de e-mail único (não nulo, índice único).
name: Nome completo do contato (não nulo).

Tabela Chats
id: Identificador único do chat (Primary Key).
atendente_id: Referência ao atendente responsável (Foreign Key para Atendentes, com exclusão em cascata).
contato_id: Referência ao contato envolvido (Foreign Key para Contatos, com exclusão em cascata).
start_time: Data e hora de início do chat (padrão: timestamp atual).
closing_time: Data e hora de encerramento do chat (opcional).
service: telegram/wpp

Tabela Messages
id: Identificador único da mensagem (Primary Key).
chat_id: Referência ao chat ao qual a mensagem pertence (Foreign Key para Chats, com exclusão em cascata).
sender_type: Indica o remetente da mensagem (USER, BOT ou ATENDENTE).
message_content: Conteúdo da mensagem (não nulo, tipo texto).
created_at: Data e hora de criação da mensagem (padrão: timestamp atual).
updated_at: Data e hora de atualização da mensagem (opcional, caso a mensagem seja editada)




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

### Testes Unitários
- [ ] Criar testes unitários para os modelos.
- [ ] Criar testes para as APIs REST.
- [ ] Garantir cobertura de código mínima aceitável.

## Diferenciais (se houver tempo)
- [ ] Implementar autenticação com **JWT**.
- [ ] Configurar cache para perguntas frequentes.
- [ ] Criar arquivos **Dockerfile** e **docker-compose**.
- [ ] Implementar rotina com **Celery** para apagar mensagens antigas.
- [x ] Integrar com uma plataforma real de atendimento humano.
- [ ] Fazer deploy da aplicação (ex.: PythonAnywhere).

## Entrega
- [ ] Garantir que todos os requisitos foram implementados.
- [ ] Conceder acesso

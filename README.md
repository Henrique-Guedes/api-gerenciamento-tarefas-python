
# API de Gerenciamento de Tarefas (Python + Flask)

Projeto desenvolvido para demonstrar conhecimentos em:

- Criação de API REST
- CRUD completo
- Integração com banco de dados SQLite
- Organização básica de backend

## Como executar

1. Criar ambiente virtual:
python -m venv venv

2. Ativar ambiente:
venv\Scripts\activate  (Windows)

3. Instalar dependências:
pip install -r requirements.txt

4. Executar:
python app.py

A API rodará em:
http://127.0.0.1:5000

## Rotas disponíveis

POST /tarefas
GET /tarefas
PUT /tarefas/<id>
DELETE /tarefas/<id>

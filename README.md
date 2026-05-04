🚀 Atividade - FastAPI com ORM

Projeto desenvolvido para demonstrar a criação de uma API REST utilizando FastAPI integrada a um ORM para manipulação de banco de dados.

📌 Descrição

Este projeto consiste em uma aplicação backend construída com FastAPI, utilizando um ORM (como SQLAlchemy) para abstração do banco de dados, permitindo realizar operações CRUD (Create, Read, Update, Delete).

A aplicação segue boas práticas de organização, separando responsabilidades em camadas como:

Rotas (endpoints)
Modelos (ORM)
Schemas (validação com Pydantic)
Configuração de banco de dados
🛠️ Tecnologias utilizadas
Python 3.x
FastAPI
SQLAlchemy (ORM)
Pydantic
Uvicorn
SQLite / PostgreSQL (dependendo da configuração)
📂 Estrutura do projeto (exemplo)
├── app/
│   ├── main.py          # Arquivo principal da aplicação
│   ├── database.py      # Configuração do banco
│   ├── models.py        # Modelos ORM
│   ├── schemas.py       # Schemas (validação)
│   ├── crud.py          # Operações CRUD
│   └── routes/          # Rotas da API
│
├── requirements.txt
└── README.md
⚙️ Como executar o projeto
1. Clone o repositório
git clone https://github.com/IagoMonfredini/Atividade_FASTAPI-ORM
cd Atividade_FASTAPI-ORM
2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Instale as dependências
pip install -r requirements.txt
4. Execute o servidor
uvicorn app.main:app --reload
🌐 Acesse a API

Documentação Swagger:

http://127.0.0.1:8000/docs

Documentação alternativa (Redoc):

http://127.0.0.1:8000/redoc
📌 Funcionalidades
✅ Criação de registros
✅ Listagem de dados
✅ Atualização de informações
✅ Exclusão de registros
✅ Validação de dados com Pydantic
✅ Integração com banco de dados via ORM
🧠 Conceitos aplicados
Arquitetura em camadas
API RESTful
ORM (Object Relational Mapping)
Validação de dados
Boas práticas com FastAPI
📄 Exemplo de endpoint
POST /items/
{
  "name": "Produto exemplo",
  "price": 100
}
👨‍💻 Autor
Iago Monfredini
📜 Licença

Este projeto foi desenvolvido para fins acadêmicos.

💡 Observações

Projetos com FastAPI + ORM são amplamente utilizados para construção de APIs modernas, pois combinam alta performance com facilidade de desenvolvimento e validação automática de dados .

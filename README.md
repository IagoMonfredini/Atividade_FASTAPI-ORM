# 🚀 FastAPI + ORM API

API REST robusta desenvolvida com FastAPI utilizando SQLAlchemy como ORM para persistência de dados. Este projeto implementa padrões de design modernos e uma arquitetura escalável.

---

## 🧠 Sobre o Projeto

O objetivo principal deste repositório é demonstrar o domínio em construção de APIs performáticas, focando em:

- **Arquitetura em Camadas:** Separação clara entre modelos, schemas e lógica de negócio.  
- **Segurança de Tipos:** Uso extensivo de Type Hinting e Pydantic.  
- **Performance:** Operações assíncronas e servidor ASGI.  

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.10+  
- **Framework:** FastAPI  
- **ORM:** SQLAlchemy (Suporte a SQLite, PostgreSQL, MySQL)  
- **Validação:** Pydantic v2  
- **Servidor:** Uvicorn  

---

## 🧱 Arquitetura e Fluxo de Dados

O projeto segue a separação de responsabilidades para facilitar a manutenção:

- **models.py:** Definição das tabelas do banco de dados (SQLAlchemy).  
- **schemas.py:** Contratos de entrada e saída de dados (Pydantic).  
- **crud.py:** Camada de persistência (queries e manipulação de dados).  
- **routes/:** Controladores que gerenciam as rotas e respostas HTTP.  

---

## ⚙️ Instalação e Execução

### 1. Clonar o Repositório

```bash
git clone https://github.com/IagoMonfredini/Atividade_FASTAPI-ORM
cd Atividade_FASTAPI-ORM



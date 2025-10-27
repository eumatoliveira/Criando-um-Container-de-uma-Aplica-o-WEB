# Docker Compose Web App

Este projeto utiliza **Docker Compose** para orquestrar uma aplicação web completa com:

- **Python (Flask)** — aplicação web que se conecta ao MySQL.  
- **MySQL** — banco de dados com persistência de dados via volume.  
- **Adminer** — interface web para gerenciar o banco de dados.  

---

## Estrutura do projeto

web_app/
│
├─ app.py # Código da aplicação Flask
├─ requirements.txt # Dependências do Python
├─ Dockerfile # Dockerfile para construir a imagem da aplicação
└─ docker-compose.yml # Orquestra os serviços

markdown
Copiar código

---

## Conteúdo do docker-compose.yml

O `docker-compose.yml` define três serviços:

1. **db (MySQL)**  
   - Imagem: `mysql:8.0`  
   - Variáveis de ambiente configuradas:  
     - `MYSQL_ROOT_PASSWORD=Senha123`  
     - `MYSQL_DATABASE=minha_base`  
     - `MYSQL_USER=usuario`  
     - `MYSQL_PASSWORD=senha`  
   - Porta mapeada: `3306:3306`  
   - Volume persistente: `db_data:/var/lib/mysql`  

2. **web (Flask App)**  
   - Constrói a imagem a partir do `Dockerfile`.  
   - Depende do serviço `db`.  
   - Porta mapeada: `5000:5000`.  
   - Volume: monta a pasta atual para permitir edição do código em tempo real.  

3. **adminer**  
   - Imagem: `adminer`  
   - Porta mapeada: `8080:8080`  
   - Interface web para acessar o banco de dados MySQL.

---

## Como usar

1. **Clone o projeto** ou copie os arquivos para uma pasta local:

```bash
git clone <link-do-repositorio> web_app
cd web_app
Suba os serviços:

bash
Copiar código
docker-compose up -d
Acesse a aplicação web:

arduino
Copiar código
http://localhost:5000
Acesse o Adminer (interface do MySQL):

arduino
Copiar código
http://localhost:8080
System: MySQL

Server: db

Username: usuario

Password: senha

Database: minha_base

Parar os serviços:

bash
Copiar código
docker-compose down
Volumes
db_data → mantém os dados do MySQL persistentes mesmo após parar os containers.

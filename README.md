# Amparo - Backend ⚙️

Este é o repositório do backend da aplicação Amparo. Desenvolvido com **Django** e **Django REST Framework**, ele serve como API para o frontend mobile, gerenciando dados de medicamentos, usuários e outras funcionalidades da plataforma.

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Versão do Python](#versão-do-python)
- [Dependências do Sistema](#dependências-do-sistema)
- [Configuração Inicial](#configuração-inicial)
- [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
- [Como Rodar a Aplicação](#como-rodar-a-aplicação)

## Sobre o Projeto

O backend do Amparo é uma API RESTful que fornece os endpoints necessários para as operações do aplicativo móvel. Ele lida com a lógica de negócios, persistência de dados e autenticação/autorização de usuários.

## Tecnologias Utilizadas

* **Python**: Versão especificada abaixo.
* **Django**: Framework web de alto nível.
* **Django REST Framework**: Toolkit para a construção de Web APIs.
* **PostgreSQL**: Banco de dados relacional robusto para desenvolvimento e produção.
* **Pip**: Gerenciador de dependências Python.

## Versão do Python

Este projeto utiliza **Python 3.12**. É altamente recomendado o uso de um ambiente virtual (`venv`) para isolar as dependências do projeto.

## Dependências do Sistema

* **Python** 3.12 ou superior.
* **Pip** (geralmente já vem instalado com o Python).
* **Servidor PostgreSQL** (versão 12 ou superior recomendada).

## Configuração Inicial

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/luisjro16/amparo-back-end.git](https://github.com/luisjro16/amparo-back-end.git)
    cd amparo-back-end
    ```

2.  **Crie e ative um ambiente virtual:**
    Esta é a melhor prática para projetos Python, isolando as dependências.
    
    ```bash
    # Crie o ambiente virtual (só precisa fazer isso uma vez)
    python -m venv venv
    ```
    
    ```bash
    # Ative o ambiente virtual (precisa fazer isso toda vez que for trabalhar no projeto)
    # No Windows (cmd ou PowerShell):
    venv\Scripts\activate
    # No Linux ou macOS:
    # source venv/bin/activate
    ```

3.  **Instale as dependências do projeto:**
    O arquivo `requirements.txt` lista todos os pacotes Python necessários.
    ```bash
    pip install -r requirements.txt
    ```

## Configuração do Banco de Dados

Este projeto está configurado para usar **PostgreSQL** tanto para desenvolvimento quanto para produção.

1.  **Instale e Inicie o PostgreSQL:**
    Certifique-se de ter um servidor PostgreSQL rodando na sua máquina. Se não tiver, você pode baixá-lo através do [site oficial](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

2.  **Crie o Banco de Dados:**
    Antes de rodar as migrações, você precisa criar um banco de dados vazio para o projeto. Você pode usar uma ferramenta gráfica como o **pgAdmin 4** (que vem com a instalação do Postgres) para criar um novo banco de dados.
    * **Nome sugerido:** `amparo_db`

3.  **Configure as Variáveis de Ambiente:**
    Para segurança, as credenciais do banco de dados não devem ser escritas diretamente no código. Crie um arquivo chamado `.env` na raiz do projeto e adicione suas credenciais.
    
    Crie o arquivo `.env` com o seguinte conteúdo:
    ```
    # Exemplo de conteúdo para o arquivo .env
    SECRET_KEY='sua-secret-key-super-segura-aqui'
    DB_NAME='amparo_db'
    DB_USER='postgres'
    DB_PASSWORD='sua_senha_do_banco'
    DB_HOST='localhost'
    DB_PORT='5432'
    ```
    *O arquivo `settings.py` já deve estar configurado para ler essas variáveis. O `.gitignore` do projeto deve conter a linha `.env` para que este arquivo nunca seja enviado para o GitHub.*

4.  **Execute as migrações:**
    Este comando irá ler os modelos do Django e criar todas as tabelas no seu banco de dados PostgreSQL.
    ```bash
    python manage.py migrate
    ```

5.  **(Opcional, mas recomendado) Crie um superusuário:**
    Para acessar o painel de administração do Django, crie um usuário administrador.
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções no terminal para definir um nome de usuário, email e senha.

## Como Rodar a Aplicação

1.  **Para iniciar o servidor Django localmente:**
    Este comando sobe o servidor em `http://127.0.0.1:8000/`.
    ```bash
    python manage.py runserver
    ```

2.  **Para testar com o seu celular (Expo Go):**
    Use este comando para que o servidor seja acessível na sua rede Wi-Fi local.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

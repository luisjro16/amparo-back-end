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
* **SQLite3**: Banco de dados para ambiente de desenvolvimento.
* **Pip**: Gerenciador de dependências Python.

## Versão do Python

Este projeto utiliza **Python 3.12**. É altamente recomendado o uso de um ambiente virtual (`venv`) para isolar as dependências do projeto.

## Dependências do Sistema

* **Python** 3.12 ou superior.
* **Pip** (geralmente já vem instalado com o Python).
* **SQLite 3** (já vem incluído na biblioteca padrão do Python).

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

Este projeto utiliza SQLite3 para o ambiente de desenvolvimento, conforme configurado em `settings.py`.

1.  **Execute as migrações:**
    O Django criará o arquivo de banco de dados `db.sqlite3` automaticamente na primeira vez que você rodar as migrações. Este comando cria todas as tabelas necessárias baseadas nos seus modelos.
    ```bash
    python manage.py migrate
    ```

2.  **(Opcional, mas recomendado) Crie um superusuário:**
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
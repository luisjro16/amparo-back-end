# Amparo - Backend ⚙️

Este é o repositório do backend da aplicação Amparo. Desenvolvido com Ruby on Rails, ele serve como API para o frontend mobile, gerenciando dados de medicamentos, usuários e outras funcionalidades da plataforma.

## Sumário

* [Sobre o Projeto](#sobre-o-projeto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Versão do Ruby](#versão-do-ruby)
* [Dependências do Sistema](#dependências-do-sistema)
* [Configuração Inicial](#configuração-inicial)
* [Configuração do Banco de Dados](#configuração-do-banco-de-dados)
* [Como Rodar a Aplicação](#como-rodar-a-aplicação)
  
## Sobre o Projeto

O backend do Amparo é uma API RESTful que fornece os endpoints necessários para as operações do aplicativo móvel. Ele lida com a lógica de negócios, persistência de dados e autenticação/autorização.

## Tecnologias Utilizadas

* **Ruby:** Versão especificada abaixo.
* **Ruby on Rails:** Framework web MVC.
* **SQLite3:** Banco de dados para ambiente de desenvolvimento e teste.
* **Bundler:** Gerenciador de dependências Ruby (gems).

## Versão do Ruby

Este projeto utiliza **Ruby `3.2.2`**.
É recomendado o uso de um gerenciador de versões Ruby como [rbenv](https://github.com/rbenv/rbenv), para garantir a versão correta.

## Dependências do Sistema

* Ruby `3.2.2`
* Bundler (gem): `gem install bundler`
* SQLite 3.8.0 ou superior (incluindo bibliotecas de desenvolvimento, ex: `sudo apt-get install libsqlite3-dev` em sistemas Debian/Ubuntu).

## Configuração Inicial

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/luisjro16/amparo-back-end.git
    cd amparo-back-end 
    ```

2.  **Instale a versão correta do Ruby (se estiver usando um gerenciador de versões):**
    ```bash
    # Exemplo com rbenv:
    rbenv install 3.2.2
    rbenv local 3.2.2
    ```

3.  **Instale o Bundler (se ainda não o tiver para esta versão do Ruby):**
    ```bash
    gem install bundler
    ```

4.  **Instale as dependências do projeto (gems):**
    ```bash
    bundle install
    ```

## Configuração do Banco de Dados

Este projeto utiliza SQLite3 para os ambientes de desenvolvimento e teste, conforme configurado em `config/database.yml`.

1.  **Crie o banco de dados:**
    ```bash
    rails db:create
    ```

2.  **Execute as migrações:**
    ```bash
    rails db:migrate
    ```

## Como Rodar a Aplicação

Para iniciar o servidor Rails localmente:

```bash
rails server
```
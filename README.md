# Sistema de Cadastro e Login de Usuários

Este projeto é um sistema simples de **cadastro e login de usuários** desenvolvido em **Python**. Ele utiliza o **SQLite** como banco de dados para persistir as informações dos usuários e oferece as operações básicas de um **CRUD** (Create, Read, Update, Delete) para gerenciar os dados dos usuários. 

---
## 📖 Sumário
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#️-pré-requisitos)
- [Como Executar](#️-como-executar)
- [Conclusão](#-conclusão)
---
## 🚀 Funcionalidades
- **Cadastro de Usuário**: Permite que novos usuários se cadastrem fornecendo nome de usuário, ano de nascimento, sexo e nacionalidade. A senha é armazenada de forma segura usando hash SHA-256.

- **Login de Usuário**: Usuários cadastrados podem fazer login com seu nome de usuário e senha.

- **Listar Usuários**: Exibe uma lista de todos os usuários cadastrados no banco de dados, incluindo seus IDs.

- **Atualizar Dados do Usuário**: Permite a modificação das informações de um usuário existente (nome de usuário, ano de nascimento, sexo ou nacionalidade) com base no ID do usuário.

- **Apagar Usuário**: Permite a exclusão de um usuário do banco de dados com base no seu ID.



---

## 📂 Estrutura do Projeto

Cadastro_usuario/  
│── main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # lógica principal do app (menu do terminal)  
│── db.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # funções de banco de dados (Create, Read, Update, Delete)  
│── .gitignore &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # ignora arquivos desnecessários (pycache, tmp etc.)  
│── README.md &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; # documentação (este arquivo)

---

## 🛠️ Pré-requisitos / Tecnologias Utilizadas
* **Python**: Linguagem de programação principal utilizada no desenvolvimento do projeto.

* **SQLite**: Sistema de gerenciamento de banco de dados relacional leve e integrado, utilizado para armazenar os dados dos usuários.

---
## ▶️ Como executar
Clone este reposítorio e execute o programa no terminal:
```bash
git clone https://github.com/raphhhaaaa/Cadastro_usuario.git
```
```bash
cd Cadastro_usuario
```
```bash
python main.py
```
O programa irá criar automaticamente o arquivo ```usuario.db``` na primeira execução. Se trata do arquivo DataBase responsável por alocar os dados localmente.

---
# 🧠 Uso
Ao executar o programa, você será apresentado a um menu com as seguintes opções:

 1 . **Cadastro**: Inicia o processo de cadastro de um novo usuário.

 2 . **Login**: Permite que um usuário existente faça login no sistema.

 3 . **Sair**: Encerra a execução do programa.

 98 . **Listar dados de usuarios**: Exibe os dados de todos os usuários cadastrados.

 99 . **Apagar usuário**: Permite remover um usuário pelo seu ID.

 100 . **Atualizar dados**: Permite atualizar as informações de um usuário existente.

Basta digitar o número da opção desejada e pressionar **Enter* para interagir com o sistema.

---
## 📜 Conclusão
Este projeto foi desenvolvido com objetivos de prática e estudo, por isso, está sujeito a melhorias/alterações ao longo do tempo.

# Flask-SQLAlchemy-CRUD

Este exemplo cria uma aplicação Flask que interage com um banco de dados contendo duas tabelas: User (Usuário) e Post (Postagem). Vamos explorar as funcionalidades de criação, leitura, atualização e exclusão de dados (CRUD).

## 1. Instalação dos pacotes necessários

Primeiramente, instale o Flask e o SQLAlchemy, executando o seguinte comando:

pip install flask sqlalchemy flask-sqlalchemy

## 2. Estrutura do Projeto

Aqui está a estrutura básica do projeto que vamos criar:

flask_app/
│
├── app.py
├── config.py
└── database.db (criado automaticamente após rodar o app)

## 3. Arquivo config.py (Configuração da aplicação)

Este arquivo contém a configuração do banco de dados SQLite.

## 4. Arquivo app.py (Aplicação Flask)

Este é o arquivo principal da aplicação, onde criaremos as rotas e configuraremos o SQLAlchemy.

## 5. Templates (HTML)

Exemplos dos Templates HTML. Coloque-os em uma pasta chamada templates dentro da pasta flask_app.

- users.html (Lista de Usuários)
- new_user.html (Formulário para Novo Usuário)
- posts.html (Lista de Postagens de um Usuário)
- new_post.html (Formulário para Nova Postagem)

## 6. Explicação

Configuração: O arquivo config.py contém as configurações do banco de dados, incluindo o caminho do arquivo SQLite.

Modelos: User e Post são as tabelas do banco de dados. Um User pode ter várias postagens (relacionamento 1 para N).

Rotas:

/users: Exibe todos os usuários.

/user/new: Formulário para criar um novo usuário.

/user/<int:user_id>/posts: Exibe todas as postagens de um usuário.

/post/new: Formulário para criar uma nova postagem associada a um usuário.

## 7. Executando a Aplicação

Para executar a aplicação, abra o terminal e execute:

python app.py

Acesse a aplicação em http://127.0.0.1:5000/.

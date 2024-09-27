# 🚀 Flask-SQLAlchemy-CRUD

Este projeto é uma aplicação Flask que interage com um banco de dados SQLite, contendo duas tabelas principais: **User (Usuário)** e **Post (Postagem)**. Vamos explorar as funcionalidades de **CRUD** (Criar, Ler, Atualizar, Excluir) de forma simples e prática.

---

## 📦 1. Instalação dos Pacotes Necessários

Para começar, você precisará instalar os pacotes do Flask e do SQLAlchemy. Execute o seguinte comando no terminal:

```bash
pip install flask sqlalchemy flask-sqlalchemy
```

---

## 🏗️ 2. Estrutura do Projeto

Aqui está a estrutura básica do projeto que vamos criar:

```
flask_app/
│
├── templates/
│      │
│      ├── new_post.html
│      ├── new_user.html
│      ├── posts.html
│      └──users.html
│
├── app.py               # Arquivo principal da aplicação
├── config.py            # Configurações da aplicação
└── database.db          # Banco de dados SQLite (criado automaticamente)
```

---

## ⚙️ 3. Arquivo `config.py` (Configuração da Aplicação)

Este arquivo contém todas as configurações necessárias para a aplicação, incluindo a configuração do banco de dados SQLite e uma chave secreta para segurança.

### Exemplo de `config.py`:
```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  # Defina uma chave secreta
```

---

## 📜 4. Arquivo `app.py` (Aplicação Flask)

Este é o arquivo principal da aplicação. Aqui, você configurará as rotas e o SQLAlchemy para interagir com o banco de dados.

### Exemplo de `app.py`:
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o banco de dados com SQLAlchemy
db = SQLAlchemy(app)

# Define o modelo de User (Usuário)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

# Define o modelo de Post (Postagem)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Cria o banco de dados
with app.app_context():
    db.create_all()

# Rota para exibir todos os usuários
@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

# Rota para criar um novo usuário
@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return render_template('new_user.html')

# Rota para visualizar postagens de um usuário
@app.route('/user/<int:user_id>/posts')
def user_posts(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template('posts.html', user=user, posts=posts)

# Rota para criar uma nova postagem
@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = request.form['user_id']
        new_post = Post(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('user_posts', user_id=user_id))
    users = User.query.all()
    return render_template('new_post.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🖥️ 5. Templates (HTML)

Os templates HTML devem ser colocados em uma pasta chamada **templates** dentro da pasta `flask_app`. Aqui estão alguns exemplos de templates que você pode criar:

- **users.html**: Lista de Usuários
- **new_user.html**: Formulário para Novo Usuário
- **posts.html**: Lista de Postagens de um Usuário
- **new_post.html**: Formulário para Nova Postagem

### Exemplo de `users.html`:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Lista de Usuários</title>
</head>
<body>
    <h1>👥 Lista de Usuários</h1>
    <!-- Conteúdo da lista de usuários -->
</body>
</html>
```

---

## 📝 6. Explicação

### **Configuração**:
O arquivo `config.py` contém as configurações do banco de dados, incluindo o caminho do arquivo SQLite e uma chave secreta.

### **Modelos**:
Os modelos **User** e **Post** representam as tabelas do banco de dados. Um **User** pode ter várias postagens, estabelecendo um relacionamento 1 para N.

### **Rotas**:
- **/users**: Exibe todos os usuários.
- **/user/new**: Formulário para criar um novo usuário.
- **/user/<int:user_id>/posts**: Exibe todas as postagens de um usuário.
- **/post/new**: Formulário para criar uma nova postagem associada a um usuário.

---

## 🚀 7. Executando a Aplicação

Para executar a aplicação, abra o terminal e execute o seguinte comando:

```bash
python app.py
```

Acesse a aplicação em [http://127.0.0.1:5000/](http://127.0.0.1:5000/) no seu navegador.

---

## 🌟 Conclusão

Este projeto serve como uma base para você desenvolver uma aplicação CRUD com Flask e SQLAlchemy. Você pode expandir a funcionalidade, adicionar novos recursos e estilizar os templates como preferir. Divirta-se programando! 🎉
```

### Melhoria e Estilização:
- **Detalhamento de `config.py` e `app.py`**: Incluí exemplos dos códigos completos para melhor compreensão.
- **Estrutura e clareza**: Mantive uma estrutura clara e organizada.
- **Emojis e estilo**: Mantive os emojis para tornar a leitura mais agradável.

Sinta-se à vontade para personalizar ainda mais conforme necessário!

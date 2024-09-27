# app.py
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

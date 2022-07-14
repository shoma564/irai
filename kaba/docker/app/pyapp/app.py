from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
# from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
# from werkzeug.security import generate_password_hash, check_password_hash
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jisyu.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

# DBのモデル
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    due = db.Column(db.DateTime, nullable=False)

# class User(UserMixin, db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(50), nullable=False, unique=True)
# 	password = db.Column(db.String(25))


# サインアップ
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == "POST":
#         username = request.form.get('username')
#         password = request.form.get('password')
#         # Userのインスタンスを作成
#         user = User(username=username, password=generate_password_hash(password, method='sha256'))
#         db.session.add(user)
#         db.session.commit()
#         return redirect('/login')
#     else:
#         return render_template('signup.html')

# ログイン
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         username = request.form.get('username')
#         password = request.form.get('password')
#         # Userテーブルからusernameに一致するユーザを取得
#         user = User.query.filter_by(username=username).first()
#         if check_password_hash(user.password, password):
#             login_user(user)
#             return redirect('/')
#     else:
#         return render_template('login.html')

# #ログアウト
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect('/login')

#一覧？
@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

    else:
        num = request.form.get('num')
        time = request.form.get('time')
        due = request.form.get('due')
        
        due = datetime.datetime.strptime(due, '%Y-%m-%d')
        new_post = Post(num=num, time=time, due=due)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

#新規作成
@app.route('/create')
# @login_required
def create():
    return render_template('create.html')

#削除
@app.route('/delete/<int:id>')
# @login_required
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

#グラフ
@app.route('/graph')
def graph():
#   posts = Post.query.all()
    td = datetime.date.today() 
    yd1 = td - datetime.timedelta(days=1)
    yd2 = td - datetime.timedelta(days=2)
    yd3 = td - datetime.timedelta(days=3)
    yd4 = td - datetime.timedelta(days=4)
    yd5 = td - datetime.timedelta(days=5)
    yd6 = td - datetime.timedelta(days=6)

    jisyuu = Post.query.filter(Post.time == 3)
    print({jisyuu.time})
    return render_template('graph.html' , td=td, yd1=yd1, yd2=yd2, yd3=yd3, yd4=yd4, yd5=yd5,  yd6=yd6, jisyuu=jisyuu)

if __name__ == "__main__":
    app.run(debug=True)

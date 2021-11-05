from app import app, db
from flask import render_template, redirect, flash
from app.forms import Login, Register, PostForm
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required



@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
@login_required
def index():
    form = PostForm()
    posts = Post.query.all()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user.username)
        db.session.add(post)
        db.session.commit()
        return redirect('/index')
    return render_template('index.html', title='Home', form=form, posts=posts)

@app.route('/deletep/<pid>')
@login_required
def deletep(pid):
    post = Post.query.get(pid)
    db.session.delete(post)
    db.session.commit()
    return redirect('/index')

@app.route('/deleteu')
@login_required
def deleteu():
    user = User.query.get(current_user.id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/index')


@app.route('/login', methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user)
        flash('Login Successful')
        return redirect("/index")
    return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = Register()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

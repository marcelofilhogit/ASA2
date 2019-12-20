from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from flaskblog import app
from dbUtils import *
from datetime import date

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Posts')


@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html', title='Register')

@app.route('/registerUser', methods=['POST'])
def registerUser():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    banco = DbUtils()
    result = banco.newUser(username, email, password)
    if(result == True):
        return redirect(url_for('login', email = email, usuario = usuario))
    return jsonify(result)
    
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', title='Login')

@app.route('/authUser', methods=['POST'])
def authUser():
    email = request.form["email"]
    password = request.form["password"]
    banco = DbUtils()
    result = banco.authUser(email, password)
    if(result):
        return redirect(url_for('account', user = result))
    return False

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET'])
# @login_required
def account():
    return render_template('account.html', title='Account')

# @app.route('/getPosts', methods=['GET'])
# def account():
#     banco = DbUtils()
#     result = banco.getPosts()
#     return jsonify(result)

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    return render_template('create_post.html', title='Novo Post', legend='Novo Post')

@app.route('/registerPost', methods=['POST'])
def registerPost():
    user_id = '69'
    title = request.form["title"]
    date_posted = date.today()
    content = request.form["content"]
    banco = DbUtils()
    result = banco.registerPost(user_id, title, date_posted, content)
    # if(result == True):
    #     return redirect(url_for('/account', result = result))
    return jsonify(result)

@app.route("/post/<int:post_id>")
def post(post_id):
    # post = Post.query.get_or_404(post_id)
    # return render_template('post.html', title=post.title, post=post)
    return render_template('post.html')


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
def update_post(post_id):
    # post = Post.query.get_or_404(post_id)
    # if post.author != current_user:
    #     abort(403)
    # form = PostForm()
    # if form.validate_on_submit():
    #     post.title = form.title.data
    #     post.content = form.content.data
    #     db.session.commit()
    #     flash('Post editado com sucesso!', 'success')
    #     return redirect(url_for('post', post_id=post.id))
    # elif request.method == 'GET':
    #     form.title.data = post.title
    #     form.content.data = post.content
    # return render_template('create_post.html', title='Editar Post', form=form, legend='Update Post')
    return render_template('create_post.html', title='Editar Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
# @login_required
def delete_post(post_id):
    return redirect(url_for('account'))

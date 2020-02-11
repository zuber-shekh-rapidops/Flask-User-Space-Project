from flask import Blueprint,render_template,flash,redirect,url_for,request
from userspaceapp import db
from userspaceapp.post.forms import AddPostForm
from userspaceapp.post.models import Post
from flask_login import login_required,current_user

post=Blueprint('post',__name__)


@post.route('/addPost',methods=['GET','POST'])
@login_required
def add_post():
    form_label='add new post'
    form=AddPostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data,content=form.content.data,user=current_user)
        db.session.add(post)
        db.session.commit()
        flash('post Added')
        return redirect(url_for('users.posts'))
    return render_template('add_post.html',form=form,form_label=form_label)


@post.route('/post/<int:post_id>')
@login_required
def view_post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('view_post.html',post=post)


@post.route('/post/update/<int:post_id>',methods=['GET','POST'])
@login_required
def update_post(post_id):
    form_label='update_post'
    form=AddPostForm()
    post=Post.query.get_or_404(post_id)
    
    if request.method=='GET':
        form.title.data=post.title
        form.content.data=post.content

    if form.validate_on_submit():
        # post=Post.query.get_or_404(post_id)
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('post updated')
        return redirect(url_for('users.posts'))

    return render_template('add_post.html',form=form,form_label=form_label)


@post.route('/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('post deleted')
    return redirect(url_for('users.posts'))
import json
import ast

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project.models.models import User, Product
from project import db


admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        current_user = User.find_by_username(username)
        if not current_user:
            flash('ERROR! user not found.', 'error')
            return redirect(url_for('admin.dashboard'))


        if User.verify_hash(password, current_user.password):
            current_user.authenticated = True
            db.session.add(current_user)
            db.session.commit()
            login_user(current_user)
            if current_user.role == 'admin':
                return redirect(url_for('admin.dashboard'))
            else:
                return redirect(url_for('home.home'))

        else:
            db.session.rollback()
            flash('ERROR! Incorrect login credentials.', 'error')

    return render_template('login.html')


@admin_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('admin.login'))


@admin_blueprint.route('/admin')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    return render_template('dashboard.html')



# Products ############################################
@admin_blueprint.route('/admin/products')
@login_required
def products():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    all_product = Product.query.all()
    return render_template('products.html', products=all_product)



# Products ############################################
@admin_blueprint.route('/admin/products_add', methods=['GET', 'POST'])
@login_required
def products_add():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    if request.method == 'POST':
        try:
            file = request.files['json']
            json_data = json.loads(file.read().decode('utf-8'))

            for data in json_data:
                new_product = Product(
                    title=data['title'],
                    description=data['description'],
                    stock=data['stock'],
                    url=data['url'],
                    image=data['image'],
                    price=data['price'],
                    category=data['category']
                )
                db.session.add(new_product)

            db.session.commit()
            return redirect(url_for('admin.products'))

        except IntegrityError as e:
            db.session.rollback()
            flash('ERROR! {}'.format(e), 'error')

    return render_template('products_add.html')


@admin_blueprint.route('/admin/products_delete', methods=['GET', 'POST'])
@login_required
def products_delete():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    try:
        db.session.query(Product).delete()
        db.session.commit()
        return redirect(url_for('admin.products'))

    except IntegrityError as e:
        db.session.rollback()
        flash('ERROR! {}'.format(e), 'error')


# USERS ############################################
@admin_blueprint.route('/admin/users')
@login_required
def users():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    all_user = User.query.all()
    return render_template('users.html', users=all_user)


@admin_blueprint.route('/admin/user_add', methods=['GET', 'POST'])
@login_required
def user_add():
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = User.generate_hash(request.form.get('password'))
            is_admin = request.form.get('is-admin')
            if is_admin:
                new_user = User(username, password, role='admin')
            else:
                new_user = User(username, password)

            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('admin.users'))

        except IntegrityError:
            db.session.rollback()
            flash('ERROR! username ({}) already exists.'.format(username), 'error')

    return render_template('user_add.html')


@admin_blueprint.route('/admin/user_delete/<user_id>')
@login_required
def user_delete(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    user = User.find_by_id(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin.users'))


@admin_blueprint.route('/admin/user_edit/<user_id>', methods=['GET', 'POST'])
@login_required
def user_edit(user_id):
    if current_user.role != 'admin':
        return redirect(url_for('home.home'))

    user = User.find_by_id(user_id)
    if request.method == 'POST':
        try:
            is_admin = request.form.get('is-admin')
            password = request.form.get('password')

            user.username = request.form.get('username')
            # user.password = User.generate_hash(password)
            # if User.verify_hash(password, current_user.password):
            #     user.password = password

            user.address = request.form.get('address')
            if is_admin:
                user.role = 'admin'

            db.session.commit()
            return redirect(url_for('admin.users'))

        except IntegrityError:
            db.session.rollback()
            flash('ERROR! username ({}) already exists.'.format(user.username), 'error')

    return render_template('user_edit.html', user=user)



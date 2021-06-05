import math

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError

from project.models.models import User, Product
from project import db


home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    page=1
    if request.args.get('page'):
        page = int(request.args.get('page'))
    per_page = 12
    all_product = Product.query.paginate(page,per_page,error_out=False)
    rows = Product.query.count()
    total_page = math.ceil(rows/12)


    return render_template('index.html', products=all_product, total=total_page)


@home_blueprint.route('/<url>', methods=['GET', 'POST'])
@login_required
def detail(url):
    product = Product.query.filter_by(url=url).first()
    return render_template('product.html', product=product)


@home_blueprint.route('/cat/<cat>', methods=['GET', 'POST'])
@login_required
def category(cat):
    products = Product.query.filter(Product.category==cat).all()
    return render_template('categories.html', products=products)


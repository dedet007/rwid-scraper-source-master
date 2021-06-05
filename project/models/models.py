from project import db

from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False, unique=True,)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String, default='user')
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, role='user'):
        self.username = username
        self.password = password
        self.role = role
        self.authenticated = False

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def __repr__(self):
        return '<title {}'.format(self.username)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    stock = db.Column(db.String)
    url = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.String)
    category = db.Column(db.String)

    def __init__(self, title, description, stock, url, image, price, category):
        self.title = title
        self.description = description
        self.stock = stock
        self.url = url
        self.image = image
        self.price = price
        self.category = category

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()
from flask import Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return '<h1> Welcome to my home page!</h1>'

@site.route('/contact')
def contact():
    return '<h1> Welcome to the contact page!</h1>'


@site.route('/about')
def about():
    return '<h1> Welcome to the about page...not much to see</h1>'


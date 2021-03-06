from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.jinja')


@main.route('/about')
def about():
    return render_template('about.jinja')


@main.route('/markdown')
def markdown():
    return render_template('markdown.jinja')

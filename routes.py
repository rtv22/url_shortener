from flask import Blueprint, render_template, request, redirect

import requests
from extensions import db
from models import Link
import re

short = Blueprint('short', __name__)


@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits += 1
    db.session.commit()

    return redirect(link.original_url)


@short.route('/')
def index():
    return render_template('index.html')


@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']

    if len(original_url) and len(re.findall(r'(http|https):\/\/\w+.(\w+)', original_url)) != 0:
        if requests.get(original_url).status_code == 200:

            link = Link(original_url=original_url)
            db.session.add(link)
            db.session.commit()

            return render_template('link_added.html',
                                   new_link=link.short_url,
                                   original_url=link.original_url)
        else:
            return render_template('page_404.html'), 404
    return render_template('page_404.html'), 404


@short.route('/stats')
def stats():
    links = Link.query.all()

    return render_template('stats.html',
                           links=links)


@short.errorhandler(404)
def page_not_fount(e):
    return render_template('page_404.html'), 404

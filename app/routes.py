from app import app
from flask import render_template, request, redirect, url_for
from .color_palette_generator import get_colors


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            colors = get_colors(f)
            return redirect(url_for('effect'))
    return render_template('index.html')


@app.route('/effect')
def effect():
    colors = request.args.get('colors')
    return render_template('effect.html')

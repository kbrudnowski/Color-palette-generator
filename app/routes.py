from app import app
from flask import render_template, request, redirect, url_for
from .color_palette_generator import get_colors


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files.get('file')
        colors = get_colors(f)
        print(colors)
        return render_template('effect.html', colors = colors)
    return render_template('index.html')

from app import app
from flask import render_template, request, session
from .color_palette_generator import get_colors
import json


@app.route('/', methods=['GET', 'POST'])
def generate_colors():
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            session['colors'] = get_colors(f)
    return render_template('index.html')


@app.route('/effect/')
def effect():
    if session['colors'] is not None:
        colors_json_str = session.get(
            'colors', '{}'
        )
        colors_dict = json.loads(colors_json_str)
    else:
        colors_dict = {"colors": ['#000000', '#ff0000', '#ffffff', '#ff0000']}

    colors_list = colors_dict['colors']

    return render_template('effect.html', colors=colors_list)

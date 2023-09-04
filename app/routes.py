from app import app
from flask import render_template, request, session
from .color_palette_generator import get_colors


@app.route('/', methods=['GET', 'POST'])
def generate_colors():
    if request.method == 'POST':
        f = request.files.get('file')
        if f:
            colors_list = get_colors(f)
            session['color_1'] = colors_list[0]
            session['color_2'] = colors_list[1]
            session['color_3'] = colors_list[2]
            session['color_4'] = colors_list[3]
    return render_template('index.html')

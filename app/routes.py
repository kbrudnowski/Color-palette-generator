from app import app
from flask import render_template, request, session, jsonify
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
            print('colors changed')
    return render_template('index.html')


@app.route('/get_updated_colors', methods=['GET'])
def get_updated_colors():
    # Access the session variables here
    color_1 = session['color_1']
    color_2 = session['color_2']
    color_3 = session['color_3']
    color_4 = session['color_4']

    # Return the updated colors as JSON
    return jsonify({
        'color_1': color_1,
        'color_2': color_2,
        'color_3': color_3,
        'color_4': color_4
    })
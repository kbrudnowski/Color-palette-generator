from flask import Flask
from flask_dropzone import Dropzone

app = Flask(__name__)
app.debug = True

app.config['DROPZONE_MAX_FILES'] = 1
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
app.config['DROPZONE_MAX_FILE_SIZE'] = 5

dropzone = Dropzone(app)

from app import routes

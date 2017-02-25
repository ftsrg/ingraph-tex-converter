#!/usr/bin/env python3

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/sources'
ALLOWED_EXTENSIONS = set(['tex'])

RESOURCE_FOLDER = 'resources'
RELALG_FRAGMENT_KEY = 'is_relalg_fragment'
ENVELOPE_PLACEHOLDER = '% INSERT_CONTENT_HERE'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            is_relalg_fragment = RELALG_FRAGMENT_KEY in request.form and request.form.get(RELALG_FRAGMENT_KEY)=='1'
            if is_relalg_fragment:
                with open(os.path.join(RESOURCE_FOLDER, 'relalg-envelope.tex'), 'r') as envelope_file:
                    envelope = envelope_file.read()
                standalone_doc = envelope.replace(ENVELOPE_PLACEHOLDER, file.read().decode("utf-8"))
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as standalone_doc_file:
                    standalone_doc_file.write(standalone_doc)
            else:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <html>
    <head>
    <title>ingraph-tex-converter</title>
    </head>
    <body>
    <h1>ingraph-tex-converter</h1>
    <form method="post" enctype="multipart/form-data">
      <p><input type="file" name="file">
         <input type="submit" value="Upload">
      </p>
      <p>
         <input type="checkbox" id="''' + RELALG_FRAGMENT_KEY + '''" name="''' + RELALG_FRAGMENT_KEY + '''" value="1" > <label for="''' +RELALG_FRAGMENT_KEY + '''">Relalg TeX fragment only.</label>
      </p>
    </form>
    </body>
    </html>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    filename = secure_filename(filename)
    pdf_filename = filename.rsplit(".", 1)[0] + ".pdf"
    os.system("bash -c 'cd " + app.config['UPLOAD_FOLDER'] + " && latexmk -xelatex -quiet " + filename + "'")
    return send_from_directory(app.config['UPLOAD_FOLDER'], pdf_filename)

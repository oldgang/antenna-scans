from flask import Flask, render_template, request, redirect, url_for, flash, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from main import readData
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.txt']
app.config['UPLOAD_PATH'] = 'uploads'
db = SQLAlchemy(app)

class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(17), nullable=False)
    ssid = db.Column(db.String(30), nullable=False)
    channel = db.Column(db.Integer, nullable=False)
    signal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Scan %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html', text=readData(os.path.join(app.config['UPLOAD_PATH'], 'scan.txt')))

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], 'scan.txt'))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)






































# from flask import Flask, render_template, request, redirect, url_for, flash, abort, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
# app.config['UPLOAD_EXTENSIONS'] = ['.txt']
# app.config['UPLOAD_PATH'] = 'uploads'
# db = SQLAlchemy(app)

# class Scan(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     mac = db.Column(db.String(17), nullable=False)
#     ssid = db.Column(db.String(30), nullable=False)
#     channel = db.Column(db.Integer, nullable=False)
#     signal = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return '<Scan %r>' % self.id

# @app.route('/')
# def index():
#     files = os.listdir(app.config['UPLOAD_PATH'])
#     return render_template('index.html', files=files)

# @app.route('/', methods=['POST'])
# def upload_files():
#     uploaded_file = request.files['file']
#     filename = secure_filename(uploaded_file.filename)
#     if filename != '':
#         file_ext = os.path.splitext(filename)[1]
#         if file_ext not in app.config['UPLOAD_EXTENSIONS']:
#             abort(400)
#         uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#     return redirect(url_for('index'))

# @app.route('/uploads/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)

# if __name__ == "__main__":
#     app.run(debug=True)
from importlib.metadata import files
from pdb import post_mortem
from pickle import GET
from flask import Flask, render_template, Blueprint, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
#in terminal install 
#pip install flask 
#pip install flask_wtf wtforms


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'



class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


static = Blueprint('static',__name__, template_folder='static')


@app.route('/', methods=['GET',"POST"])

@app.route('/home', methods=['GET',"POST"])

# @static.route('/static/files')
# def static_list():
#     q = request.args.get('q')

#     if q:
#         static = files.query.filter(files.title.contains(q) | files.body.contains(q))
#     else:
#         static = files.query.all()
#     return render_template('static/static.html', static=static)



def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data 
        # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) 
        # Then save the file
        return render_template('downloads.html', form=form)
        # Need to add display file as next step
    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
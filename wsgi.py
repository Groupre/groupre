'''Website module.'''

import csv
import os
from random import randint

from flask import (Flask, Response, flash, redirect, render_template, request,
                   url_for)
from werkzeug.utils import secure_filename

# relies on groupre having been installed to the machine running this script
import groupre

UPLOAD_FOLDER = os.getcwd() + '/uploads/'
ALLOWED_EXTENSIONS = set(['csv'])

application = Flask(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def run_groupre(filename, row_count):
    main_dir = os.path.dirname(os.path.realpath(__file__))
    test_location = os.path.join(main_dir, 'static/test/randomizedTests/')
    chairs = os.path.join(test_location, 'chairs/')
    students = filename
    output_name = UPLOAD_FOLDER + 'output/' + \
        str(randint(1000000, 9999999)) + '-' + str(randint(1000000, 9999999))
    # output_name = os.path.join(UPLOAD_FOLDER, 'output/output.csv')
    if 'fallback' in filename:
        chairs = os.path.join(
            main_dir, 'static/test/testFiles/fallback/chairs_fallback.csv')
        groupre.main(['--fallback', '--chairs', chairs,
                      '--students', students, '--output', output_name])
        return output_name
    if row_count <= 101:
        chairs = os.path.join(chairs, 'test_chairs_demo_100.csv')
    elif row_count <= 401:
        chairs = os.path.join(chairs, 'test_chairs_demo_400.csv')
    elif row_count <= 1001:
        chairs = os.path.join(chairs, 'test_chairs_demo_1000.csv')
    else:
        chairs = os.path.join(chairs, 'test_chairs_1.csv')
        students = os.path.join(test_location, 'test_students_1.csv')
        output_name = os.path.join(UPLOAD_FOLDER, 'test_output_1.csv')
    arguments = ['--chairs', chairs, '--students',
                 students, '--output', output_name]
    groupre.main(arguments)
    return output_name


def make_tree(path):
    tree = dict(name=path.split('/')[-2], children=[])
    try:
        lst = os.listdir(path)
    except OSError:
        pass  # ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree


@application.route("/")
def hello():
    return render_template('index.html')


@application.route("/docs/")
def docs():
    path = os.path.dirname(os.path.realpath(__file__)) + '/static/docs/'
    return render_template('dirtree.html', tree=make_tree(path))


@application.route('/upload', methods=['GET', 'POST'])
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
            newlocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(newlocation)
            with open(newlocation, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                row_count = sum(1 for row in reader)
            output_name = run_groupre(newlocation, row_count)
            with open(output_name, 'r') as f:
                output = f.read()
            output_name = output_name.split('/')[-1] + '.csv'
            return Response(
                output,
                mimetype="text/csv",
                headers={"Content-disposition":
                         "attachment; filename=" + output_name})
    test_files = {'100 Students': 'test_students_demo_100.csv', '400 Students': 'test_students_demo_400.csv',
                  '1000 Students': 'test_students_demo_1000.csv', 'Fallback Test': 'students_fallback.csv'}
    return render_template('upload.html', test_files=test_files)


@application.route("/metrics/")
def metrics():
    output_name = 'notempty'
    return render_template("metrics.html", output_name=output_name)


# TODO feed output into this URL
@application.route("/download/<string:output_name>", methods=['POST'])
def downloadcsv(output_name):
    # if not allowed_file(output_name):
    #     return "404"
    if 'test' in output_name or 'fallback' in output_name:
        with open(os.getcwd() + "/uploads/testCases/" + output_name) as file:
            csvfile = file.read()
        return Response(
            csvfile,
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=" + output_name})
    with open(os.getcwd() + "/uploads/output" + output_name) as file:
        csvfile = file.read()
    return Response(
        csvfile,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=" + output_name})


if __name__ == "__main__":
    application.run()

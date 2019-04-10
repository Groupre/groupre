'''Website module.'''

import csv
import os
import json
from random import randint
from flask import (Flask, Response, flash, redirect, render_template, request,
                   url_for)
from werkzeug.utils import secure_filename

# relies on groupre having been installed to the machine running this script
# import src.groupre as groupre
# import src.main as groupre_test
#import src.groupre.helpers.postem as postem

UPLOAD_FOLDER = os.getcwd() + '/uploads/'
ALLOWED_EXTENSIONS = set(['csv'])

if os.path.exists('/chairs'):
    CHAIRS_DIR = '/chairs'
else:
    CHAIRS_DIR = UPLOAD_FOLDER + 'chairs/'

if os.path.exists('/classrooms'):
    CLASSROOMS_DIR = '/classrooms'
else:
    CLASSROOMS_DIR = UPLOAD_FOLDER + 'classrooms/'

application = Flask(__name__)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#helper scripts
def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def run_groupre(students, chairs):
    output_name = UPLOAD_FOLDER + 'output/' + \
    str(randint(1000000, 9999999)) + '' + \
    str(randint(1000000, 9999999)) + '.csv'
    # arguments = ['--chairs', chairs, '--students',
    #              students, '--output', output_name]
    # groupre.main(arguments)
    arguments = 'python3.7 ./src/groupre.py -c {} -s {} -o {}'.format(chairs,students,output_name)
    os.system(arguments)
    return output_name
def run_groupre_test (students, chairs):
    output_name = UPLOAD_FOLDER + 'output/' + \
    str(randint(1000000, 9999999)) + '' + \
    str(randint(1000000, 9999999)) + '.csv'
    # arguments = ['--chairs', chairs, '--students',
    #              students, '--output', output_name]
    # groupre.main(arguments)
    arguments = 'python3.7 ./src/test.py -c {} -s {} -o {}'.format(chairs,students,output_name)
    os.system(arguments)
    return output_name

def run_test(students, row_count):
    main_dir = os.path.dirname(os.path.realpath(__file__))
    test_location = os.path.join(main_dir, 'uploads/')
    chairs = os.path.join(main_dir, 'src/python/chairs/')
    # currently, this function will find a seat based on the amount of rows
    # if 'fallback' in students:
    #     chairs = os.path.join(
    #         main_dir, 'static/test/testFiles/fallback/chairs_fallback.csv')
    #     return run_groupre(students, chairs)
    # if row_count <= 101:
    #     chairs = os.path.join(chairs, 'test_chairs_demo_100.csv')
    # elif row_count <= 401:
    #     chairs = os.path.join(chairs, 'test_chairs_demo_400.csv')
    # elif row_count <= 1001:
    #     chairs = os.path.join(chairs, 'test_chairs_demo_1000.csv')
    # else:
    #     # only for testing responses
    #     chairs = os.path.join(chairs, 'test_chairs_1.csv')
    #     students = os.path.join(test_location, 'test_students_1.csv')
    #     output_name = os.path.join(UPLOAD_FOLDER, 'test_output_1.csv')
    return run_groupre(students, chairs)

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())
def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

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
    return render_template('index.html', title = "Home")


@application.route("/docs/")
def docs():
    path = os.path.dirname(os.path.realpath(__file__)) + '/static/docs/archive'
    return render_template('dirtree.html', tree=make_tree(path))


@application.route('/template/<string:jsonName>',methods = ['GET','POST'])
def retrieve_file(jsonName):
    # returns json files to javascript
    filepath =CLASSROOMS_DIR + jsonName
    with open(filepath, 'r') as f:
        jdata = json.load(f)
    return render_template('groupreTeam.html', jdata = jdata , name = jsonName, title = "Create Team")

@application.route('/chair/<string:jsonName>',methods = ['GET','POST'])
def retrieve_team(jsonName):
    # returns json files to javascript
    jdata = []
    filepath =CHAIRS_DIR + jsonName
    print(filepath)
    with open(filepath, 'r') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            jdata.append(row)
        # jdata = json.load(jdata)
    return render_template('editTeam.html', jdata = jdata , name = jsonName, title = "Edit Team")

@application.route('/class/<string:jsonName>',methods = ['GET','POST'])
def retrieve_class(jsonName):
    # returns json files to javascript
    filepath =CLASSROOMS_DIR + jsonName
    with open(filepath, 'r') as f:
        jdata = json.load(f)
    return render_template('editClass.html', jdata = jdata , name = jsonName, title = "Edit Template")

  
@application.route('/upload/<string:roomID>', methods=['GET', 'POST'])
def upload_file(roomID):
    # This is options for grouping
    fallback = False
    # gender = False
    # mHighLow = False
    # mAverage = False
    test = False
    if request.method == 'POST':
        # check if any of the options were checked for groupre
        # if (request.form.get('teamOpt') == "gender"):
        #     gender = True
        # elif (request.form.get('teamOpt') == "highlow"):
        #     mHighLow = True
        # elif (request.form.get('teamOpt') == "average"):
        #     mAverage = True
        if (request.form.get('teamOpt')) == 'test':
            test = True
        if 'file' not in request.files:
          #  flash('No file part')
            flash('Your file doesnt exist')
            return redirect(url_for('selectRoom'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('selectRoom'))
        if file and allowed_file(file.filename):
        
            filename = secure_filename(file.filename)
            newlocation = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(newlocation)
            capacity = int(roomID.split('-')[-2]) * int(roomID.split('-')[-1])
            with open(newlocation, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                row_count = sum(1 for row in reader) - 1
            if row_count > capacity:
                flash('Students more than num of seats')
                return redirect(url_for('selectRoom'))
            
            roomID = CHAIRS_DIR + roomID + '.csv'
            if test:
                output_name = run_groupre_test(newlocation, roomID)
            else:
                output_name = run_groupre(newlocation, roomID)

            
            output_name = output_name.split('/')[-1].split('.', 1)[0]
            return redirect('/metrics/' + output_name)
    return render_template('upload.html', title = "Loaded " + str(roomID))

@application.route("/room-select")
def selectRoom():
    chairFiles = {}
    for cFile in os.listdir(CHAIRS_DIR):
        if '.csv' in cFile:
            cValue = cFile.split('.csv')[0]
            cKey = cValue.split('-')[2:]
            roomID = cKey[0].title()
            capacity = ' ' + str(int(cKey[1]) * int(cKey[2])) + ' Students'
            cKey = roomID + capacity
            # cKey = '-'.join(cValue.split('-')[2:]).title()
            chairFiles.update({cKey:cValue})
    return render_template("room.html", chairFiles=chairFiles, title = "Run Groupre")

@application.route("/metrics/<string:output_name>")
def metrics(output_name):
    metrics = UPLOAD_FOLDER + 'output/' + output_name + '-metrics.txt'
    try:
        with open(metrics, 'r') as f:
            metrics = f.readlines()
        for m in metrics:
            print(m)
        ### bug with postem need to be fixed
        
        # postem.postem(['--output', UPLOAD_FOLDER +
        #                'output/' + output_name + '.csv'])
        return render_template("metrics.html", output_name=output_name, metrics=metrics , title = "Metrics result")
    except FileNotFoundError:
        return render_template("metrics.html", output_name=output_name, title = "Metrics result")

@application.route("/download/<string:output_name>", methods=['POST'])
def downloadcsv(output_name):
    if "room-" in output_name:
        with open(CHAIRS_DIR + output_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            csvfile = []
            for row in reader:
                for field in row:
                    csvfile += str(field) + ','
                csvfile += '\n'
        return Response(
            csvfile,
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=" + output_name})
    if 'test' in output_name or 'fallback' in output_name:
        with open(UPLOAD_FOLDER + "testCases/" + output_name, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            csvfile = []
            for row in reader:
                for field in row:
                    csvfile += str(field) + ','
                csvfile += '\n'
        return Response(
            csvfile,
            mimetype="text/csv",
            headers={"Content-disposition":
                     "attachment; filename=" + output_name})   
    with open(UPLOAD_FOLDER + "output/" + output_name, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        csvfile = []
        for row in reader:
            for field in row:
                csvfile += str(field) + ','
            csvfile += '\n'
    return Response(
        csvfile,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=" + output_name})
# directs to a page that allows user to decide wheather to change template or make new
@application.route("/editTemplate")
def changeTemplate():
    roomFiles = {}
    for rFile in os.listdir(CLASSROOMS_DIR):
        if '.json' in rFile:
            rKey = rFile.split('-')[1] 
            roomFiles[rKey]= rFile

    return render_template('chooseClass.html', roomFiles = roomFiles, title = "Edit Room")


@application.route("/room-creation")
def create_room():
    return render_template('groupreHome.html', title = "Create room")
@application.route("/team-creation")
def create_team():
    roomFiles = {}
    for rFile in os.listdir(CLASSROOMS_DIR):
        if '.json' in rFile:
            rKey = rFile.split('-')[1] 
            roomFiles[rKey]= rFile
    return render_template('chooseTeam.html', roomFiles = roomFiles , title = "Create teams")
@application.route("/team-edition")
def edit_team():
    # chairFiles = {}
    # for cFile in os.listdir(CHAIRS_DIR):
    #     if '.csv' in cFile:
    #         cValue = cFile.split('.csv')[0]
    #         cKey = cValue.split('-')[2:]
    #         roomID = cKey[0].title()
    #         capacity = ' ' + str(int(cKey[1]) * int(cKey[2])) + ' Students'
    #         cKey = roomID + capacity
    #         # cKey = '-'.join(cValue.split('-')[2:]).title()
    #         chairFiles.update({cKey:cValue})
    roomFiles = {}
    for rFile in os.listdir(CHAIRS_DIR):
        if '.csv' in rFile:
            rKey = rFile.split('-')[2] 
            roomFiles[rKey]= rFile
    return render_template('chooseEditTeams.html', roomFiles = roomFiles , title = "Edit teams")

@application.route("/room-saver", methods=['POST'])
def saveRoom():
    content = request.get_json()
    info = content.pop(0)
    filename = []
    for item in info:
        filename.append(str(item))
    filename = '-'.join(filename)
    filename = CHAIRS_DIR + 'room-' + filename + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in content:
            writer.writerow(row)
    return "saved room"
#saves json file from class builder to upload
@application.route("/class-saver", methods=['POST'])
def saveClass():
    content = request.get_json()
    info = content.pop(0)
    filename = []
    for item in info:
        filename.append(str(item))
    filename = '-'.join(filename)
    filename = CLASSROOMS_DIR + 'template-' + filename + '.json'
    with open(filename, 'w') as outfile:
        json.dump(content[1:],outfile,ensure_ascii=False)
    return "saved template"    

if __name__ == "__main__":
    application.secret_key = '5791628bb0b13ce0c676dfde280ba245'
    application.run(debug=True)

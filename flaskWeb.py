from flask import Flask, render_template, make_response,request

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=",",")

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/room_builder")
def about():
    return render_template("room_builder.html")

@app.route("/demo")
def demo():
    return render_template("builderDemo.html")

@app.route("/transform" , methods = ["POST"])
def transform_view():
    file = request.files['data_file']
    if not file:
        return "no file"
    
    file_contents = file.stream.read().decode("utf-8")
    result = transform(file_contents)
    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv" 
    return response

if __name__ == '__main__':
    app.run(debug=True)

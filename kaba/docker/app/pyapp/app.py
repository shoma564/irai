from flask import Flask, render_template, request



app = Flask(__name__, static_folder='./templates/img')


@app.route('/')
def index():
    global name
    return render_template("index.html",name = name)




if __name__ == "__main__":
    app.run(host="0.0.0.0")

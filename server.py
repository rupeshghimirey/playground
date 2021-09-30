from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:num>')
def playbox(num):
    return render_template("box.html", num = num)

@app.route('/play/<int:num>/<string:color>')
def changeBoxWithColor(num, color):
    return render_template("box.html", num = num, color = color)


if __name__=="__main__":
    app.run(debug=True) 
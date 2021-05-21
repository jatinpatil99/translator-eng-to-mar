from flask import *

import translate

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == "POST":
        inp_string = request.form["inputtext"]
        index = translate.transinput(inp_string)
    return render_template("Index.html", output_text ='Marathi translation {}'.format(index))


if __name__ =="__main__":
    app.run(debug=True)






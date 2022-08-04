from flask import Flask, render_template, request
import re
import time
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=["GET","POST"])
def test():

    if request.method == "POST":
        regex_string = str(request.form["regex"])
        text_string = str(request.form["text"])
        count = 0
        #print(text_string)
        string_list = text_string.split("\n")

        output_text = list()
        for i in string_list:
            if bool(re.search(regex_string,i)):
                output_text.append(i)
                count+=1

        print(count)
        print(len(output_text))
        #print(output_text)
    return render_template('index.html',output=output_text,text_string_1=text_string)

if __name__ == '__main__':
    app.run(debug=True)

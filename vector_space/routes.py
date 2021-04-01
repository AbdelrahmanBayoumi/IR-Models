from flask import render_template, url_for, flash, redirect, request
from vector_space import app
from vector_space.vector_space_model import main_fun, format_input, read_file


@app.route('/')
@app.route('/Home')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/rand', methods=['GET', 'POST'])
def rand_handle():
    print("in rand_handle() ...")
    if request.method == 'POST':
        text = str(request.form['text'])
        if text == "":
            return render_template('home.html', query=text, showdata=False)
        return render_template('home.html',
                               list=main_fun(input_str=text, random_files=True),
                               query=text, showdata=True)
    return render_template('home.html', showdata=False)


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    print("in my_form_post() ...")
    if request.method == 'POST':
        text = str(request.form['text'])
        if text == "":
            return render_template('home.html', query=text, showdata=False)
        return render_template('home.html', list=main_fun(text), query=text, showdata=True)
    return render_template('home.html', showdata=False)


@app.route('/<name>')
def result(name):
    print("name : ", name)
    if name == 'favicon.ico':
        print("in favicon.ico condition ...")
        return render_template('result.html', k=read_file("files/"+name), text=name, title=name)
    return render_template('result.html', title=name, k=read_file("files/"+name+".txt"), text=name)

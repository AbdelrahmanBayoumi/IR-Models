import pygal
from flask import render_template, request
from vector_space import app
from vector_space.vector_space_model import main_fun, read_file


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
        d = main_fun(input_str=text, random_files=True)
        sg = Pie(d)
        return render_template('home.html',
                               list=d,
                               query=text, showdata=True, graph_data=sg)
    return render_template('home.html', showdata=False)


@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    print("in my_form_post() ...")
    if request.method == 'POST':
        text = str(request.form['text'])
        if text == "":
            return render_template('home.html', query=text, showdata=False)
        d = main_fun(text)
        sg = Pie(d)
        return render_template('home.html', list=d, query=text, showdata=True, graph_data=sg)
    return render_template('home.html', showdata=False)


@app.route('/<name>')
def result(name):
    print("name : ", name)
    if name == 'favicon.ico':
        print("in favicon.ico condition ...")
        return render_template('result.html', k=read_file("files/" + name), text=name, title=name)
    return render_template('result.html', title=name, k=read_file("files/" + name + ".txt", gui=True), text=name)


def Pie(dict_out):
    try:
        pie_chart = pygal.Pie()
        pie_chart.title = "Pie Chart"
        pie_chart = pygal.Pie(inner_radius=.4)
        for i in dict_out:
            pie_chart.add(str(i), float(dict_out[i][0]) * 100)
        graph_data = pie_chart.render_data_uri()
        return graph_data
    except Exception as e:
        print(e)
        return None

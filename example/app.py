from flask import Flask, render_template
from flask.ext.wtf import Form
from flask.ext.pagedown import PageDown
from flask.ext.pagedown.fields import PageDownField
from wtforms.fields import SubmitField

app = Flask(__name__)
pagedown = PageDown(app)

class PageDownFormExample(Form):
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = PageDownFormExample(csrf_enabled = False)
    text = None
    if form.validate_on_submit():
        text = form.pagedown.data
    form.pagedown.data = '# This is a demo of Flask-PageDown\n**Markdown** is rendered on the fly in the <i>preview area</i>!'
    return render_template('index.html', form = form, text = text)

@app.route('/with_callback', methods = ['GET', 'POST'])
def index_with_callback():
    form = PageDownFormExample(csrf_enabled = False)
    text = None
    if form.validate_on_submit():
        text = form.pagedown.data
    form.pagedown.data = '# This is a demo of Flask-PageDown\n**Markdown** is rendered on the fly in the <i>preview area</i>!'
    return render_template('index_with_callback.html', form = form, text = text)


if __name__ == '__main__':
    app.run(debug = True)

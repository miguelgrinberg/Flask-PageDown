from flask import Flask, render_template
from flask_wtf import Form
from flask_pagedown import PageDown
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
pagedown = PageDown(app)


class PageDownFormExample(Form):
    pagedown = PageDownField('Enter your markdown')
    pagedown2 = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PageDownFormExample()
    text = None
    text2 = None
    if form.validate_on_submit():
        text = form.pagedown.data
        text2 = form.pagedown2.data
    else:
        form.pagedown.data = ('# This is demo #1 of Flask-PageDown\n'
                              '**Markdown** is rendered on the fly in the '
                              '<i>preview area below</i>!')
        form.pagedown2.data = ('# This is demo #2 of Flask-PageDown\nThe '
                               '*preview* is rendered separately from the '
                               '*input*, and in this case it is located above.')
    return render_template('index.html', form=form, text=text, text2=text2)


if __name__ == '__main__':
    app.run(debug=True)

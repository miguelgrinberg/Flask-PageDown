Flask-PageDown
==============
Implementation of StackOverflow's "PageDown" markdown editor for Flask and Flask-WTF.

What is PageDown?
-----------------

[PageDown](https://code.google.com/p/pagedown/wiki/PageDown) is the JavaScript [Markdown](http://daringfireball.net/projects/markdown/) previewer used on [Stack Overflow](http://stackoverflow.com/) and all the other question and answer sites in the [Stack Exchange network](http://stackexchange.com/).

Flask-PageDown provides a `PageDownField` class that extends [Flask-WTF](https://flask-wtf.readthedocs.org/en/latest/) with a specialized text area field that renders an HTML preview of the Markdown text on the fly as you type.

Installation
------------

    $ pip install flask-pagedown

Example
-------

An example is worth a thousand words. Below is how to define a Flask-WTF form that includes a PageDown field:

    from flask.ext.wtf import Form
    from flask.ext.pagedown.fields import PageDownField
    from wtforms.fields import SubmitField

    class PageDownFormExample(Form):
        pagedown = PageDownField('Enter your markdown')
        submit = SubmitField('Submit')

The `PageDownField` works exactly like a `TextAreaField` (in fact it is a subclass of it). The handling in view functions is identical. For example:

    @app.route('/', methods = ['GET', 'POST'])
    def index():
        form = PageDownFormExample()
        if form.validate_on_submit():
            text = form.pagedown.data
            # do something interesting with the Markdown text
        return render_template('index.html', form = form)

The extension needs to be initialized in the usual way before it can be used:

    from flask.ext.pagedown import PageDown

    app = Flask(__name__)
    pagedown = PageDown(app)

Finally, the template needs the support Javascript code added, by calling `pagedown.include_pagedown()` somewhere in the page:

    <html>
    <head>
    {{ pagedown.include_pagedown() }}
    </head>
    <body>
        <form method="POST">
            {{ form.pagedown(rows = 10) }}
            {{ form.submit }}
        </form>
    </body>
    </html>

The Javascript classes are imported from a CDN, there are no static files that need to be served by the application. If the request is secure then the Javascript files are imported from an https:// URL to match.

To help adding specific CSS styling the `<textarea>` element has class `flask-pagedown-input` and the preview `<div>` has class `flask-pagedown-preview`. Since the preview `<div>` is generated after the DOM loads, you'll need to create a (JavaScript) function named `flaskPageDownCallBack` that specifies what to do after the preview `<div>` has been created.

    <html>
    <head>
    {{ pagedown.include_pagedown() }}
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            flaskPageDownCallBack = function(){
                //Do whatever you want with $(".flask-pagedown-preview")
            };
        });
    </script>
    </head>
    <body>
        <form method="POST">
            {{ form.pagedown(rows = 10) }}
            {{ form.submit }}
        </form>
    </body>
    </html>


Note that the submitted text will be the raw Markdown text. The rendered HTML is only used for the preview, if you need to render to HTML in the server then use a server side Markdown renderer like [Flask-Markdown](http://pythonhosted.org/Flask-Markdown/).

Also note that the current version does not include a toolbar like the one used by Stack Overflow.

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

An example is worth a thousand words. Below is how to define a simple Flask-WTF form that includes a PageDown field:

    from flask_wtf import Form
    from flask_pagedown.fields import PageDownField
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

    from flask_pagedown import PageDown
    
    app = Flask(__name__)
    pagedown = PageDown(app)

Finally, the template needs the support Javascript code added, by calling `pagedown.include_pagedown()` somewhere in the page:

    <html>
    <head>
    {{ pagedown.include_pagedown() }}
    </head>
    <body>
        <form method="POST">
            {{ form.pagedown(rows=10) }}
            {{ form.submit }}
        </form>
    </body>
    </html>

The Javascript classes are imported from a CDN, there are no static files that need to be served by the application. If the request is secure then the Javascript files are imported from an https:// URL to match.

To help adding specific CSS styling the `<textarea>` element has class `flask-pagedown-input` and the preview `<div>` has class `flask-pagedown-preview`.

With the template above, the preview area is created by the extension right below the input text area. For greater control, it is also possible to render the input and preview areas on different parts of the page. The following example shows how to render the preview area above the input area:

    <html>
    <head>
    {{ pagedown.include_pagedown() }}
    </head>
    <body>
        <form method="POST">
            {{ form.pagedown(only_preview=True) }}
            {{ form.pagedown(only_input=True, rows=10) }}
            {{ form.submit }}
        </form>
    </body>
    </html>

Note that in all cases the submitted text will be the raw Markdown text. The rendered HTML is only used for the preview, if you need to render to HTML in the server then use a server side Markdown renderer like [Flask-Markdown](http://pythonhosted.org/Flask-Markdown/).

Also note that the current version does not include a toolbar like the one used by Stack Overflow.

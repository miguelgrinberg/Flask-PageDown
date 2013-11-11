from jinja2 import Markup
from flask import current_app

class _pagedown(object):
    def include_pagedown(self):
        return Markup('''
<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Converter.min.js"></script>
<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Sanitizer.min.js"></script>
''')

    def html_head(self):
        return self.include_pagedown()

class PageDown(object):
    def __init__(self, app = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['pagedown'] = _pagedown()
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {
            'pagedown': current_app.extensions['pagedown']
        }


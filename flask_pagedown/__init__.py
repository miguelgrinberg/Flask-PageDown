from jinja2 import Markup
from flask import current_app


class _pagedown(object):
    # Default MD urls
    CONVERTER_JS_URL = "//cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Converter.min.js"
    SANITIZER_JS_URL = "//cdnjs.cloudflare.com/ajax/libs/pagedown/1.0/Markdown.Sanitizer.min.js"

    def include_pagedown(self, converter_js=None, sanitizer_js=None):
        """
        Includes required markdown files in the page

        :param str converter_js: Full path to the converter.js file
        :param str sanitizer_js: Full path to the sanitizer.js file
        """

        # If path wasn't passed
        if converter_js is None:
            converter_js = self.__class__.CONVERTER_JS_URL

        # If path wasn't passed
        if sanitizer_js is None:
            sanitizer_js = self.__class__.SANITIZER_JS_URL

        return Markup('''
                    <script type="text/javascript" src={0}></script>
                    <script type="text/javascript" src={1}></script>
                    '''.format(converter_js, sanitizer_js))

        return self.include_pagedown()


class PageDown(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['pagedown'] = _pagedown()
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor():
        return {'pagedown': current_app.extensions['pagedown']}

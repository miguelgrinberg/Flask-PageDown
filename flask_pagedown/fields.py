from wtforms.fields import TextAreaField
from .widgets import PageDown

class PageDownField(TextAreaField):
    widget = PageDown()


from flask import render_template
from flask.views import View


class CoreView(View):
    def __init__(self, template_name):
        self._template_name = template_name

    def dispatch_request(self):
        return render_template(self._template_name)

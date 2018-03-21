from flask import Blueprint, render_template

from ..view_core import CoreView

home_blueprint = Blueprint('home_blueprint', __name__)


class HomeView(CoreView):
    def dispatch_request(self, symbol):
        return render_template(self._template_name)


class GrubView(CoreView):
    def dispatch_request(self, symbol, code):
        return render_template(self._template_name)


class IndexView(CoreView):
    pass

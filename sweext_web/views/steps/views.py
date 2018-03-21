from flask import Blueprint, render_template

from ..view_core import CoreView

steps_blueprint = Blueprint('steps_blueprint', __name__)


class StepsView(CoreView):
    def dispatch_request(self, symbol):
        return render_template(self._template_name)

from flask import Blueprint, render_template
from ..view_core import CoreView

claim_blueprint = Blueprint('claim_blueprint', __name__)


class ClaimView(CoreView):
    def dispatch_request(self, symbol):
        return render_template(self._template_name)

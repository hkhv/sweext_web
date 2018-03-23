from .views import ClaimView, claim_blueprint
from ..url_core import UrlRegister


class ClaimUrlRegister(UrlRegister):
    def views_register():
        claim_view = ClaimView.as_view('claim_view', template_name='claim/claim.html')

        claim_blueprint.add_url_rule('/<string:symbol>/claim/<string:session>',
                                     view_func=claim_view,
                                     methods=['GET', ])

from .views import StepsView
from .views import steps_blueprint
from ..url_core import UrlRegister


class StepsUrlRegister(UrlRegister):
    def views_register():
        steps_view = StepsView.as_view('steps_view', template_name='steps/steps.html')

        steps_blueprint.add_url_rule('/<string:symbol>/steps',
                                     view_func=steps_view,
                                     methods=['GET', ])
